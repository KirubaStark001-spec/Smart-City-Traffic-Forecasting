# 🚦 Smart City Traffic Forecasting using Machine Learning

## 📌 Project Overview

Smart City Traffic Forecasting is a Machine Learning project that predicts the expected number of vehicles at a traffic junction based on historical traffic data. The system helps analyze traffic patterns and provides accurate traffic predictions that can support smart city planning, congestion management, and transportation optimization.

The application is developed using Python, Scikit-learn, Pandas, and Streamlit, with an interactive dashboard for real-time traffic prediction.

---

## 🎯 Objectives

* Predict traffic volume using historical data.
* Analyze traffic trends across different junctions.
* Help city planners understand traffic congestion.
* Build a user-friendly dashboard for traffic prediction.
* Demonstrate the practical application of Machine Learning in smart city management.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## 📂 Project Structure

```
TSCTF/
│
├── app.py
├── train_model.py
├── traffic_model.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── train_aWnotuB.csv
│   └── test_BdBKk80.csv
│
└── assets/
    ├── style.css
    ├── logo.png
    └── background.jpg
```

---

## 📊 Dataset

The dataset contains historical traffic information collected from four different road junctions.

### Features

* Junction
* Date and Time
* Year
* Month
* Day
* Hour

### Target

* Vehicles (Traffic Volume)

---

## 🔄 Project Workflow

1. Load the dataset.
2. Perform data preprocessing.
3. Convert DateTime into Year, Month, Day, and Hour.
4. Remove unnecessary columns.
5. Perform Exploratory Data Analysis (EDA).
6. Train the Random Forest Regression model.
7. Evaluate model performance.
8. Save the trained model.
9. Build an interactive Streamlit dashboard.
10. Predict traffic volume based on user input.

---

## 🤖 Machine Learning Model

**Algorithm Used**

* Random Forest Regressor

### Model Performance

| Metric                         |  Value |
| ------------------------------ | -----: |
| Mean Absolute Error (MAE)      |   2.86 |
| Root Mean Squared Error (RMSE) |   4.29 |
| R² Score                       | 95.49% |

The model achieved excellent prediction accuracy, making it suitable for traffic forecasting applications.

---

## 🚀 Features

* Interactive Streamlit Dashboard
* Real-Time Traffic Prediction
* User-Friendly Interface
* Machine Learning Powered Prediction
* Traffic Status Indicator
* Data Visualization
* Model Performance Metrics
* Clean and Responsive Design

---

## ▶️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd TSCTF
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📈 Sample Prediction

**Input**

* Junction: 1
* Year: 2017
* Month: 6
* Day: 15
* Hour: 18

**Predicted Vehicles**

```
100 Vehicles
```

Traffic Status

```
Heavy Traffic
```

---

## 🌟 Future Enhancements

* Live Traffic API Integration
* Weather-Based Traffic Prediction
* Google Maps Integration
* Deep Learning Models (LSTM)
* Real-Time Vehicle Count
* Smart Route Recommendation
* Mobile Application
* Traffic Alert Notifications

---

## 👨‍💻 Developer

**Kirubanantham M**

Machine Learning | Python | Data Analytics | AI Enthusiast

---

## 📄 License

This project is developed for educational and internship purposes.

---

## ⭐ Acknowledgement

Thanks to the open-source Python community and the developers of Pandas, Scikit-learn, Streamlit, Matplotlib, and Seaborn for providing excellent libraries that made this project possible.
