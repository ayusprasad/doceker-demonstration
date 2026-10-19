# Docker Greeting App

[![CI](https://github.com/ayusprasad/doceker-demonstration/actions/workflows/ci.yml/badge.svg)](https://github.com/ayusprasad/doceker-demonstration/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web-000000?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)

A compact Flask greeting app that demonstrates safe form handling and a reproducible Docker image.

## Run locally

### Prerequisites

- Python 3.11 or newer
- Docker Desktop or Docker Engine for the container workflow

### Install and start

~~~bash
git clone https://github.com/ayusprasad/doceker-demonstration.git
cd doceker-demonstration
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
~~~

Open http://127.0.0.1:5000. The form validates empty and oversized submissions and escapes user input before displaying it.

### Docker

~~~bash
docker build -t greeting-demo .
docker run --rm -p 5000:5000 greeting-demo
~~~

## Quality checks

~~~bash
pytest -q
ruff check --select E4,E7,E9,F app.py tests
~~~

GitHub Actions runs lint, tests, compilation, and a Docker build on pushes and pull requests. No credentials or environment variables are required.
