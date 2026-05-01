from fastapi import FastAPI, HTTPException
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel
from pyspark.sql.functions import log1p, when, col

# -------------------------------
# INIT
# -------------------------------
spark = SparkSession.builder.appName("fraud-api").getOrCreate()
model = PipelineModel.load("/home/kirankumarsrkiru/fraud_modelss")

app = FastAPI(title="Fraud Detection API")

# -------------------------------
# FEATURE ENGINEERING
# -------------------------------
def feature_engineering(df):
    df = df.withColumn("log_amounts", log1p(col("amount")))
    df = df.withColumn("amount_outliers", when(col("amount") > 200000, 1).otherwise(0))
    df = df.withColumn("oldbalanceOrg_outliers", when(col("oldbalanceOrg") > 200000, 1).otherwise(0))
    df = df.withColumn("newbalanceOrig_outliers", when(col("newbalanceOrig") > 200000, 1).otherwise(0))
    df = df.withColumn("oldbalanceDest_outliers", when(col("oldbalanceDest") > 200000, 1).otherwise(0))
    df = df.withColumn("newbalanceDest_outliers", when(col("newbalanceDest") > 200000, 1).otherwise(0))
    df = df.withColumn("balance_diff_origs", col("oldbalanceOrg") - col("newbalanceOrig"))
    df = df.withColumn("balance_diff_dests", col("newbalanceDest") - col("oldbalanceDest"))
    return df

# -------------------------------
# ROUTES
# -------------------------------
@app.get("/")
def home():
    return {"message": "Fraud API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict):
    try:
        df = spark.createDataFrame([data])
        df = feature_engineering(df)

        result = model.transform(df)
        rows = result.select("prediction").collect()

        # ✅ SAFETY (prevents index error)
        if not rows:
            raise Exception("Empty prediction result")

        prediction = rows[0][0]

        return {
            "prediction": int(prediction),
            "status": "Fraud" if prediction == 1 else "Safe"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
