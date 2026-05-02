# 🚀 Fraud Detection System — Production-Grade ML Platform

<p align="center">
Detect fraudulent financial transactions at scale using <b>PySpark + FastAPI + Streamlit</b>
</p>

<p align="center">
<b>⚡ Real-Time Inference • 🔥 Big Data Processing • 📊 Interactive Analytics</b>
</p>

---

## 🏆 Badges

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![PySpark](https://img.shields.io/badge/PySpark-BigData-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🌐 Live Deployment

| Service | Link |
|--------|------|
| 📊 Streamlit Dashboard | http://34.131.252.227:8501 |
| ⚡ FastAPI Backend | http://34.131.252.227:8000 |
| 📄 API Docs | http://34.131.252.227:8000/docs |
| 🧪 Health Check | http://34.131.252.227:8000/health |

> ⚡ Deployed on a cloud VM with real-time inference capability.

---

## 🔥 Live Demo

<p align="center">
  <img src="screenshots/demo.gif" width="800">
</p>

---

## 💡 Why This Project Matters

Financial fraud detection is a high-impact real-world problem:

- Millions of transactions per day  
- Extremely imbalanced data (~0.13% fraud)  
- Need for real-time decision systems  
- Requirement for scalable ML pipelines  

👉 This project demonstrates a **production-grade ML system** (Data → Model → API → UI)

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

## ⚡ API Endpoints

| Endpoint | Method | Description |
|----------|--------|------------|
| /health | GET | Health check |
| /predict | POST | Single prediction |

---

## 📊 Dashboard Preview

<p align="center">
  <img src="screenshots/frd_dash1.png" width="700"><br><br>
  <img src="screenshots/frd_dash2.png" width="700"><br><br>
  <img src="screenshots/frd_dash3.png" width="700"><br><br>
  <img src="screenshots/frd_dash4.png" width="700"><br><br>
  <img src="screenshots/frd_dash5.png" width="700">
</p>

---

## 📂 Project Structure

```
fraud-detection-system/
│
├── app/                # FastAPI backend
├── streamlit_app/      # Streamlit dashboard
├── model/              # Trained Spark model
├── data/               # Dataset
├── screenshots/        # UI visuals
│
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

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run API
```bash
uvicorn app.app:app --host 0.0.0.0 --port 8000
```

### 4️⃣ Run Dashboard
```bash
streamlit run streamlit_app/app.py
```

---

## 🚀 Future Improvements

- 🔥 Kafka real-time streaming  
- 🔥 Explainable AI (SHAP / LIME)  
- 🔥 Docker + CI/CD pipelines  
- 🔥 Custom domain + HTTPS  

---

## 👨‍💻 Author

**Kiran Kumar**  
Data Science & AI Engineer  

---

## ⭐ Support

If you found this useful:

- ⭐ Star the repository  
- 🔗 Share it  
- 🤝 Connect  

---

<p align="center">
Built with 💡 Big Data + Machine Learning + Engineering
</p>
