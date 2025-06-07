import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.badges import badge

def app():
    st.markdown("<h2 style='text-align:center; color:#4CAF50;'>Transaction Status</h2>", unsafe_allow_html=True)

    txn = st.session_state.get("transaction", {})
    is_fraud = st.session_state.get("is_fraud")

    if not txn:
        st.warning("🚫 No transaction data found. Please initiate a transaction first.")
        return

    st.markdown("---")
    colored_header(
        label="🔍 Transaction Summary",
        description="Below are the details of your recent UPI transaction",
        color_name="blue-70"
    )

    with st.container():
        st.markdown(f"""
        <div style='padding:10px; background-color:#f9f9f9; border-radius:10px'>
        <b>User ID:</b> {txn.get('sender_upi', 'N/A')}<br>
        <b>Amount:</b> ₹{txn.get('amount', 'N/A')}<br>
        <b>Transaction Type:</b> {txn.get('category', 'N/A').title()}<br>
        <b>Location:</b> {txn.get('location', 'N/A')}<br>
        <b>Time Since Last Transaction:</b> {txn.get('time_gap', 0)} seconds
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    if is_fraud is True:
        st.error("⚠️ This transaction has been flagged as **FRAUDULENT**.")

        st.markdown("**Reason(s) may include:**")
        st.markdown("- ❌ High amount or suspicious category")
        st.markdown("- ❌ Risky device used (e.g. rooted/jailbroken)")
        st.markdown("- ❌ Too many failed attempts")
        st.markdown("- ❌ Short time gap between transactions")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔒 Go to Sender Alert Page"):
                st.session_state.page = "sender_alert"
                st.rerun()
        with col2:
            if st.button("🔁 Cancel and Reinitiate Payment"):
                st.session_state.page = "payment"
                st.rerun()

    elif is_fraud is False:
        st.success("✅ This transaction appears to be **legitimate**.")
        if st.button("🏦 Proceed to Bank Alert"):
            st.session_state.page = "bank_alert"
            st.rerun()
    else:
        st.warning("❓ Unable to determine transaction result. Please re-check inputs.")
