# 🚀 Fraud Detection System — Production-Grade ML Platform

<p align="center">
  <b>Detect fraudulent financial transactions at scale using PySpark + FastAPI + Streamlit + Docker</b>
</p>

<p align="center">
  ⚡ Real-Time Inference • 🔥 Big Data Processing • 📊 Interactive Analytics
</p>

<p align="center">
  🚨 Achieves <b>0.993 ROC-AUC</b> on 6.3M+ transactions with real-time fraud detection
</p>

---

## 🏆 Badges

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/PySpark-BigData-orange?logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-HighPerformance-green?logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Interactive-red?logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Model-LogisticRegression-yellow"/>
  <img src="https://img.shields.io/badge/Status-Production--Ready-success"/>
</p>

---

## 🌐 Live Deployment

| Service | Link |
|--------|------|
| 📊 Streamlit Dashboard | http://34.131.252.227:8501 |
| ⚡ FastAPI Backend | http://34.131.252.227:8000 |
| 📄 API Docs (Swagger) | http://34.131.252.227:8000/docs |
| 🧪 Health Check | http://34.131.252.227:8000/health |

> ⚡ Deployed on a cloud VM with real-time inference capability.

---

## 🔥 Live Demo

<p align="center">
  <img src="screenshots/frd_demo.gif" width="900">
</p>

---

## 🏅 Key Highlights

- ⚡ Handles **6M+ transactions** using PySpark  
- 🎯 Achieves **0.993 ROC-AUC**  
- 🚀 Real-time fraud detection via FastAPI  
- 📊 Interactive dashboard using Streamlit  
- 🔍 Advanced feature engineering + imbalance handling  
- 🐳 Fully Dockerized PySpark deployment  
- ☁️ Cloud-ready production architecture  

---

## 💡 Why This Project Matters

Financial fraud detection is a high-impact real-world problem:

- Millions of transactions per day  
- Highly imbalanced dataset (~0.13% fraud)  
- Requires real-time decisions  
- Needs scalable ML infrastructure  

👉 This project demonstrates a **complete production ML system**  
(Data → Model → API → UI → Deployment → Docker)

---

## 🚀 What This System Does

✔ Detects fraudulent transactions in real-time  
✔ Processes millions of records using PySpark  
✔ Provides instant predictions via API  
✔ Visualizes fraud insights through dashboard  
✔ Supports scalable containerized deployment  

---

## 📊 Dataset Overview

- 📦 Total Records: **6,362,620**  
- 🎯 Fraud Cases: **8,213 (~0.13%)**  
- ⚠️ Highly Imbalanced Dataset  

---

## ⚙️ Tech Stack

| Layer | Technology |
|------|-----------|
| Big Data | PySpark |
| ML Pipeline | Spark ML |
| Backend | FastAPI |
| Frontend | Streamlit |
| Visualization | Plotly |
| Containerization | Docker |
| Deployment | Cloud VM |

---

## 🧠 ML Pipeline Overview

### ✔ Data Processing
- Schema inference  
- Null & duplicate handling  
- Statistical profiling  

### ✔ Feature Engineering
- Log transformations  
- IQR-based outlier detection  
- Balance difference features  
- Transaction behavior signals  

### ✔ Handling Imbalance
- Undersampling  
- Class-weighted learning  

### ✔ Model Pipeline
- StringIndexer  
- OneHotEncoder  
- VectorAssembler  
- StandardScaler  
- Logistic Regression  

---

## 📈 Model Performance

| Metric | Score |
|--------|------|
| ROC-AUC | **0.9931** |
| Precision | **0.9998** |
| Recall | **0.9378** |

👉 High precision + strong recall → **Reliable fraud detection system**

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[User] --> B[Streamlit Dashboard]
    B --> C[FastAPI API]
    C --> D[Feature Engineering Layer]
    D --> E[PySpark ML Pipeline]
    E --> F[Prediction Engine]
    F --> G[Results & Insights]
    G --> B
```

---

## 🐳 Dockerized Architecture

```text
Docker Container
│
├── FastAPI Backend
├── PySpark Runtime
├── Spark ML Pipeline
├── Java Runtime (JDK)
├── Feature Engineering Layer
└── Prediction Engine
```

---

## ⚡ API Endpoints

| Endpoint | Method | Description |
|----------|--------|------------|
| /health | GET | Health check |
| /predict | POST | Single prediction |

---

## 📊 Dashboard & API Preview

### 🎯 Streamlit Dashboard

<p align="center">
  <img src="screenshots/frd_dash1.png" width="700"><br><br>
  <img src="screenshots/frd_dash2.png" width="700"><br><br>
  <img src="screenshots/frd_dash3.png" width="700"><br><br>
  <img src="screenshots/frd_dash4.png" width="700"><br><br>
  <img src="screenshots/frd_dash5.png" width="700">
</p>

---

### ⚡ FastAPI Swagger UI

<p align="center">
  <img src="screenshots/frd_dash6.png" width="700"><br><br>
  <img src="screenshots/frd_dash7.png" width="700"><br><br>
  <img src="screenshots/frd_dash8.png" width="700"><br><br>
  <img src="screenshots/frd_dash9.png" width="700">
</p>

---

## 🐳 Dockerized Deployment

This project has been fully containerized using Docker for reproducible and production-ready deployment.

---

## 🚀 Why Docker?

✔ Ensures consistent environment across systems

✔ Eliminates dependency conflicts

✔ Simplifies deployment workflow

✔ Supports scalable cloud-native deployment

✔ Enables isolated execution environment

✔ Improves portability across machines and servers

✔ Supports Spark + Java containerized execution

---

## 📦 Dockerfile Highlights

✔ Lightweight Python 3.11 slim image

✔ Java runtime installation for PySpark

✔ Optimized build context using `.dockerignore`

✔ Reduced unnecessary file transfer

✔ Spark ML model packaged inside container

✔ Production-ready FastAPI startup command

---

## 📂 Docker Files Added

```text
Dockerfile
.dockerignore
```

---

## ⚙️ Build Docker Image

```bash
docker build -t fraud-api .
```

---

## ▶️ Run Docker Container

```bash
docker run -p 8000:8000 fraud-api
```

---

## 🌐 Access Dockerized API

### FastAPI Swagger Docs

```text
http://localhost:8000/docs
```

---

## 🧠 Docker Optimization Techniques Used

✔ `.dockerignore` to exclude datasets and Spark cache

✔ Optimized Docker build context

✔ Layer caching for faster rebuilds

✔ Separate COPY instructions for efficient builds

✔ Java + Spark runtime optimization

✔ Docker storage moved to D drive for heavy Spark workloads

---

## 📊 Docker Benefits for Big Data ML Systems

- Reproducible Spark environments
- Portable ML deployment
- Easier cloud deployment
- Simplified infrastructure setup
- Better scalability
- Production-grade deployment workflow

---

## 🔥 Production Engineering Concepts Demonstrated

✔ PySpark Big Data Processing

✔ Spark ML Pipeline Deployment

✔ FastAPI Production Serving

✔ Docker Containerization

✔ Java Runtime Integration

✔ Cloud Deployment

✔ Build Context Optimization

✔ Containerized ML Inference

✔ Real-time Prediction APIs

---

## 📂 Project Structure

```bash
fraud-detection-system/
│
├── app/                # FastAPI backend
├── streamlit_app/      # Streamlit dashboard
├── model/              # Trained Spark model
│   └── fraud_modelss/
│
├── data/               # Dataset
├── screenshots/        # UI + GIF + API images
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── architecture.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/fraud-detection-system.git

cd fraud-detection-system
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run API

```bash
uvicorn app.app:app --host 0.0.0.0 --port 8000
```

---

### 4️⃣ Run Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

## 🐳 Run Using Docker

```bash
docker build -t fraud-api .

docker run -p 8000:8000 fraud-api
```

---

## 📌 Key Insights

- Fraud transactions often involve high amounts with zero destination balance  
- Balance inconsistencies are strong fraud indicators  
- Transfer and Cash-out operations carry higher risk  

---

## 🎯 Use Case

This system can be used by:

- Banks for real-time fraud detection  
- Fintech platforms for transaction monitoring  
- Payment gateways for risk scoring  

---

## ⚠️ Limitations

- Model trained on historical data (may not capture new fraud patterns)  
- No real-time streaming integration yet  
- Requires further tuning for production-scale latency  

---

## 🚀 Future Improvements

- 🔥 Real-time streaming with Kafka  
- 🔥 Explainable AI (SHAP / LIME)  
- 🔥 CI/CD pipeline integration  
- 🔥 Kubernetes deployment  
- 🔥 Cloud deployment with custom domain  
- 🔥 Docker Compose multi-container architecture  

---

## 👨‍💻 Author

**Kiran Kumar S R**  
Data Science & AI Engineer  

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository  
- 🔗 Share it  
- 🤝 Connect  

---

<p align="center">
Built with 💡 Big Data + Machine Learning + Engineering + Docker
</p>
