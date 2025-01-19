import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

question_dict = {
    "anx": {
        "anx_q1": "1. In a semester, how often you felt nervous, anxious or on edge due to academic pressure?",
        "anx_q2": "2. In a semester, how often have you been unable to stop worrying about your academic affairs?",
        "anx_q3": "3. In a semester, how often have you had trouble relaxing due to academic pressure?",
        "anx_q4": "4. In a semester, how often have you been easily annoyed or irritated because of academic pressure?",
        "anx_q5": "5. In a semester, how often have you worried too much about academic affairs?",
        "anx_q6": "6. In a semester, how often have you been so restless due to academic pressure that it is hard to sit still?",
        "anx_q7": "7. In a semester, how often have you felt afraid, as if something awful might happen?",
    },
    "str": {
        "str_q1": "1. In a semester, how often have you felt upset due to something that happened in your academic affairs? ",
        "str_q2": "2. In a semester, how often you felt as if you were unable to control important things in your academic affairs?",
        "str_q3": "3. In a semester, how often you felt nervous and stressed because of academic pressure?",
        "str_q4": "4. In a semester, how often you felt as if you could not cope with all the mandatory academic activities? (e.g, assignments, quiz, exams) ",
        "str_q5": "5. In a semester, how often you felt confident about your ability to handle your academic / university problems?",
        "str_q6": "6. In a semester, how often you felt as if things in your academic life is going on your way? ",
        "str_q7": "7. In a semester, how often are you able to control irritations in your academic / university affairs? ",
        "str_q8": "8. In a semester, how often you felt as if your academic performance was on top?",
        "str_q9": "9. In a semester, how often you got angered due to bad performance or low grades that is beyond your control? ",
        "str_q10": "10. In a semester, how often you felt as if academic difficulties are piling up so high that you could not overcome them? ",
    },
    "dep": {
        "dep_q1": "1. In a semester, how often have you had little interest or pleasure in doing things?",
        "dep_q2": "2. In a semester, how often have you been feeling down, depressed or hopeless?",
        "dep_q3": "3. In a semester, how often have you had trouble falling or staying asleep, or sleeping too much? ",
        "dep_q4": "4. In a semester, how often have you been feeling tired or having little energy?",
        "dep_q5": "5. In a semester, how often have you had poor appetite or overeating? ",
        "dep_q6": "6. In a semester, how often have you been feeling bad about yourself - or that you are a failure or have let yourself or your family down?",
        "dep_q7": "7. In a semester, how often have you been having trouble concentrating on things, such as reading the books or watching television?",
        "dep_q8": "8. In a semester, how often have you moved or spoke too slowly for other people to notice? Or you've been moving a lot more than usual because you've been restless?",
        "dep_q9": "9. In a semester, how often have you had thoughts that you would be better off dead, or of hurting yourself? ",
    },
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

regularity_dict = {0: "Rarely", 1: "Sometimes", 2: "Usually", 3: "Often"}



if "active_page" not in st.session_state:
    st.session_state.active_page = "Tests"
if "result" not in st.session_state:
    st.session_state.result = None


def get_results():
    models = {
        "Anxiety": TabularPredictor.load("./AutogluonModels/Anxiety"),
        "Depression": TabularPredictor.load("./AutogluonModels/Depression"),
        "Stress": TabularPredictor.load("./AutogluonModels/Stress"),
    }

    results = [
        models["Anxiety"].predict(pd.DataFrame(anxiety_answ, index=[0])),
        models["Depression"].predict(pd.DataFrame(depression_answ, index=[0])),
        models["Stress"].predict(pd.DataFrame(stress_answ, index=[0]))
    ]

    st.info("results: {}".format(results[0].values))
    st.info("results: {}".format(results[1].values))
    st.info("results: {}".format(results[2].values))


    st.session_state.active_page = "Results"
    st.session_state.result = results


info_string = "You didn't complete {} test.\n Make sure you filled all questions if you want to know your results."
@st.dialog("Are you sure?")
def confirmation_modal():
    st.write("Do you want to proceed?")
    if (
        None in anxiety_answ.values()
        and None in depression_answ.values()
        and None in stress_answ.values()
    ):
        st.error(
            "You didn't complete any test! Fill out at least one, so we could analize your state"
        )
    else:
        if None in anxiety_answ.values():
            st.info(
                info_string.format("Anxiety")
            )
        if None in stress_answ.values():
            st.info(
                info_string.format("Stress")
            )
        if None in depression_answ.values():
            st.info(
                info_string.format("Depression")
            )

            # Confirmation control
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                get_results()
        with col2:
            if st.button("No"):
                st.rerun()

if "error" in st.session_state:
    st.error("Something went wrong. Restarting..")
    st.session_state.error = None

if st.session_state.active_page == "Tests":
    tab1, tab2, tab3 = st.tabs(["Anxiety Test", "Stress Test", "Depression Test"])
    st.info(st.session_state)
    with tab1:
        for key in question_dict["anx"]:
            anxiety_answ[key] = st.radio(
                question_dict["anx"][key],
                options=regularity_dict.keys(),
                format_func=lambda x: regularity_dict[x],
                index=None,
            )
        if None not in anxiety_answ.values():
            st.button("Send answers", on_click=confirmation_modal, key="anx_send")
    with tab2:
        for key in question_dict["str"]:
            stress_answ[key] = st.radio(
                question_dict["str"][key],
                options=regularity_dict.keys(),
                format_func=lambda x: regularity_dict[x],
                index=None,
            )
        if None not in stress_answ.values():
            st.button("Send answers", on_click=confirmation_modal, key="stress_send")
    with tab3:
        for key in question_dict["dep"]:
            depression_answ[key] = st.radio(
                question_dict["dep"][key],
                options=regularity_dict.keys(),
                format_func=lambda x: regularity_dict[x],
                index=None,
            )
        if None not in depression_answ.values():
            st.button("Send answers", on_click=confirmation_modal, key="depr_send")

elif st.session_state.active_page == "Results":
    st.subheader("Results")
    for index, _ in enumerate(["Anxiety", "Stress", "Depression"]):
        st.write(_ + ": {}".format(st.session_state.results[index]))
else:
    st.session_state.error = "true"
    st.session_state.active_page = "Tests"
    st.rerun()
