# 🚀 Fraud Detection System — Production-Grade ML Platform

<p align="center">
Detect fraudulent financial transactions in real-time using a scalable ML system built with FastAPI, PySpark, and Streamlit.
</p>

<p align="center">
<b>⚡ Real-Time Inference • 🔥 Scalable ML • 📊 Interactive Dashboard</b>
</p>

---

## 🏆 Badges

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![PySpark](https://img.shields.io/badge/PySpark-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🔥 Live Demo (Product Experience)

🎥 Real-time fraud detection + batch analytics dashboard in action

<p align="center">
  <img src="screenshots/demo.gif" width="800">
</p>

---

## 💡 Why This Project Matters

Financial fraud costs billions every year — detecting it in real-time at scale is a real-world engineering challenge.

This project demonstrates how to:

- ⚡ Build real-time fraud detection systems  
- 🔥 Scale ML pipelines using PySpark  
- 🚀 Deploy models via production-ready APIs  
- 📊 Create interactive dashboards for decision-making  

👉 This is not just a model — it's a complete production-style ML system

---

## ⚙️ Tech Stack

| Layer        | Technology            |
|-------------|---------------------|
| Backend     | FastAPI             |
| ML Engine   | PySpark Pipeline    |
| Frontend    | Streamlit           |
| Visualization | Plotly / Matplotlib |
| Deployment  | VM / GCP Ready      |

---

## ✨ Key Features

### ⚡ Real-Time Prediction
- Instant fraud detection via API  
- Low latency inference  

### 📊 Interactive Dashboard
- Single transaction prediction  
- CSV batch processing  
- Visual fraud distribution  

### 🧠 Feature Engineering
- Log transformation of transaction amount  
- Outlier detection  
- Balance difference analysis  
- Behavioral signals  

### 🔥 Scalable ML Pipeline
- PySpark PipelineModel  
- Handles large-scale transaction data  

---

## 🏗️ System Architecture

```mermaid
flowchart LR
    A[User] --> B[Streamlit Dashboard]
    B --> C[FastAPI Server]
    C --> D[Feature Engineering]
    D --> E[PySpark ML Pipeline]
    E --> F[Prediction Output]
    F --> B
```

---

## 📊 Model Performance

| Metric    | Score  |
|----------|--------|
| Accuracy | 99%+   |
| Precision | High  |
| Recall   | High   |
| ROC-AUC  | Strong |

⚠️ Replace these with your real evaluation metrics for maximum impact

---

## 📸 Screenshots

<p align="center">
  <img src="screenshots/frd_dash9.png" width="700"><br><br>
  <img src="screenshots/frd_dash7.png" width="700"><br><br>
  <img src="screenshots/frd_dash6.png" width="700"><br><br>
  <img src="screenshots/frd_dash3.png" width="700"><br><br>
  <img src="screenshots/frd_dash5.png" width="700"><br><br>
  <img src="screenshots/frd_dash2.png" width="700">
</p>

---

## 📂 Project Structure

```
fraud-detection-system/
│
├── app/                    # FastAPI backend
│   └── app.py
│
├── streamlit_app/         # Streamlit frontend
│   └── app.py
│
├── model/                 # Trained Spark model
│   └── fraud_modelss/
│
├── data/
├── screenshots/
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

### 3️⃣ Run FastAPI Server
```bash
uvicorn app.app:app --host 0.0.0.0 --port 8000
```

### 4️⃣ Run Streamlit Dashboard
```bash
streamlit run streamlit_app/app.py
```

---

## ⚡ API Endpoints

| Endpoint   | Method | Description          |
|-----------|--------|----------------------|
| /health   | GET    | Health check         |
| /predict  | POST   | Single prediction    |

---

## 📈 Features Used

- Transaction Amount  
- Transaction Type  
- Balance Differences  
- Destination Account Behavior  
- Outlier Indicators  

---

## 🚀 Future Improvements

- 🔥 Real-time streaming with Kafka  
- 🔥 Explainable AI (feature contribution)  
- 🔥 Docker + CI/CD pipeline  
- 🔥 Cloud deployment with custom domain  
- 🔥 Risk scoring system  

---

## 👨‍💻 Author

**Kiran Kumar**  
Data Science & AI Engineer  

---

## ⭐ Support

If you found this useful:

👉 Star ⭐ the repo  
👉 Share with others  
👉 Connect for collaboration  

---

<p align="center">
Built with 💡 Data + Engineering Precision
</p>
