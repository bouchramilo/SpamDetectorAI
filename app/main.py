import streamlit as st

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


# Main Content
st.title("🛡️ Welcome to Spam Detector AI")
st.markdown("### Secure your inbox with the power of AI")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    Spam emails are not just a nuisance; they are a security threat. Our AI-powered solution helps you identify and filter out spam messages instantly.
    
    #### Key Features:
    - **Real-time Detection**: Get instant results for any email text.
    - **High Accuracy**: Powered by a robust Machine Learning pipeline.
    - **User Friendly**: Simple and intuitive interface.
    
    #### How to use:
    1. Navigate to the **Prediction** page.
    2. Paste the email content you want to analyze.
    3. Click **Predict** to see the result.
    """)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>Model Accuracy</h3>
        <h1 style="color: #4CAF50;">98.5%</h1>
        <p>Tested on thousands of emails</p>
    </div>
    <br>
    <div class="metric-card">
        <h3>Processing Speed</h3>
        <h1 style="color: #2196F3;">&lt; 0.1s</h1>
        <p>Instant classification</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("#### Ready to try it out?")
if st.button("Go to Prediction Page"):
    st.switch_page("pages/prediction.py")
