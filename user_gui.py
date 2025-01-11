import streamlit as st
import requests

# Or even better, call Streamlit functions inside a "with" block:
general_answ = {
    "age": None,
    "gender": None,
    "department": None,
    "academic_year": None,
    "scholarship": None,
}
anxiety_answ = {
    "anx_q1": None,
    "anx_q2": None,
    "anx_q3": None,
    "anx_q4": None,
    "anx_q5": None,
    "anx_q6": None,
    "anx_q7": None,
}

depression_answ = {
    "dep_q1": None,
    "dep_q2": None,
    "dep_q3": None,
    "dep_q4": None,
    "dep_q5": None,
    "dep_q6": None,
    "dep_q7": None,
    "dep_q8": None,
    "dep_q9": None,
}
stress_answ = {
    "str_q1": None,
    "str_q2": None,
    "str_q3": None,
    "str_q4": None,
    "str_q5": None,
    "str_q6": None,
    "str_q7": None,
    "str_q8": None,
    "str_q9": None,
    "str_q10": None,
}

tab1, tab2, tab3, tab4 = st.tabs(
    ["General questions", "Anxiety Test", "Stress Test", "Depression Test"]
)

regularity_dict = {0: "Rarely", 1: "Sometimes", 2: "Usually", 3: "Often"}


with tab1:
    general_answ["age"] = st.radio(
        "1. What's your age?",
        ("18-22", "23-26", "27-30", "Above 30", "Below 18"),
        index=None,
    )

    general_answ["gender"] = st.radio(
        "2. Gender", ("Male", "Female", "Prefer not to say"), index=None
    )

    general_answ["department"] = st.radio(
        "3. Department",
        (
            "Biological Sciences",
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
            "Pharmacy and Public Health",
        ),
        index=None,
    )

    general_answ["academic_year"] = st.radio(
        "4. Academic Year",
        (
            "First Year or Equivalent",
            "Fourth Year or Equivalent",
            "Other",
            "Second Year or Equivalent",
            "Third Year or Equivalent",
        ),
        index=None,
    )

    general_answ["scholarship"] = st.radio("Scholardhip", ("No", "Yes"), index=None)

with tab2:
    if None not in general_answ.values():
        anxiety_answ["anx_q1"] = st.radio(
            "1. In a semester, how often you felt nervous, anxious or on edge due to academic pressure?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        anxiety_answ["anx_q2"] = st.radio(
            "2. In a semester, how often have you been unable to stop worrying about your academic affairs?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        anxiety_answ["anx_q3"] = st.radio(
            "3. In a semester, how often have you had trouble relaxing due to academic pressure?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        anxiety_answ["anx_q4"] = st.radio(
            "4. In a semester, how often have you been easily annoyed or irritated because of academic pressure?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        anxiety_answ["anx_q5"] = st.radio(
            "5. In a semester, how often have you worried too much about academic affairs?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        anxiety_answ["anx_q6"] = st.radio(
            "6. In a semester, how often have you been so restless due to academic pressure that it is hard to sit still?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        anxiety_answ["anx_q7"] = st.radio(
            "7. In a semester, how often have you felt afraid, as if something awful might happen?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )
        if None not in anxiety_answ.values():
            get_results()
    else:
        st.warning("Firstly you must complete general info")
with tab3:
    if None not in general_answ.values():
        stress_answ["str_q1"] = st.radio(
            "1. In a semester, how often have you felt upset due to something that happened in your academic affairs?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q2"] = st.radio(
            "2. In a semester, how often you felt as if you were unable to control important things in your academic affairs?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q3"] = st.radio(
            "3. In a semester, how often you felt nervous and stressed because of academic pressure?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q4"] = st.radio(
            "4. In a semester, how often you felt as if you could not cope with all the mandatory academic activities? (e.g, assignments, quiz, exams)",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q5"] = st.radio(
            "5. In a semester, how often you felt confident about your ability to handle your academic / university problems?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q6"] = st.radio(
            "6. In a semester, how often you felt as if things in your academic life is going on your way?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q7"] = st.radio(
            "7. In a semester, how often are you able to control irritations in your academic / university affairs?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q8"] = st.radio(
            "8. In a semester, how often you felt as if your academic performance was on top?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q9"] = st.radio(
            "9. In a semester, how often you got angered due to bad performance or low grades that is beyond your control?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        stress_answ["str_q10"] = st.radio(
            "10. In a semester, how often you felt as if academic difficulties are piling up so high that you could not overcome them?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )
        if None not in stress_answ.values():
            st.write(stress_answ)
    else:
        st.warning("Firstly you must complete general info")
with tab4:
    if None not in general_answ.values():
        depression_answ["dep_q1"] = st.radio(
            "1. In a semester, how often have you had little interest or pleasure in doing things?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q2"] = st.radio(
            "2. In a semester, how often have you been feeling down, depressed or hopeless?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q3"] = st.radio(
            "3. In a semester, how often have you had trouble falling or staying asleep, or sleeping too much?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q4"] = st.radio(
            "4. In a semester, how often have you been feeling tired or having little energy?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q5"] = st.radio(
            "5. In a semester, how often have you had poor appetite or overeating?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q6"] = st.radio(
            "6. In a semester, how often have you been feeling bad about yourself - or that you are a failure or have let yourself or your family down?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q7"] = st.radio(
            "7. In a semester, how often have you been having trouble concentrating on things, such as reading the books or watching television?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q8"] = st.radio(
            "8. In a semester, how often have you moved or spoke too slowly for other people to notice? Or you've been moving a lot more than usual because you've been restless?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        depression_answ["dep_q9"] = st.radio(
            "9. In a semester, how often have you had thoughts that you would be better off dead, or of hurting yourself?",
            options=regularity_dict.keys(),
            format_func=lambda x: regularity_dict[x],
            index=None,
        )

        if None not in depression_answ.values():
            st.write(depression_answ)
    else:
        st.warning("Firstly you must complete general info")


def get_results():
    requests.post(
        "ml-api-link", data={general_answ, anxiety_answ, stress_answ, depression_answ}
    )
    # <data parsing>
    # return results
