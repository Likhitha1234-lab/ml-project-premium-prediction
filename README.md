# 🏥 Health Insurance Cost Predictor

A Machine Learning-powered web application that predicts health insurance costs based on customer demographics, health conditions, lifestyle habits, and financial information.

---

## 📌 Project Overview

Health insurance premiums are influenced by several factors such as age, medical history, BMI, smoking habits, income, and insurance plans. This project leverages Machine Learning to estimate insurance costs accurately and provide instant predictions through an interactive Streamlit application.

The application helps insurance providers and customers understand how different factors impact premium pricing.

---

## 🚀 Features

* Interactive Streamlit Web Application
* Real-Time Insurance Cost Prediction
* Personalized Premium Estimation
* Health & Financial Risk Assessment
* User-Friendly Interface
* Machine Learning-Based Prediction System

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Joblib

---

## 📊 Input Features

### Personal Details

* Age
* Gender
* Marital Status
* Number of Dependents

### Health Details

* BMI Category
* Smoking Status
* Medical History
* Genetic Risk

### Financial Details

* Annual Income
* Insurance Plan
* Employment Status
* Region

---

## 📷 Application Screenshots

### 🏠 Home Page

![Home Page](images/Screenshot%202026-06-20%20162708.png)

---

### ❤️ Health Details Section

![Health Details](images/Screenshot%202026-06-20%20164037.png)

---

### 💰 Financial Details Section

![Financial Details](images/Screenshot%202026-06-20%20164121.png)

---

### 🎯 Prediction Result

![Prediction Result](images/Screenshot%202026-06-20%20164140.png)

---

## 🤖 Modeling Approach & Performance

Instead of using a single model for all customers, the dataset was segmented based on age to improve prediction accuracy and better capture different risk patterns.

### 👦 Young Customers (Age ≤ 25)

For younger customers, **Genetic Risk** was found to be an important predictor of insurance costs.

Models Evaluated:

* Linear Regression
* Ridge Regression

Results:

| Model             | Test R² Score |
| ----------------- | ------------: |
| Linear Regression |         0.989 |
| Ridge Regression  |         0.989 |

Key Findings:

* Adding **Genetic Risk** significantly improved model performance.
* Linear and Ridge Regression performed best due to the strong linear relationship between features and insurance costs in this age group.

---

### 👨 Adult Customers (Age > 25)

For older customers, factors such as lifestyle, medical history, income, and insurance plan had a greater influence on premium costs.

Models Evaluated:

* Linear Regression
* Ridge Regression
* XGBoost Regressor

Results:

| Model             | Test R² Score |
| ----------------- | ------------: |
| Linear Regression |         0.925 |
| Ridge Regression  |         0.925 |
| XGBoost Regressor |         0.998 |

Key Findings:

* Genetic Risk did not provide meaningful improvement in this segment.
* XGBoost captured complex non-linear relationships and delivered the highest prediction performance.

---

### 💡 Key Insight

A segmented modeling strategy produced better results than using a single model for all customers.

* Age ≤ 25 → Linear/Ridge Regression with Genetic Risk
* Age > 25 → XGBoost without Genetic Risk

This approach improved prediction accuracy while maintaining model interpretability for younger customers and leveraging advanced machine learning techniques for older customer segments.

---

## 🔄 Machine Learning Workflow

1. Data Collection & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Data Cleaning
5. Model Training
6. Model Evaluation
7. Hyperparameter Optimization
8. Streamlit Application Development

---

## 📂 Project Structure

```text
ml-project-premium-prediction/
│
├── artifacts/
│   ├── model_rest.joblib
│   ├── model_young.joblib
│   ├── scaler_rest.joblib
│   └── scaler_young.joblib
│
├── images/
│
├── main.py
├── prediction_helper.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ▶️ Installation & Usage

```bash
pip install -r requirements.txt
streamlit run main.py
```

---

## 🎯 Business Impact

This solution enables faster and more consistent insurance premium estimation by leveraging Machine Learning, reducing manual effort and improving decision-making for insurance providers.

---

## 👩‍💻 Author

**Likhitha N**

Aspiring AI & Data Scientist | Machine Learning | Python | SQL | Streamlit
