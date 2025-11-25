## 📡 Complete Observability System – Metrics, Logs & Traces  
### **Using Prometheus • Grafana • Loki • Promtail • Jaeger • Docker Compose**

<img width="1536" height="1024" alt="Architecture Diagram (ASCII)" src="https://github.com/user-attachments/assets/debad095-54d7-4431-95c7-89c9d3415da7" />


---

## 🔥 Overview

This project implements a **complete end-to-end observability system** running entirely on **Docker Compose**, with **no cloud account required**.  
It provides:

✔ Metrics (Prometheus)  
✔ Logs (Loki + Promtail)  
✔ Distributed Traces (Jaeger + OpenTelemetry)  
✔ Dashboards & Visualization (Grafana)

The entire stack runs locally and is designed to simulate **production-grade observability** used by DevOps/SRE teams.

---

## 🎯 Project Objectives

- Build a **cloud-free observability platform**
- Monitor application latency & performance using **Prometheus metrics**
- Centralize logs using **Loki + Promtail**
- Capture full request lifecycle using **Jaeger tracing**
- Visualize everything in **Grafana dashboards**
- Understand how real-world observability stacks work in production

---

## 🛠 Tools & Technologies

| Component      | Purpose |
|----------------|---------|
| **Prometheus** | Metrics collection & scraping |
| **Grafana** | Dashboards for logs, metrics & traces |
| **Loki** | Log aggregation backend |
| **Promtail** | Log collector (scrapes Docker logs) |
| **Jaeger** | Distributed tracing |
| **Flask App** | Sample instrumented service |
| **Docker Compose** | Local orchestration |

---

## 🏛 Architecture Diagram  

```text
                  ┌─────────────────────────────┐
                  │     Sample Flask App        │
                  │  • Metrics (/metrics)       │
                  │  • Logs (stdout)            │
                  │  • Traces (OpenTelemetry)   │
                  └──────────────┬──────────────┘
                                 │
        ┌────────────────────────┼──────────────────────────────┐
        │                        │                              │
┌──────────────┐        ┌─────────────────┐          ┌───────────────────┐
│  Prometheus  │◄───────│ Metrics Export  │          │      Jaeger       │
│   (9090)     │        │  (Scraping)     │◄────────│   Traces Backend  │
└──────────────┘        └─────────────────┘          └───────────────────┘
        │
        │ Scraped Metrics
        ▼
┌──────────────────────────────────────────────────┐
│                     Grafana                       │
│   • Dashboards                                     │
│   • Explore Logs (Loki)                           │
│   • Explore Metrics (Prometheus)                  │
│   • View Traces (Jaeger)                          │
└──────────────────────────────────────────────────┘
        ▲
        │ Logs
┌──────────────┐
│   Loki       │◄─── Promtail (Docker Logs)
└──────────────┘
```

## 📦 Repository Structure
```text
complete-observability-system/
│── app/
│ └── app.py
│── prometheus/
│ └── prometheus.yml
│── loki/
│ └── loki-config.yml
│── promtail/
│ └── promtail-config.yml
│── dashboards/
│ └── grafana-dashboard.json
│── architecture/
│ └── architecture-diagram.png
│── screenshots/
│ └── screenshots-of-ui/
│── docker-compose.yml
│── observability_project_report_final.pdf
│── README.md
```
---
## 🚀How to Run the Project

### 1️⃣ Clone the repository

- git clone https://github.com/YOUR-USERNAME/complete-observability-system.git
- cd complete-observability-system

## 2️⃣ Start all services
- docker compose up -d

## 3️⃣ Access all tools
| Service    | URL                                              |
| ---------- | ------------------------------------------------ |
| Grafana    | [http://localhost:3000](http://localhost:3000)   |
| Prometheus | [http://localhost:9090](http://localhost:9090)   |
| Loki API   | [http://localhost:3100](http://localhost:3100)   |
| Jaeger UI  | [http://localhost:16686](http://localhost:16686) |
| Sample App | [http://localhost:5000](http://localhost:5000)   |

## 📊 Grafana Dashboards Included
This repository includes dashboards for:
- Request count
- Latency distribution
- Error rate
- Log views (Loki)
- Trace views (Jaeger UI)
Dashboard JSONs are stored in:
- /dashboards/
---
## 🔍 Observability Features
## ✅ Metrics (Prometheus)
  - Request count
  - Error count
  - Request duration histogram
  - Scraped every 15 seconds
## ✅ Logs (Loki + Promtail)
  - Scrapes Docker container logs
  - Parses log levels
  - Allows filtering & log querying
## ✅ Traces (Jaeger)
  - End-to-end trace visualization
  - Latency breakdown per span
  - Error tracing
---
## 📄 Documentation:

observability_project_report_final.pdf

https://github.com/Lokesh-Soft-Dev/complete-observability-system/blob/ed208fa4e24a7483577cbc73f25d0f18d0bd422e/observability_project_report.pdf

---
## Screenshots are stored separately:

/screenshots/ (Folder)

---
## 📚 Deliverables Included

✔ docker-compose.yml<br>
✔ Python application code<br>
✔ Prometheus config<br>
✔ Loki config<br>
✔ Promtail config<br>
✔ Grafana dashboards<br>
✔ Architecture diagram<br>
✔ PDF report<br>
✔ Screenshots folder<br>
---
## 🏁 Conclusion

This project demonstrates how metrics, logs, and distributed traces can be combined into a **powerful, unified observability platform**.
# It covers:
    - Monitoring
    - Debugging
    - Performance optimization
    - Root-cause analysis
# Future enhancements:
    - Add Alertmanager
    - Deploy on Kubernetes
    - Add SLO/SLI measurement dashboards
    - Expand microservices with more trace spans
---

## THE SECOND PROJECT, <br>
## Project-Name : 
- *"**devops-ci-cd-simple-app**,"* is completed. <br> 
- All _**Project Details(Screenshots, Scripts Files, Report File)**_ are in this **Repo-link** and the corresponding **link** are provided below...<br>
## 🔗Link : https://github.com/Lokesh-Soft-Dev/devops-ci-cd-simple-app 

---
## 👤 Author

## KANNAIAH LOKESH
## GitHub: https://github.com/Lokesh-Soft-Dev
---
