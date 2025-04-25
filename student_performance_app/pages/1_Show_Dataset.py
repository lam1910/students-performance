import streamlit as st

st.set_page_config(page_title="Show Dataset", page_icon="📋")

dtf = st.session_state['dataframe']
st.write(dtf)
