# 🚀 ML Prediction API & CI/CD Pipeline

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.121.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19.0-FF6F00.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg?style=flat&logo=docker)](https://www.docker.com/)
[![CI/CD](https://github.com/hp/ml-predictionAPI-ci-cd/actions/workflows/main.yml/badge.svg)](https://github.com/hp/ml-predictionAPI-ci-cd/actions)

A production-ready Image Classification REST API built with FastAPI and TensorFlow. This project demonstrates end-to-end MLOps practices including model serving, robust error handling, containerization, and automated CI/CD workflows. The current implementation predicts handwritten digits (0-9) using a pre-trained convolutional neural network.

---

## 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Architecture Overview](#-architecture-overview)
- [Technology Stack](#-technology-stack)
- [Folder Structure](#-folder-structure)
- [Installation](#-installation)
- [Running Locally](#-running-locally)
- [Docker Usage](#-docker-usage)
- [API Endpoints](#-api-endpoints)
- [CI/CD Workflow](#-cicd-workflow)
- [Testing Instructions](#-testing-instructions)
- [Environment Variables](#-environment-variables)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## 🌟 Project Overview

The ML Prediction API provides a scalable and robust web service for evaluating image classification models. Built entirely in Python, it exposes a primary endpoint that accepts image uploads, performs rigorous preprocessing (converting to 28x28 grayscale tensors), and feeds the data into a TensorFlow model to generate real-time predictions with associated probabilities.

---

## ✨ Key Features

- **High-Performance API:** Asynchronous request handling using FastAPI.
- **Robust Model Serving:** Lazy-loading of TensorFlow models to optimize memory and minimize startup time.
- **Strict Validation:** Real-time input validation checking file size (max 5MB) and MIME types (PNG/JPEG only).
- **Containerization:** Multi-stage Docker builds to ensure minimal image sizes and secure runtime environments.
- **Automated CI/CD:** Complete GitHub Actions pipeline for continuous integration, automated testing, and container image builds.
- **Comprehensive Testing:** Mock-driven unit testing of all API layers utilizing `pytest`.

---

## 🏗 Architecture Overview

The system architecture follows a decoupled approach for serving Machine Learning models:

1. **Client Request:** The user sends a multipart/form-data POST request containing an image to the `/predict` endpoint.
2. **API Layer (`src/main.py`):** FastAPI handles routing, parameter validation, size constraints, and error formatting.
3. **ML Layer (`src/model.py`):** 
   - **Preprocessing:** The image bytes are ingested by Pillow, converted to grayscale, resized to 28x28, normalized (0.0 - 1.0), and reshaped into a tensor `(1, 28, 28, 1)`.
   - **Inference:** The tensor is passed into the pre-loaded Keras/TensorFlow model (`my_classifier_model.h5`).
4. **Response:** The index of the highest probability is mapped to the corresponding class label ("0"-"9"), and returned alongside the full probability distribution array.

---

## 🛠 Technology Stack

- **Core:** Python 3.11
- **Web Framework:** FastAPI, Uvicorn, Python-Multipart
- **Machine Learning:** TensorFlow 2.19.0, NumPy, Pandas, Pillow
- **Testing:** Pytest, HTTPX
- **DevOps:** Docker, Docker Compose, GitHub Actions

---

## 📂 Folder Structure

```text
.
├── .github/
│   └── workflows/
│       └── main.yml           # GitHub Actions CI/CD pipeline configuration
├── models/
│   └── my_classifier_model.h5 # Pre-trained TensorFlow/Keras model
├── src/
│   ├── __init__.py
│   ├── main.py                # FastAPI application and endpoint definitions
│   └── model.py               # ML inference and image preprocessing logic
├── tests/
│   └── test_api.py            # Unit tests for the endpoints and core logic
├── .env.example               # Template for environment variables
├── docker-compose.yml         # Docker Compose services definition
├── Dockerfile                 # Multi-stage Docker build instructions
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation (this file)
```

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ml-predictionAPI-ci-cd.git
   cd ml-predictionAPI-ci-cd
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure Environment:**
   ```bash
   cp .env.example .env
   # Edit .env to suit your environment configuration
   ```

---

## 🚀 Running Locally

Once installed, start the API using Uvicorn:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

The application will be accessible at:
- **API Base:** `http://localhost:8000`
- **Interactive Swagger UI:** `http://localhost:8000/docs`
- **ReDoc Documentation:** `http://localhost:8000/redoc`

---

## 🐳 Docker Usage

To ensure a consistent environment, you can run the API entirely inside Docker.

### Using Docker Compose (Recommended)
This will build the image and mount the local `models` directory:

```bash
docker-compose up --build -d
```

### Using Docker CLI
Build the multi-stage image:
```bash
docker build -t ml-prediction-api:latest .
```

Run the container:
```bash
docker run -d -p 8000:8000 \
  -v $(pwd)/models:/app/models \
  -e MODEL_PATH=/app/models/my_classifier_model.h5 \
  --name ml_api ml-prediction-api:latest
```

---

## 🌐 API Endpoints

### 1. Health Check
Checks if the API is responsive and the ML model is successfully loaded in memory.

**Request:**
```http
GET /health
```

**Response (200 OK):**
```json
{
  "status": "ok",
  "message": "API is healthy and model is loaded."
}
```

### 2. Predict Image
Upload an image for the model to classify.

**Request:**
```http
POST /predict
Content-Type: multipart/form-data
```
| Form Data Field | Type | Description |
| --- | --- | --- |
| `file` | `File` | The image file (PNG/JPEG) to predict. Max size 5MB. |

**Example using cURL:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test_image.png;type=image/png"
```

**Response (200 OK):**
```json
{
  "class_label": "5",
  "probabilities": [
    0.012, 0.001, 0.003, 0.054, 0.011, 0.892, 0.015, 0.004, 0.006, 0.002
  ]
}
```

**Error Responses:**
- `400 Bad Request`: When the file is not PNG/JPEG, or the file size exceeds 5MB.
- `422 Unprocessable Entity`: When the image format is corrupted or missing.
- `500 Internal Server Error`: For unexpected preprocessing or inference failures.

---

## 🔄 CI/CD Workflow

This repository utilizes **GitHub Actions** (`.github/workflows/main.yml`) for continuous integration and delivery. 

The pipeline runs automatically on `push` or `pull_request` to the `main` branch and executes the following steps:
1. **Source Checkout & Environment Setup:** Pulls code and configures Python 3.11.
2. **Dependency Installation:** Upgrades pip and installs packages from `requirements.txt`.
3. **Automated Testing:** Executes the `pytest` suite against the API.
4. **Container Build:** Builds the Docker image locally to verify multi-stage configuration.
5. **Artifact Generation:** Simulates model output predictions and uploads them as workflow artifacts.

---

## 🧪 Testing Instructions

The project uses `pytest` for unit testing with mocked ML inferences to ensure fast and isolated API testing.

To run the test suite:
```bash
python -m pytest tests/ -v
```

This will run all tests, including:
- Checking the `/health` endpoint.
- Validating the `/predict` endpoint with mock valid images.
- Asserting correct HTTP codes for invalid file types and missing payloads.

---

## ⚙️ Environment Variables

Configuration is managed via environment variables. Refer to `.env.example`.

| Variable | Default Value | Description |
| --- | --- | --- |
| `MODEL_PATH` | `models/my_classifier_model.h5` | Absolute or relative path to the pre-trained TensorFlow model. |
| `LOG_LEVEL` | `INFO` | Standard Python logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`). |

---

## 🔮 Future Improvements

- **Model Registry Integration:** Integrate MLflow or Weights & Biases for versioning and tracking model performance.
- **Monitoring & Metrics:** Add Prometheus metrics to track inference latency and prediction distributions.
- **Batch Predictions:** Introduce an endpoint to handle bulk/batch image predictions asynchronously via Celery or Kafka.
- **GPU Acceleration:** Enhance the Docker image to utilize NVIDIA runtime (`nvidia-docker`) for high-throughput GPU inference.
- **Code Quality Checks:** Add `flake8`, `black`, and `mypy` steps to the GitHub Actions pipeline.
