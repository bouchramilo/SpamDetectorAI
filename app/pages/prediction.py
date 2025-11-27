import streamlit as st
import joblib
import numpy as np


st.set_page_config(
    page_title="Spam Detector AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better aesthetics
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Spam Detector AI")
    st.info("This application uses advanced Machine Learning to detect spam emails in real-time.")



# -------------------------
# Chargement du modèle
# -------------------------
@st.cache_resource
def load_model():
    return joblib.load("././models/best_text_classifier.pkl")

model = load_model()

# -------------------------
# Interface
# -------------------------
st.title("📧 Spam Detector")
st.subheader("Détection automatique des emails spam")

email = st.text_area("✍️ Entrez un email ici :", height=200)

if st.button("🔍 Détecter"):
    if email.strip() == "":
        st.warning("Veuillez entrer un texte.")
    else:
        pred = model.predict([email])[0]

        st.write("---")
        if pred == 1:
            st.error("🚨 Cet email est **SPAM**.")
        else:
            st.success("✅ Cet email est **NON SPAM**.")
