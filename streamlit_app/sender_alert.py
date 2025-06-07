import streamlit as st

def app():
    st.title("🚨 Sender Alert")

    # Only show this page if a fraud was detected
    if not st.session_state.get("is_fraud", False):
        st.warning("No suspicious transaction to alert.")
        return

    st.warning("Our system flagged this transaction as potentially fraudulent.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚫 Cancel Transaction"):
            st.success("Transaction cancelled.")
            st.session_state.clear()
    with col2:
        if st.button("✅ Proceed Anyway"):
            st.success("Proceeding to bank alert.")
            # Mark that sender overrode and then stop
            st.session_state["override"] = True
            st.info("➡️ Please select **Bank Alert** from the sidebar.")
            st.stop()
