import streamlit as st
import pandas as pd
import joblib

# Load trained model and encoders
model = joblib.load('model/traffic_model.pkl')

# Page config
st.set_page_config(page_title="Real-Time Traffic Flow Predictor", layout="centered")

# Custom CSS for style
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #E6F0FF, #F0FAFF);
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    .stMarkdown h1 {
        text-align: center;
        color: #003366;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🚦 Real-Time Traffic Flow Predictor</h1>", unsafe_allow_html=True)

st.markdown("### Enter details below to predict traffic vehicle count:")

# UI Input
location = st.selectbox("📍 Location", ['Patna Junction', 'Bailey Road', 'Kankarbagh', 'Gandhi Maidan', 'Boring Road'])
weather = st.selectbox("🌦️ Weather", ['Clear', 'Rain', 'Fog'])
road_type = st.selectbox("🛣️ Road Type", ['Highway', 'City', 'Bridge'])
hour = st.slider("⏰ Hour of the Day", 0, 23, 12)
day = st.slider("📅 Day of the Month", 1, 31, 15)
weekday = st.slider("📆 Day of Week (0=Mon)", 0, 6, 3)
avg_speed = st.slider("🚗 Avg Speed (km/h)", 5, 80, 30)

# Encode input values manually (based on training)
location_map = {'Patna Junction':0, 'Bailey Road':1, 'Kankarbagh':2, 'Gandhi Maidan':3, 'Boring Road':4}
weather_map = {'Clear':0, 'Rain':1, 'Fog':2}
road_type_map = {'Highway':0, 'City':1, 'Bridge':2}

# Create input dataframe
input_data = pd.DataFrame([[
    avg_speed, hour, day, weekday,
    location_map[location],
    weather_map[weather],
    road_type_map[road_type]
]], columns=[
    'avg_speed', 'hour', 'day', 'weekday',
    'location_enc', 'weather_enc', 'road_type_enc'
])

# Predict button
if st.button("🚥 Predict Traffic Count"):
    prediction = int(model.predict(input_data)[0])
    st.success(f"📊 **Predicted Vehicle Count: {prediction}**")
