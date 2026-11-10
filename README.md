
# Customer Churn Prediction – MLOps Pipeline

An end-to-end Machine Learning Operations (MLOps) project for customer churn prediction using Scikit-learn, MLflow, FastAPI, Docker, and GitHub Actions CI/CD.

**Repository:** https://github.com/pallu6753/mlops-churn-prediction

---

## 1. Project Overview

Customer churn prediction helps identify customers who may discontinue a product or service. This project demonstrates an end-to-end MLOps workflow for developing, tracking, testing, and serving a machine learning model.

The project integrates machine learning with software engineering practices to support reproducibility, maintainability, and deployment.

## 2. Objectives

- Develop a machine learning model for customer churn prediction.
- Process and prepare customer data.
- Train and evaluate a classification model.
- Track experiments using MLflow.
- Expose prediction functionality through FastAPI.
- Containerize the application using Docker.
- Automate workflows using GitHub Actions.
- Maintain an organized and testable project structure.

## 3. Key Features

- **Machine Learning:** Customer churn prediction using Scikit-learn.
- **Experiment Tracking:** MLflow integration.
- **REST API:** FastAPI-based model serving.
- **Containerization:** Docker support.
- **CI/CD:** GitHub Actions workflow automation.
- **Testing:** Dedicated automated testing directory.
- **Modular Architecture:** Separate API, source code, data, and test directories.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Scikit-learn | Machine learning |
| MLflow | Experiment tracking |
| FastAPI | REST API development |
| Docker | Containerization |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | CI/CD automation |

## 5. System Architecture

```text
          Customer Dataset
                  |
                  v
          Data Preprocessing
                  |
                  v
          Feature Engineering
                  |
                  v
          Model Training
                  |
                  v
          Model Evaluation
                  |
                  v
          Trained ML Model
                  |
          +-------+-------+
          |               |
          v               v
       MLflow         Model Artifact
                          |
                          v
                    FastAPI Service
                          |
                          v
                     Docker Image
                          |
                          v
                   Deployment
```

## 6. Project Structure

```text
mlops-churn-prediction/
│
├── .github/
│   └── workflows/
│
├── api/
│
├── data/
│
├── src/
│
├── tests/
│
├── .dockerignore
│
├── .gitignore
│
├── Dockerfile
│
└── requirements.txt
```

### Directory Description

| Directory / File | Description |
|---|---|
| `.github/workflows/` | GitHub Actions workflow configuration |
| `api/` | API application and prediction-serving code |
| `data/` | Customer dataset files |
| `src/` | Machine learning and supporting source code |
| `tests/` | Automated test cases |
| `.dockerignore` | Files excluded from Docker build context |
| `.gitignore` | Files excluded from Git |
| `Dockerfile` | Docker image configuration |
| `requirements.txt` | Python dependencies |

## 7. Installation and Setup

### Prerequisites

- Python
- Git
- Docker Desktop (for container execution)
- GitHub account

### Step 1: Clone the Repository

```bash
git clone https://github.com/pallu6753/mlops-churn-prediction.git

cd mlops-churn-prediction
```

### Step 2: Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv

.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

## 8. Machine Learning Workflow

The machine learning workflow is organized within the `src/` directory.

The general workflow includes:

1. Loading the customer dataset.
2. Data preprocessing.
3. Feature preparation.
4. Training and testing data separation.
5. Model training using Scikit-learn.
6. Model evaluation.
7. Saving the trained model artifact.
8. Recording experiment information using MLflow.

### Evaluation Metrics

Common classification metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Actual metric values should be obtained from the model evaluation output.

## 9. MLflow Experiment Tracking

MLflow supports tracking machine learning experiments, parameters, metrics, and model artifacts.

Start the MLflow interface if configured:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

## 10. FastAPI – Model Serving

The `api/` directory contains the API implementation.

The API exposes model functionality through HTTP endpoints. The exact endpoint paths and request fields should be checked in the implemented API code.

If the application is exposed through `api/main.py` with a FastAPI object named `app`, a typical local command is:

```bash
uvicorn api.main:app --reload --host 127.0.0.1 --port 8000
```

Swagger documentation, if enabled, is available at:

```text
http://127.0.0.1:8000/docs
```

## 11. Docker – Containerization

Build the Docker image:

```bash
docker build -t mlops-churn-prediction .
```

Run the container using the port configured by the Dockerfile and API:

```bash
docker run --rm -p 8000:8000 mlops-churn-prediction
```

## 12. GitHub Actions – CI/CD

GitHub Actions workflows are maintained in:

```text
.github/workflows/
```

The workflow can automate:

1. Source code checkout.
2. Python environment setup.
3. Dependency installation.
4. Automated testing.
5. Docker image build.
6. Additional deployment steps when configured.

To inspect workflow execution:

1. Open the GitHub repository.
2. Navigate to **Actions**.
3. Select the latest workflow run.
4. Review the job logs and results.

## 13. Testing

The project includes a dedicated `tests/` directory.

If Pytest is configured, run:

```bash
pytest -v
```

Testing should verify the implemented data-processing, model, and API functionality.

## 14. Future Enhancements

- Compare multiple machine learning classification algorithms.
- Improve feature engineering.
- Perform hyperparameter tuning.
- Enhance MLflow model tracking.
- Add API integration tests.
- Implement model monitoring.
- Detect data drift.
- Automate model retraining.
- Improve cloud deployment automation.

## 15. Author

**Pallavi R**

**USN:** 1TJ23DS019

B.E. – Computer Science and Engineering (Data Science)  
T. John Institute of Technology, Bengaluru

**GitHub:** https://github.com/pallu6753

**Project Repository:** https://github.com/pallu6753/mlops-churn-prediction

---

*This project is developed for educational and demonstration purposes. Model predictions should be interpreted in the context of the dataset and actual evaluation results.*
