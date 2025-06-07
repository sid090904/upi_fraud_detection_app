import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie(url: str):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

def app():
    # Hero Section (unchanged)
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1A2A6C 0%, #B21F1F 50%, #FDBB2D 100%);
        padding: 60px; border-radius: 12px; text-align: center;
        color: white; margin-bottom: 30px;
    ">
        <h1 style="font-size: 3.5rem; margin-bottom: 10px;">🚀 UPI Fraud Detection System</h1>
        <p style="font-size: 1.2rem; max-width: 800px; margin: auto;">
            Real‑time, rule‑based fraud alerts to keep your UPI transactions airtight.  
            Intelligent rules scan every transaction and flag anomalies instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Lottie Animation (unchanged)
    lottie_url = "https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json"
    lottie_json = load_lottie(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=300, key="hero_lottie")

    st.markdown("---")

    # Login Expander with Bank Dropdown
    with st.expander("🔒 Login"):
        if not st.session_state.get("logged_in", False):
            name = st.text_input("Your Name", placeholder="e.g., alice")
            bank = st.selectbox(
                "Select Your Bank",
                ["okicici", "oksbi", "okhdfc", "okaxis", "okpaytm", "okphonepe"]
            )
            if st.button("Login"):
                if name and bank:
                    upi_id = f"{name.lower()}@{bank}"
                    st.session_state["user_name"] = name.title()
                    st.session_state["user_upi"] = upi_id
                    st.session_state["logged_in"] = True
                    st.success(f"Welcome, {name.title()}! Your UPI ID is `{upi_id}`")
                else:
                    st.error("Please enter your name and select your bank.")
        else:
            st.write(f"✅ Logged in as **{st.session_state['user_name']}**")
            st.write(f"🔑 Your UPI ID: `{st.session_state['user_upi']}`")

    st.markdown("---")

    # Feature Highlights (unchanged)
    cols = st.columns(3, gap="large")
    features = [
        ("⚡ Instant Detection", "Transactions over ₹50,000 or odd‑hour txns flagged immediately."),
        ("🛡️ Multi‑Rule Engine", "Checks category, location, device integrity, UPI‑ID patterns, and more."),
        ("📊 Audit Trail", "Every action logged for compliance and future analysis.")
    ]
    for col, (title, desc) in zip(cols, features):
        col.markdown(f"""
        <div style="
            background: #FFFFFF; padding: 20px; border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center;
            height: 180px;
        ">
            <h3 style="color: #1A2A6C; margin-bottom: 10px;">{title}</h3>
            <p style="color: #555; font-size: 0.95rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align: center; font-size:1rem;">👉 Use the <strong>sidebar</strong> to kick off your first transaction!</p>',
        unsafe_allow_html=True
    )
