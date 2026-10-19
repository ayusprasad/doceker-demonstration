# 🐳 Docker Demonstration App

A clean, beginner-friendly containerized Flask web application demonstrating how to containerize Python web services, build Docker images, and expose ports.

---

## 🚀 Quickstart

### 1. Run with Docker
```bash
# Build image
docker build -t docker-demo-app .

# Run container
docker run -p 5000:5000 docker-demo-app
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

---

### 2. Run Locally
```bash
pip install -r requirements.txt
python app.py
```
Open [http://localhost:5000](http://localhost:5000).

---

## 📁 Repository Structure
```text
doceker-demonstration/
├── app.py             # Flask application entrypoint
├── Dockerfile         # Docker build definition
├── requirements.txt   # Dependencies (Flask, Gunicorn)
└── README.md          # Guide and quickstart
```