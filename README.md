# 🚀 ML Prediction API with CI/CD

A production-ready Machine Learning Prediction API built using **FastAPI**, **TensorFlow/Keras**, **Docker**, and **GitHub Actions**. The project demonstrates how to deploy a trained image classification model as a scalable REST API, containerize it using Docker, and automate testing and deployment workflows using CI/CD practices.

---

# 📌 Project Overview

Machine learning models are often developed in notebooks but rarely deployed in a production-ready manner. This project bridges that gap by transforming a trained Keras image classification model into a RESTful API that can accept image uploads and return predictions in real time.

The application follows MLOps best practices including:

* Model serving through FastAPI
* Docker containerization
* Automated testing with Pytest
* CI/CD automation using GitHub Actions
* Environment variable configuration
* Structured logging and error handling

---

# ✨ Features

* RESTful API built with FastAPI
* Image Classification using TensorFlow/Keras
* Health Monitoring Endpoint
* Image Upload Support
* Input Validation
* File Size Validation
* Error Handling with Appropriate HTTP Status Codes
* Dockerized Deployment
* Docker Compose Support
* Automated Unit Testing
* GitHub Actions CI/CD Pipeline
* Environment Variable Configuration
* Prediction Example Artifacts

---

# 🛠️ Technology Stack

| Category            | Technology         |
| ------------------- | ------------------ |
| Language            | Python 3.11        |
| Framework           | FastAPI            |
| ML Framework        | TensorFlow / Keras |
| Image Processing    | Pillow             |
| Numerical Computing | NumPy              |
| Data Handling       | Pandas             |
| Testing             | Pytest             |
| Containerization    | Docker             |
| Orchestration       | Docker Compose     |
| CI/CD               | GitHub Actions     |
| API Server          | Uvicorn            |

---

# 📂 Project Structure

```text
ML-PredictionAPI-CICD/

├── .github/
│   └── workflows/
│       └── main.yml
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── model.py
│
├── models/
│   └── my_classifier_model.h5
│
├── tests/
│   └── test_api.py
│
├── predictions/
│   ├── example1.json
│   └── example2.json
│
├── scripts/
│   └── train_model.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── .dockerignore
└── README.md
```

---

# ⚙️ Local Setup

## Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ML-PredictionAPI-CICD
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the API:

```bash
uvicorn src.main:app --reload
```

Open Swagger Documentation:

```text
http://localhost:8000/docs
```

Open Health Endpoint:

```text
http://localhost:8000/health
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t ml-api .
```

## Run Docker Container

```bash
docker run -p 8000:8000 ml-api
```

---

# 🐳 Docker Compose

Run the application using Docker Compose:

```bash
docker compose up --build
```

Stop containers:

```bash
docker compose down
```

---

# 📡 API Endpoints

## Health Check

### Request

```http
GET /health
```

### Response

```json
{
  "status": "ok",
  "message": "API is healthy and model is loaded."
}
```

---

## Image Prediction

### Request

```http
POST /predict
```

### Supported Formats

* PNG
* JPEG
* JPG

### Example CURL Request

```bash
curl -X POST \
-F "file=@digit.png" \
http://localhost:8000/predict
```

### Example Response

```json
{
  "class_label": "5",
  "probabilities": [
    0.01,
    0.01,
    0.01,
    0.90,
    0.01,
    0.01,
    0.01,
    0.01,
    0.01,
    0.02
  ]
}
```

---

# 🧪 Testing

Run all tests:

```bash
python -m pytest tests/
```

Covered test scenarios:

* Health Endpoint Testing
* Prediction Endpoint Testing
* Invalid File Type Validation
* Missing File Validation

---

# 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow that automatically executes whenever code is pushed to the main branch or a pull request is created.

## Workflow Steps

1. Checkout Repository
2. Setup Python Environment
3. Install Dependencies
4. Execute Unit Tests
5. Build Docker Image
6. Generate Prediction Artifacts
7. Upload Artifacts

## Trigger Events

```yaml
push:
  branches:
    - main

pull_request:
  branches:
    - main
```

---

# 📁 Prediction Examples

Example prediction outputs are stored in:

```text
predictions/
```

Files:

```text
example1.json
example2.json
```

These demonstrate successful API inference responses.

---

# 🌎 Environment Variables

Example configuration:

```env
MODEL_PATH=models/my_classifier_model.h5
LOG_LEVEL=INFO
```

---

# 📈 Future Enhancements

* JWT Authentication
* Kubernetes Deployment
* Docker Registry Integration
* Model Monitoring
* Prometheus Metrics
* Grafana Dashboards
* MLflow Integration
* Multi-Model Serving
* Cloud Deployment (AWS/GCP/Azure)

---

## Screenshots

### Swagger UI

![Swagger UI](screenshots/swagger-ui.png)

### Health Endpoint

![Health Endpoint](screenshots/health-endpoint.png)

### GitHub Actions Success

![GitHub Actions](screenshots/github-actions-success.png)

---

# 🎯 Learning Outcomes

Through this project, the following concepts were implemented:

* Machine Learning Model Serving
* FastAPI Development
* Docker Containerization
* REST API Design
* Automated Testing
* Continuous Integration
* Continuous Deployment
* MLOps Fundamentals
* Environment Configuration Management
* Production-Ready API Development

---

# 📜 License

This project is intended for educational and portfolio purposes.

---

# 👨‍💻 Author

Developed as part of an MLOps-focused Machine Learning Engineering project demonstrating model deployment, containerization, testing, and CI/CD automation.

Pavan Teja