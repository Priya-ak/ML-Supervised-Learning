# 🛍️ Customer Spending Prediction & Segmentation App

A Machine Learning + Streamlit web app that predicts **customer yearly spending** and automatically segments customers into business-friendly categories.

This project demonstrates a complete **ML deployment workflow**:  
Model Training → Model Saving → Web App Deployment → User Predictions

---

## 🚀 App Features

✔️ Upload a CSV dataset  
✔️ Predict customer yearly spending  
✔️ Automatically segment customers  
✔️ Download prediction results  

---

## 🎯 Customer Segmentation Logic

| Predicted Spending | Segment |
|--------------------|---------|
| > 600 | 💎 VIP |
| 500 – 600 | 🌟 Premium |
| 400 – 500 | 🙂 Regular |
| < 400 | 🔹 Low Value |

---

## 🧠 Model Details

The model was trained using the **Ecommerce Customers Dataset** with the following features:

- Avg. Session Length  
- Time on App  
- Time on Website  
- Length of Membership  

The trained model and scaler are saved using **Pickle** and loaded directly in the Streamlit app.

---

## 📂 Project Structure

```
Customer-Spending-Prediction/
│
├── app.py
├── spending_model.pkl
├── scaler.pkl
├── run.bat
├── sample_input.csv
├── requirement.txt
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/priya-ak/ML-Supervised-Learning
cd ML-Supervised-Learning
```

### 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser 🎉

---

## 📥 Input CSV Format

Upload a CSV file with these columns:

```
Avg. Session Length, Time on App, Time on Website, Length of Membership
```

You can use the provided **sample_input.csv** to test the app.

---

## 🧰 Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 💡 Skills Demonstrated

- Machine Learning Deployment  
- Model Serialization (Pickle)  
- Streamlit App Development  
- End-to-End ML Project

---

## 👩‍💻 Author

**Priyadharshini**  
GitHub: https://github.com/priya-ak

---

⭐ If you like this project, please star the repository!
