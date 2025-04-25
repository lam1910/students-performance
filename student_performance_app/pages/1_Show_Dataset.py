import streamlit as st


SERVER_URL = "http://127.0.0.1"
SERVER_PORT = "8000"
END_POINT = "data"

st.set_page_config(page_title="Show Dataset", page_icon="✍️")

dtf = st.session_state['dataframe']
st.write(dtf)
