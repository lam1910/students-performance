import plotly.express as px
import streamlit as st

(
    cols_list, time_cols, score_cols, cardinal_cols, category_cols, target_col,
    lmh_col, nnp_col, yn_col, school_col, parental_col, distance_col, gender_col,
    lmh_order, nnp_order, yn_order, school_order, parental_order, distance_order, gender_order
) = st.session_state['col_desp']

st.set_page_config(page_title="Explore Data", page_icon="📜")
st.sidebar.markdown("Select the Charts/Plots accordingly:")
selected_status = st.sidebar.selectbox('Select Group by Column',
                                       options=['NA'] + cols_list)
bin_nums = st.sidebar.number_input('Number of bins', min_value=0, max_value=100, value=10, step=5)

dtf = st.session_state['dataframe']
if selected_status == 'NA':
    if bin_nums == 0:
        st.warning("Number of bins is set to 0. Auto-binning will be used.")
        fig = px.histogram(dtf, x='Exam_Score')
    else:
        fig = px.histogram(dtf, x='Exam_Score', nbins=bin_nums)
    chart_name = 'Histogram of Exam Score'
else:
    if bin_nums == 0:
        st.warning("Number of bins is set to 0. Auto-binning will be used.")
        fig = px.histogram(dtf, x='Exam_Score', color=selected_status)
    else:
        fig = px.histogram(dtf, x='Exam_Score', nbins=bin_nums, color=selected_status)
    chart_name = 'Histogram of Exam Score by ' + selected_status

fig.update_layout(
    title={
        'text': chart_name,
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font=dict(
        family="Courier New, monospace",
        size=22,
        color="RebeccaPurple"
    )
)
st.plotly_chart(fig, use_container_width=True)
