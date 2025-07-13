🚦 Real-Time Traffic Flow Predictor

🔸An AI-powered traffic flow prediction system that estimates the number of vehicles using real-time input like time, location, weather, road type, and average speed.  
Built using **Python, Machine Learning**, and a fully styled **Streamlit Dashboard**.

📌 Key Features

- 🧠 **ML Model**: Random Forest Regressor
- 📍 **Location-aware** prediction
- ⏰ **Time & Weather-based** inputs
- 🎛️ **Live Dashboard** built using Streamlit
- 📄 **Full PDF Report** included (project methodology & results)

 🧰 Tech Stack

| Category      | Tools Used                             |
|---------------|----------------------------------------|
| Language      | Python 3.11                            |
| Libraries     | Pandas, Scikit-learn, Joblib           |
| Model         | RandomForestRegressor                  |
| Frontend      | Streamlit (custom layout + CSS)        |
| Visualization | Matplotlib (for EDA)                   |

📂 Project Structure
real_time_traffic_prediction/
├── app.py # Streamlit dashboard
├── data/
│ ├── traffic_data.csv # Raw data
│ └── traffic_cleaned.csv # Cleaned data
├── model/
│ └── traffic_model.pkl # Trained ML model
├── notebooks/
│ └── eda.ipynb # Data exploration notebook
├── src/
│ ├── generate_dataset.py # Synthetic data generator
│ └── model.py # Model training script
├── 8271.pdf # Final project report
└── README.md

📸 Dashboard Preview
🔸Styled 2-column layout with real-time prediction display

🧭 Input Panel (Left):
📍 Location, 🌦️ Weather, 🛣️ Road Type, ⏰ Hour, 📅 Day, 🚗 Avg Speed

📊 Output Panel (Right):
🔸Predicted Vehicle Count (AI-powered)

🧪 Synthetic Dataset Creation
✅ Wrote a custom Python script generate_dataset.py to generate realistic traffic data:

🔸 timestamp, location, vehicle_count, avg_speed, weather, road_type

📄 Saved as traffic_data.csv inside data/ folder

🧹Data Cleaning & Feature Engineering
📘 Notebook: notebooks/eda.ipynb

🔸Converted timestamp into hour, day, weekday

🔸Applied Label Encoding for categorical features:

🔸location, weather, road_type

🔸Saved cleaned data as traffic_cleaned.csv

🧠  Model Training (ML Model)
🎯 Target: vehicle_count

🧪 Algorithm: RandomForestRegressor

📁 Script: src/model.py

✅ Performed:

🔸Train-Test Split

🔸Training

🔸MAE, RMSE, R² Evaluation

📦 Saved final model as traffic_model.pkl

🚀 How to Run
🔸git clone https://github.com/Youraj8271/real-time-traffic-prediction.git
🔸cd real-time-traffic-prediction

📍 Install dependencies
🔸pip install -r requirements.txt

📍Run the app
🔸streamlit run app.py

🧠 How it Works
 🔸Collect simulated traffic data (timestamp, location, weather, speed)

 🔸Preprocess + encode with pandas + sklearn

 🔸Train model on 80% of the data

 🔸Predict vehicle_count based on real-time inputs

 🔸Show prediction on stylish Streamlit dashboard

💡 Like this Project?
⭐ Star this repo if you learned something!
🛠️ Fork and customize it for your own city traffic!

🔥 By: Youraj Kumar
🎓 IIT Patna
📧 youraj_2412res154@iitp.ac.in
🔗 GitHub.com/Youraj8271
