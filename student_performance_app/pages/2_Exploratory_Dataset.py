import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

(
    cols_list, time_cols, score_cols, cardinal_cols, category_cols, target_col,
    lmh_col, nnp_col, yn_col, school_col, parental_col, distance_col, gender_col,
    lmh_order, nnp_order, yn_order, school_order, parental_order, distance_order, gender_order
) = st.session_state['col_desp']



st.set_page_config(page_title="Explore Data", page_icon="✍️")

st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
                                    ('Scatter Plot', 'Bar Chart'))

selected_status = st.sidebar.selectbox('Select X Column',
                                       options=cols_list)
dtf = st.session_state['dataframe']
fig = go.Figure()

if chart_visual == 'Scatter Plot':
    if selected_status not in time_cols and selected_status not in score_cols:
        st.warning("Please select the correct X-axis column or the correct chart type.")
    if selected_status in time_cols:
        fig.add_trace(go.Scatter(x=dtf[selected_status], y=dtf['Exam_Score'],
                                 mode='markers',
                                 name=selected_status))
    if selected_status in score_cols:
        fig.add_trace(go.Scatter(x=dtf[selected_status], y=dtf['Exam_Score'],
                                 mode='markers', name=selected_status))
if chart_visual == 'Bar Chart':
    if selected_status not in cardinal_cols and selected_status not in category_cols:
        st.warning("Please select the correct X-axis column or the correct chart type.")
    if selected_status in cardinal_cols:
        fig.add_trace(go.Bar(x=dtf[selected_status], y=dtf['Exam_Score'],
                             orientation='v',
                             name=selected_status))
    if selected_status in category_cols:
        fig.add_trace(go.Bar(x=dtf[selected_status], y=dtf['Exam_Score'],
                             orientation='v', name=selected_status
        ))
        if selected_status in lmh_col:
            fig.update_xaxes(categoryorder='array', categoryarray=lmh_order)
        elif selected_status in nnp_col:
            fig.update_xaxes(categoryorder='array', categoryarray=nnp_order)
        elif selected_status in yn_col:
           fig.update_xaxes(categoryorder='array', categoryarray=yn_order)
        elif selected_status in school_col:
            fig.update_xaxes(categoryorder='array', categoryarray=school_order)
        elif selected_status in parental_col:
            fig.update_xaxes(categoryorder='array', categoryarray=parental_order)
        elif selected_status in distance_col:
            fig.update_xaxes(categoryorder='array', categoryarray=distance_order)
        elif selected_status in gender_col:
            fig.update_xaxes(categoryorder='array', categoryarray=gender_order)
st.plotly_chart(fig, use_container_width=True)
