# AutoDeploy-Flask-1
# AutoDeploy-Flask 

A lightweight Flask app for real-time system monitoring (CPU & Memory usage) with Prometheus & Grafana integration. Ideal for DevOps portfolio and Docker orchestration demo.

---

## Features
- Real-time CPU & Memory monitoring using `psutil`
- `/metrics` endpoint compatible with Prometheus scraping
- Grafana dashboard setup with Prometheus data source
- Dockerized setup with `docker-compose`

---

## Project Structure
```
AutoDeploy-Flask/
├── app.py                  # Flask App
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image for Flask app
├── docker-compose.yml      # Service orchestration
├── prometheus/
│   └── prometheus.yml      # Prometheus config
├── .gitignore              # Files to ignore in git
└── README.md               # Project doc (this file)
```

---

## Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/shubhammits/AutoDeploy-Flask-1.git
cd AutoDeploy-Flask-1
```

### 2. Start with Docker Compose
```bash
docker-compose up --build
```

### 3. Access:
- Flask App: http://localhost:5000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000  (default creds: `admin` / `admin`)

---

## Sample Metrics Output (curl http://localhost:5000/metrics)
```
cpu_usage 13.5
memory_usage 28.7
```

---

## Grafana Setup
- Login to Grafana (localhost:3000)
- Add Data Source → Prometheus → URL: `http://prometheus:9090`
- Create Dashboard → New Panel
  - Query: `cpu_usage` or `memory_usage`

---

## .gitignore
```gitignore
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

---

## GitHub Badges & CI (Coming Soon)
- [ ] Add GitHub Actions for lint/test
- [ ] Add DockerHub push on release

---

##  Optional: Integrate with
- AWS EC2 or ECS for cloud deployment
- DockerHub to host your image

---

## Author
**Shubham Nagariya**  
📧 shubhamnagariya1994@gmail.com  
🔗 [LinkedIn](https://in.linkedin.com/in/shivom17)

---


