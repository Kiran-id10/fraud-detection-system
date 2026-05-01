import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# CONFIG
# -------------------------------
API_URL = "http://34.131.252.227:8000/predict"

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

# -------------------------------
# STYLE
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.main-title {
    font-size: 42px;
    text-align: center;
    color: #FF4B4B;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown('<p class="main-title">💳 Fraud Detection Dashboard</p>', unsafe_allow_html=True)
st.write("---")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("⚙️ Options")
mode = st.sidebar.radio("Select Mode", ["Single Prediction", "Batch Prediction (CSV)"])

# ------------------------------
# SINGLE PREDICTION
# ------------------------------
if mode == "Single Prediction":

    col1, col2 = st.columns(2)

    with col1:
        step = st.number_input("Step", value=1)
        type = st.selectbox("Transaction Type", ["TRANSFER", "PAYMENT", "CASH_OUT"])
        amount = st.number_input("Amount", value=1000)

    with col2:
        oldbalanceOrg = st.number_input("Old Balance Origin", value=5000)
        newbalanceOrig = st.number_input("New Balance Origin", value=4000)
        oldbalanceDest = st.number_input("Old Balance Dest", value=0)
        newbalanceDest = st.number_input("New Balance Dest", value=1000)

    if st.button("🔍 Predict"):

        data = {
            "step": step,
            "type": type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
        }

        try:
            response = requests.post(API_URL, json=data, timeout=5)

            if response.status_code == 200:
                result = response.json()["prediction"]

                prob = 0.9 if result == 1 else 0.1

                st.write("### 📊 Prediction Result")

                if result == 1:
                    st.error("🚨 Fraud Detected!")
                else:
                    st.success("✅ Safe Transaction")

                st.progress(prob)

            else:
                st.error(f"API Error: {response.text}")

        except Exception as e:
            st.error(f"Connection Error: {e}")

# ------------------------------
# BATCH PREDICTION
# ------------------------------
if mode == "Batch Prediction (CSV)":

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # ✅ Clean data
        df = df.fillna(0)

        st.write("### Uploaded Data")
        st.dataframe(df.head())

        results = []

        for _, row in df.iterrows():
            data = row.to_dict()

            try:
                response = requests.post(API_URL, json=data, timeout=5)

                if response.status_code == 200:
                    pred = response.json().get("prediction", None)
                    results.append(pred)
                else:
                    results.append(None)

            except:
                results.append(None)

        df["prediction"] = results

        st.write("### Predictions")
        st.dataframe(df)

        # ✅ DEBUG (important)
        st.write("Prediction Counts:", df["prediction"].value_counts(dropna=False))

        # ✅ SAFE VISUALIZATION (NO ERROR GUARANTEED)
        valid_df = df.dropna(subset=["prediction"])

        if valid_df.empty:
            st.error("❌ No valid predictions received from API.")
        else:
            fraud_counts = valid_df["prediction"].value_counts()

            fig, ax = plt.subplots()
            fraud_counts.plot(kind="bar", ax=ax)
            ax.set_title("Fraud vs Non-Fraud")
            st.pyplot(fig)

# ------------------------------
# ANALYTICS
# ------------------------------
st.write("---")
st.write("### 📈 Real-Time Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", "6M+")
col2.metric("Fraud Cases", "8K+")
col3.metric("Model", "PySpark ML Pipeline")
