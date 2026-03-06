import streamlit as st


def show_agent_timeline(steps):

    st.markdown("### Agent Activity")

    for step in steps:

        st.markdown(f"➡ {step}")