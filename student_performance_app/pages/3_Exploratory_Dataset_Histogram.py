import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

(
    cols_list, time_cols, score_cols, cardinal_cols, category_cols, target_col,
    lmh_col, nnp_col, yn_col, school_col, parental_col, distance_col, gender_col,
    lmh_order, nnp_order, yn_order, school_order, parental_order, distance_order, gender_order
) = st.session_state['col_desp']


st.set_page_config(page_title="Explore Data", page_icon="✍️")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
selected_status = st.sidebar.selectbox('Select Group by Column',
                                       options=['NA'] + cols_list)

dtf = st.session_state['dataframe']
if selected_status == 'NA':
    fig = px.histogram(dtf, x='Exam_Score')
else:
    fig = px.histogram(dtf, x='Exam_Score', color=selected_status)
st.plotly_chart(fig, use_container_width=True)