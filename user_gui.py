import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
general_answ = [None] * 5
anxiety_answ = []
depression_answ = []
stress_answ = []


with right_column:
    general_answ[0] = st.radio(
        "What's your age?",
        ("18-22", "23-26", "27-30", "Above 30", "Below 18"))
    general_answ[1] = st.radio(
        "Gender?",
        ("Male", "Female", "Prefer not to say"))
    general_answ[2] = st.radio(
        "Gender?",
        ("Biological Sciences",
        "Business and Entrepreneurship Studies",
        "Engineering - CS / CSE / CSC / Similar to CS",
        "Engineering - Civil Engineering / Similar to CE",
        "Engineering - EEE / ECE / Similar to EEE",
        "Engineering - Mechanical Engineering / Similar to ME",
        "Engineering - Other",
        "Environmental and Life Sciences",
        "Law and Human Rights",
        "Liberal Arts and Social Sciences",
        "Other",
        "Pharmacy and Public Health"))
    general_answ[3] = st.radio(
        "Gender?",
        ("First Year or Equivalent",
        "Fourth Year or Equivalent",
        "Other",
        "Second Year or Equivalent",
        "Third Year or Equivalent"))
    general_answ[4] = st.radio(
        "Gender?",
        ("No", "Yes"))
    
    if(None not in general_answ):
        st.write(general_answ)

    