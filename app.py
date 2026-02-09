import streamlit as st
import pandas as pd
import pickle

# ======================================
# Load saved ML model
# ======================================
model = pickle.load(open("spending_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🛍️ Customer Spending Prediction App")

st.write("Upload a new customer dataset to predict spending and segment customers.")

# ======================================
# Upload CSV file
# ======================================
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    
    data = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded Dataset")
    st.write(data)

    # ======================================
    # Predict spending
    # ======================================
    scaled_data = scaler.transform(data)
    predictions = model.predict(scaled_data)
    
    data["Predicted Spending"] = predictions

    # ======================================
    # Segment customers
    # ======================================
    def segment_customer(amount):
        if amount > 600:
            return "VIP"
        elif amount > 500:
            return "Premium"
        elif amount > 400:
            return "Regular"
        else:
            return "Low Value"

    data["Segment"] = data["Predicted Spending"].apply(segment_customer)

    st.subheader("💰 Prediction Results")
    st.write(data)

    # ======================================
    # Download results
    # ======================================
    csv = data.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        "📥 Download Predictions",
        csv,
        "predicted_customers.csv",
        "text/csv"
    )
