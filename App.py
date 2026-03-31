import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("⚡ Energy Consumption Prediction App")
st.write("Predict Usage_kWh using Machine Learning Regression Model")

# -------- INPUTS --------

lagging_reactive = st.number_input("Lagging Current Reactive Power (kVarh)", min_value=0.0)
leading_reactive = st.number_input("Leading Current Reactive Power (kVarh)", min_value=0.0)

co2 = st.number_input("CO2 Emission (tCO2)", min_value=0.0)

lagging_pf = st.number_input("Lagging Current Power Factor", min_value=0.0, max_value=1.0)
leading_pf = st.number_input("Leading Current Power Factor", min_value=0.0, max_value=1.0)

nsm = st.number_input("NSM (seconds from midnight)", min_value=0)

week_status = st.selectbox("Week Status", ["Weekday", "Weekend"])

day_of_week = st.selectbox(
    "Day of Week",
    ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
)

load_type = st.selectbox(
    "Load Type",
    ["Light_Load","Medium_Load","Maximum_Load"]
)

# -------- ENCODING --------

week_status = 1 if week_status == "Weekend" else 0

day_map = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2,
    "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
}
day_of_week = day_map[day_of_week]

load_map = {
    "Light_Load": 0,
    "Medium_Load": 1,
    "Maximum_Load": 2
}
load_type = load_map[load_type]

# -------- PREDICTION --------

if st.button("Predict Energy Usage"):

    input_data = np.array([[ 
        float(lagging_reactive),
        float(leading_reactive),
        float(co2),
        float(lagging_pf),
        float(leading_pf),
        float(nsm),
        float(week_status),
        float(day_of_week),
        float(load_type)
    ]])

    try:
        prediction = model.predict(input_data)
        st.success(f"Predicted Usage_kWh: {float(prediction[0]):.2f}")
    except Exception as e:
        st.error(f"Error: {e}")