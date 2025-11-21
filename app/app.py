from flask import Flask, request, jsonify
import logging
import time
import random
from prometheus_client import Counter, Summary, generate_latest, CONTENT_TYPE_LATEST
# OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger("observability_app")

# Prometheus metrics
REQUEST_COUNT = Counter('app_request_count', 'Total request count', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Summary('app_request_latency_seconds', 'Request latency in seconds', ['endpoint'])

# OpenTelemetry tracer to Jaeger
resource = Resource(attributes={"service.name": "observability-sample-app"})
trace.set_tracer_provider(TracerProvider(resource=resource))
jaeger_exporter = JaegerExporter(
    collector_endpoint="http://jaeger:14268/api/traces"
)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))
tracer = trace.get_tracer(__name__)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def index():
    start = time.time()
    with tracer.start_as_current_span("index_handler"):
        # simulate work
        t = random.uniform(0.01, 0.8)
        time.sleep(t)
        status = 200
        REQUEST_COUNT.labels(method='GET', endpoint='/', http_status=str(status)).inc()
        REQUEST_LATENCY.labels(endpoint='/').observe(time.time() - start)
        logger.info("Handled index request", extra={"endpoint": "/", "status": status})
        return jsonify({"message": "Hello from Observability App", "delay": t}), status

@app.route("/error")
def error():
    start = time.time()
    with tracer.start_as_current_span("error_handler"):
        try:
            raise ValueError("Simulated error")
        except Exception as e:
            status = 500
            REQUEST_COUNT.labels(method='GET', endpoint='/error', http_status=str(status)).inc()
            REQUEST_LATENCY.labels(endpoint='/error').observe(time.time() - start)
            logger.exception("Error endpoint raised an exception")
            return jsonify({"error": str(e)}), status

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
