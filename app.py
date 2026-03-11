import streamlit as st
import numpy as np
import joblib

# page config
st.set_page_config(
    page_title="Credit Default Predictor",
    page_icon="💳",
    layout="wide"
)

# load model
model = joblib.load("model1.pkl")

st.title("💳 Credit Card Default Prediction")

st.write("Enter customer financial details to predict default risk.")

col1, col2, col3 = st.columns(3)

with col1:
    LIMIT_BAL = st.number_input("Limit Balance", 0)
    SEX = st.selectbox("Sex", [1,2])
    EDUCATION = st.selectbox("Education", [1,2,3,4])
    MARRIAGE = st.selectbox("Marriage", [1,2,3])
    AGE = st.number_input("Age", 18, 100)

with col2:
    PAY_0 = st.number_input("Pay 0")
    PAY_2 = st.number_input("Pay 2")
    PAY_3 = st.number_input("Pay 3")
    PAY_4 = st.number_input("Pay 4")
    PAY_5 = st.number_input("Pay 5")
    PAY_6 = st.number_input("Pay 6")

with col3:
    BILL_AMT1 = st.number_input("Bill Amount 1")
    BILL_AMT2 = st.number_input("Bill Amount 2")
    BILL_AMT3 = st.number_input("Bill Amount 3")
    BILL_AMT4 = st.number_input("Bill Amount 4")
    BILL_AMT5 = st.number_input("Bill Amount 5")
    BILL_AMT6 = st.number_input("Bill Amount 6")

PAY_AMT1 = st.number_input("Pay Amount 1")
PAY_AMT2 = st.number_input("Pay Amount 2")
PAY_AMT3 = st.number_input("Pay Amount 3")
PAY_AMT4 = st.number_input("Pay Amount 4")
PAY_AMT5 = st.number_input("Pay Amount 5")
PAY_AMT6 = st.number_input("Pay Amount 6")

# prediction button
if st.button("Predict Default Risk"):

    features = np.array([[
        LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE,
        PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
        BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
        PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ High Risk: Customer may default next month")
    else:
        st.success("✅ Low Risk: Customer likely to repay")
