import streamlit as st
from prediction_helper import predict

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #dbeafe 0%,
        #bfdbfe 50%,
        #93c5fd 100%
    );
}

/* Transparent Header */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Section Headings */
.section-heading {
    color: white !important;
    background: #1e3a8a;
    border-left: 6px solid #0f172a;
    padding: 12px 18px;
    border-radius: 12px;
    margin-bottom: 18px;
    font-weight: 700;
}

/* Labels */
[data-testid="stWidgetLabel"] {
    color: #1e3a8a !important;
    font-weight: 700 !important;
}

/* Number & Text Inputs */
.stNumberInput input,
.stTextInput input {
    background-color: white !important;
    color: #0f172a !important;
    font-weight: 600;
    border-radius: 8px;
    border: 1px solid #cbd5e1 !important;
}

/* Selectboxes */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: white !important;
    color: #0f172a !important;
    border-radius: 8px;
    border: 1px solid #cbd5e1 !important;
}

/* Dropdown menu */
div[role="listbox"] {
    background-color: white !important;
    color: #0f172a !important;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    border: none;
    background: #1e3a8a;
    color: white;
}

.stButton > button:hover {
    background: #2563eb;
    color: white;
}

/* Prediction Card */
.prediction-box {
    background: linear-gradient(
        135deg,
        #2563eb,
        #1e3a8a
    );
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
    box-shadow: 0px 8px 25px rgba(37,99,235,0.3);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<h1 style='text-align:center;color:#1e3a8a;font-size:55px;'>
🏥 Health Insurance Cost Predictor
</h1>

<p style='text-align:center;color:#1e40af;font-size:20px;'>
Predict your insurance premium using Machine Learning
</p>
""", unsafe_allow_html=True)

# =========================
# OPTIONS
# =========================
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease',
        'Diabetes',
        'High blood pressure',
        'Diabetes & High blood pressure',
        'Thyroid',
        'Heart disease',
        'High blood pressure & Heart disease',
        'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# =========================
# PERSONAL DETAILS
# =========================
st.markdown(
    "<h3 class='section-heading'>👤 Personal Details</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        step=1
    )

with col2:
    gender = st.selectbox(
        "Gender",
        categorical_options['Gender']
    )

marital_status = st.selectbox(
    "Marital Status",
    categorical_options['Marital Status']
)

number_of_dependants = st.number_input(
    "Number of Dependants",
    min_value=0,
    max_value=20,
    step=1
)

st.divider()

# =========================
# HEALTH DETAILS
# =========================
st.markdown(
    "<h3 class='section-heading'>🏥 Health Details</h3>",
    unsafe_allow_html=True
)

bmi_category = st.selectbox(
    "BMI Category",
    categorical_options['BMI Category']
)

smoking_status = st.selectbox(
    "Smoking Status",
    categorical_options['Smoking Status']
)

medical_history = st.selectbox(
    "Medical History",
    categorical_options['Medical History']
)

genetical_risk = st.slider(
    "Genetical Risk",
    min_value=0,
    max_value=5,
    value=0
)

st.divider()

# =========================
# FINANCIAL DETAILS
# =========================
st.markdown(
    "<h3 class='section-heading'>💰 Financial Details</h3>",
    unsafe_allow_html=True
)

income_lakhs = st.number_input(
    "Income in Lakhs",
    min_value=0,
    max_value=200,
    step=1
)

insurance_plan = st.selectbox(
    "Insurance Plan",
    categorical_options['Insurance Plan']
)

employment_status = st.selectbox(
    "Employment Status",
    categorical_options['Employment Status']
)

region = st.selectbox(
    "Region",
    categorical_options['Region']
)

st.divider()

# =========================
# INPUT DICTIONARY
# =========================
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# =========================
# PREDICTION
# =========================
if st.button("🔮 Predict Insurance Cost"):
    prediction = predict(input_dict)

    st.markdown(
        f"""
        <div class="prediction-box">
            Estimated Insurance Cost<br><br>
            ₹ {prediction:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )