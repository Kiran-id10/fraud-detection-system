# 🏗️ Fraud Detection System Architecture

This document explains the end-to-end architecture of the fraud detection system, covering data flow, components, and how each layer interacts.

---

## 📌 Overview

The system is designed as a **production-style machine learning pipeline**:

👉 Data → Feature Engineering → ML Model → API → Dashboard → User

It supports:
- Real-time fraud prediction
- Scalable data processing using PySpark
- Interactive visualization via Streamlit

---

## 🔄 Architecture Flow

```mermaid
flowchart LR
    A[User] --> B[Streamlit Dashboard]
    B --> C[FastAPI API]
    C --> D[Feature Engineering Layer]
    D --> E[PySpark ML Pipeline]
    E --> F[Prediction Engine]
    F --> G[Results & Insights]
    G --> B
