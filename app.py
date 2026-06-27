import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Smart City Traffic Intelligence",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#081c3a,#0d2c54,#122f67,#183c77);
    background-size:400% 400%;
}

.main-title{
    font-size:42px;
    font-weight:700;
    color:white;
}

.subtitle{
    font-size:18px;
    color:#d9d9d9;
}

.glass{
background:rgba(255,255,255,0.12);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,.25);
backdrop-filter: blur(12px);
box-shadow:0 8px 32px rgba(0,0,0,.25);
}

.metric{
font-size:34px;
font-weight:bold;
color:white;
}

.label{
font-size:15px;
color:#d9d9d9;
}

.sidebar .sidebar-content{
background:#081c3a;
}

hr{
border:none;
height:1px;
background:#ffffff33;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
model = joblib.load("traffic_model.pkl")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
"""
<div class='glass'>
<div class='main-title'>🚦 Smart City Traffic Intelligence Dashboard</div>
<div class='subtitle'>
AI Powered Traffic Forecasting using Random Forest Machine Learning
</div>
</div>
""",
unsafe_allow_html=True
)

st.write("")

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='glass'>
    <div class='metric'>95.49%</div>
    <div class='label'>Model Accuracy</div>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='glass'>
    <div class='metric'>48,120</div>
    <div class='label'>Traffic Records</div>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='glass'>
    <div class='metric'>4</div>
    <div class='label'>Junctions</div>
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='glass'>
    <div class='metric'>Random Forest</div>
    <div class='label'>ML Algorithm</div>
    </div>
    """,unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙ Prediction Settings")

junction=st.sidebar.selectbox("Junction",[1,2,3,4])

year=st.sidebar.selectbox("Year",[2015,2016,2017])

month=st.sidebar.selectbox("Month",list(range(1,13)))

day=st.sidebar.slider("Day",1,31,15)

hour=st.sidebar.slider("Hour",0,23,12)

predict=st.sidebar.button("🚀 Predict Traffic")

# --------------------------------------------------
# PLACEHOLDER
# --------------------------------------------------

st.markdown("## 📊 Prediction Result")

if predict:

    sample=pd.DataFrame({
        "Junction":[junction],
        "Year":[year],
        "Month":[month],
        "Day":[day],
        "Hour":[hour]
    })

    result=model.predict(sample)[0]

    st.success("Prediction Completed Successfully!")

    st.metric("Predicted Vehicles",int(result))

else:

    st.info("👈 Enter values in the sidebar and click Predict Traffic.")

st.write("")

st.markdown("---")

st.caption("Smart City Traffic Forecasting | Internship Project | Streamlit + Machine Learning")