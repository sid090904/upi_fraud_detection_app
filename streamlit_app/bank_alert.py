import streamlit as st

def app():
    st.title("🏦 Bank Alert System")

    if not (st.session_state.get("is_fraud") and st.session_state.get("override")):
        st.warning("No transaction requires bank review.")
        return

    st.error("🔒 Final review by bank required:")
    st.json(st.session_state["transaction"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Approve Transaction"):
            st.session_state.clear()
            st.success("Transaction approved.")
    with col2:
        if st.button("❌ Reject Transaction"):
            st.session_state.clear()
            st.error("Transaction rejected.")
