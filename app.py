import streamlit as st
import numpy as np
import pickle
import os

MODEL_FILENAME = "model.pkl"

if not os.path.exists(MODEL_FILENAME):
    st.error(f"Model file '{MODEL_FILENAME}' not found. Please place it in the same folder as this script.")
else:
    try:
        with open(MODEL_FILENAME, "rb") as f:
            model = pickle.load(f)
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        model = None

    if model:
        st.title("Credit Card Default Prediction")
        st.write("Enter customer details to predict whether they will default next month")

        # User Inputs
        LIMIT_BAL = st.number_input("Credit Limit Balance", min_value=0)
        SEX = st.selectbox("Sex", [1, 2])
        EDUCATION = st.selectbox("Education Level", [1, 2, 3, 4])
        MARRIAGE = st.selectbox("Marriage Status", [1, 2, 3])
        AGE = st.number_input("Age", min_value=18, max_value=100)

        PAY_0 = st.number_input("Repayment Status Sep")
        PAY_2 = st.number_input("Repayment Status Aug")
        PAY_3 = st.number_input("Repayment Status Jul")
        PAY_4 = st.number_input("Repayment Status Jun")
        PAY_5 = st.number_input("Repayment Status May")
        PAY_6 = st.number_input("Repayment Status Apr")

        BILL_AMT1 = st.number_input("Bill Amount Sep")
        BILL_AMT2 = st.number_input("Bill Amount Aug")
        BILL_AMT3 = st.number_input("Bill Amount Jul")
        BILL_AMT4 = st.number_input("Bill Amount Jun")
        BILL_AMT5 = st.number_input("Bill Amount May")
        BILL_AMT6 = st.number_input("Bill Amount Apr")

        PAY_AMT1 = st.number_input("Payment Amount Sep")
        PAY_AMT2 = st.number_input("Payment Amount Aug")
        PAY_AMT3 = st.number_input("Payment Amount Jul")
        PAY_AMT4 = st.number_input("Payment Amount Jun")
        PAY_AMT5 = st.number_input("Payment Amount May")
        PAY_AMT6 = st.number_input("Payment Amount Apr")

        # Prediction Button
        if st.button("Predict Default"):
            input_data = np.array([[LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE,
                                    PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                                    BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
                                    PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]])

            try:
                prediction = model.predict(input_data)
                if prediction[0] == 1:
                    st.error("Customer will DEFAULT payment next month")
                else:
                    st.success("Customer will NOT default payment")
            except Exception as e:
                st.error(f"Prediction failed: {e}")
