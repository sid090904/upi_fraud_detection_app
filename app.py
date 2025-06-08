import streamlit as st

# ─────── Must be first Streamlit command ───────
st.set_page_config(page_title="UPI Fraud Detection", layout="wide")
# ────────────────────────────────────────────────

# Sidebar navigation
st.sidebar.title("UPI Fraud Detection")
choice = st.sidebar.radio(
    "Navigate to",
    ["Welcome", "UPI Payment Interface", "Transaction Status", "Sender Alert", "Bank Alert"]
)

if choice == "Welcome":
    from streamlit_app.welcome import app as welcome_app
    welcome_app()

elif choice == "UPI Payment Interface":
    from streamlit_app.payment_interface import app as payment_app
    payment_app()

elif choice == "Sender Alert":
    from streamlit_app.sender_alert import app as sender_app
    sender_app()

elif choice == "Bank Alert":
    from streamlit_app.bank_alert import app as bank_app
    bank_app()

elif choice == "Transaction Status":
    from streamlit_app.user_notification import app as notify_app
    notify_app()

# Triggering redeployment

