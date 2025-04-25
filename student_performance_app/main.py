import streamlit as st
import polars as pl
from pathlib import Path
import sys

if '~/students-performance/' not in sys.path:
    sys.path.append('~/students-performance')
st.set_page_config(page_title='Student Performance App', page_icon='👋')

st.write("# Welcome to Student Performance App! 👋")

st.sidebar.success("Select your usage above.")

st.markdown(
    """
    Hello world!
"""
)

DATA_PATH = 'data/StudentPerformanceFactors.csv'

file_path = Path(DATA_PATH)
if not file_path.exists():
    dtf = pl.DataFrame()
else:
    dtf = pl.read_csv(file_path)
    dtf = dtf.fill_null('NA')

if 'dataframe' not in st.session_state:
    st.session_state['dataframe'] = dtf #or whatever default

COLS_LIST = [
    'Hours_Studied', 'Attendance', 'Parental_Involvement', 'Access_to_Resources',
    'Extracurricular_Activities', 'Sleep_Hours', 'Previous_Scores', 'Motivation_Level', 'Internet_Access',
    'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality', 'School_Type', 'Peer_Influence', 'Physical_Activity',
    'Learning_Disabilities', 'Parental_Education_Level', 'Distance_from_Home', 'Gender'
]

TIME_COLS = ['Hours_Studied', 'Sleep_Hours']
SCORE_COLS = ['Attendance', 'Previous_Scores']
CARDINAL_COLS = ['Tutoring_Sessions', 'Physical_Activity']
CATEGORY_COLS = [
    'Parental_Involvement', 'Access_to_Resources', 'Extracurricular_Activities', 'Motivation_Level',
    'Internet_Access', 'Family_Income', 'Teacher_Quality', 'School_Type', 'Peer_Influence',
    'Learning_Disabilities', 'Parental_Education_Level', 'Distance_from_Home', 'Gender'
]
TARGET_COL = 'Exam_Score'
LMH_COL = ['Parental_Involvement', 'Access_to_Resources', 'Motivation_Level', 'Family_Income', 'Teacher_Quality']
NNP_COL = ['Peer_Influence']
YN_COL = ['Extracurricular_Activities', 'Internet_Access', 'Learning_Disabilities']
SCHOOL_COL = ['School_Type']
PARENTAL_COL = ['Parental_Education_Level']
DISTANCE_COL = ['Distance_from_Home']
GENDER_COL = ['Gender']
LMH_ORDER = ['NA', 'Low', 'Medium', 'High']
NNP_ORDER = ['NA', 'Negative', 'Neutral', 'Positive']
YN_ORDER = ['Yes', 'No', 'NA']
SCHOOL_ORDER = ['NA', 'Public', 'Private']
PARENTAL_ORDER = ['NA', 'High School', 'College', 'Postgraduate']
DISTANCE_ORDER = ['NA', 'Near', 'Moderate', 'Far']
GENDER_ORDER = ['Male', 'Female', 'NA']
COLS_DESCRIPTION = [
    COLS_LIST, TIME_COLS, SCORE_COLS, CARDINAL_COLS, CATEGORY_COLS, TARGET_COL,
    LMH_COL, NNP_COL, YN_COL, SCHOOL_COL, PARENTAL_COL, DISTANCE_COL, GENDER_COL,
    LMH_ORDER, NNP_ORDER, YN_ORDER, SCHOOL_ORDER, PARENTAL_ORDER, DISTANCE_ORDER, GENDER_ORDER
]
st.session_state['col_desp'] = COLS_DESCRIPTION
