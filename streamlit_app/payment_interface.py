import streamlit as st
from datetime import datetime
from streamlit_app.fraud_detection import predict_fraud

def app():
    st.title("💸 UPI Payment Interface")
    st.markdown("Enter transaction details below:")

    # -- Auto compute time_gap --
    now = datetime.now()
    last_ts = st.session_state.get("last_timestamp")
    if last_ts:
        delta = now - last_ts
        time_gap = int(delta.total_seconds())
    else:
        time_gap = 0

    with st.form("transaction_form"):
        col1, col2 = st.columns(2)

        with col1:
            # Prefill sender UPI from login session
            sender_upi = st.text_input(
                "Your UPI ID",
                value=st.session_state.get("user_upi", ""),
                disabled=st.session_state.get("logged_in", False)
            )

            amount = st.number_input("Amount (₹)", min_value=1.0, format="%.2f")

            transaction_types = [
                "Personal", "Shopping", "Bill Payment", "Recharge",
                "Lottery", "Crypto", "Utilities", "Others"
            ]
            transaction_type = st.selectbox("Transaction Type", transaction_types)

            top_cities = [
                "Bangalore", "Mumbai", "Delhi", "Chennai", "Kolkata",
                "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Other"
            ]
            location = st.selectbox("Location (City)", top_cities)

            time = st.slider("Transaction Time (Hour)", 0, 23, now.hour)

        with col2:
            device = st.selectbox(
                "Device",
                ["Android", "iOS", "Rooted Android", "Jailbroken iOS"],
                help="Rooted/Jailbroken devices pose higher risk."
            )

            recipient_upi = st.text_input("Recipient UPI ID", placeholder="e.g., bob@bank")

            failed_attempts = st.number_input(
                "Prev. Failed Attempts", 0, 10, 0,
                help=">3 failed attempts increases risk."
            )

        submitted = st.form_submit_button("🔍 Check for Fraud")

    if submitted:
        txn = {
            "sender_upi": sender_upi.lower(),
            "recipient_upi": recipient_upi.lower(),
            "amount": amount,
            "category": transaction_type.lower(),  # stored as category internally
            "location": location,
            "time": time,
            "device": device.lower(),
            "failed_attempts": failed_attempts,
            "time_gap": time_gap
        }

        is_fraud = predict_fraud(txn)
        st.session_state["transaction"] = txn
        st.session_state["is_fraud"] = is_fraud
        st.session_state["last_timestamp"] = now

        if is_fraud:
            st.error("⚠️ Potential Fraud Detected! Please select **Sender Alert** in the sidebar.")
        else:
            st.success("✅ No issues found. Please select **Transaction Status** in the sidebar.")
        st.stop()
