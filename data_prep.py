import pandas as pd
import numpy as np

def data_preparation(dataToGet):
    # Analiza i małe zmiany
    df = pd.read_csv('Raw data.csv')
    print(df.head())
    print(df.shape)
    headersToDrop = ["3. University", "6. Current CGPA", "Anxiety Value", "Stress Value", "Depression Value"]
    df.drop(headersToDrop, axis=1, inplace=True)
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    df[numeric_columns] = df[numeric_columns].astype('category')
    print("Does data set has any missing data?\n", df.isnull().values.any())

    # Zmiana nazwy kolumn -> zrobione przez Nazariego
    df.rename(
        columns={
            "1. Age": "age",
            "2. Gender": "gender",
            "4. Department": "department",
            "5. Academic Year": "academic_year",
            "7. Did you receive a waiver or scholarship at your university?": "scholarship",
            '1. In a semester, how often you felt nervous, anxious or on edge due to academic pressure? ': 'anx_q1',
            '2. In a semester, how often have you been unable to stop worrying about your academic affairs? ': 'anx_q2',
            '3. In a semester, how often have you had trouble relaxing due to academic pressure? ': 'anx_q3',
            '4. In a semester, how often have you been easily annoyed or irritated because of academic pressure?': 'anx_q4',
            '5. In a semester, how often have you worried too much about academic affairs? ': 'anx_q5',
            '6. In a semester, how often have you been so restless due to academic pressure that it is hard to sit still?': 'anx_q6',
            '7. In a semester, how often have you felt afraid, as if something awful might happen?': 'anx_q7',
            'Anxiety Label': 'anxiety_label',
            '1. In a semester, how often have you felt upset due to something that happened in your academic affairs? ': 'str_q1',
            '2. In a semester, how often you felt as if you were unable to control important things in your academic affairs?': 'str_q2',
            '3. In a semester, how often you felt nervous and stressed because of academic pressure? ': 'str_q3',
            '4. In a semester, how often you felt as if you could not cope with all the mandatory academic activities? (e.g, assignments, quiz, exams) ': 'str_q4',
            '5. In a semester, how often you felt confident about your ability to handle your academic / university problems?': 'str_q5',
            '6. In a semester, how often you felt as if things in your academic life is going on your way? ': 'str_q6',
            '7. In a semester, how often are you able to control irritations in your academic / university affairs? ': 'str_q7',
            '8. In a semester, how often you felt as if your academic performance was on top?': 'str_q8',
            '9. In a semester, how often you got angered due to bad performance or low grades that is beyond your control? ': 'str_q9',
            '10. In a semester, how often you felt as if academic difficulties are piling up so high that you could not overcome them? ': 'str_q10',
            'Stress Label': 'stress_label',
            '1. In a semester, how often have you had little interest or pleasure in doing things?': 'dep_q1',
            '2. In a semester, how often have you been feeling down, depressed or hopeless?': 'dep_q2',
            '3. In a semester, how often have you had trouble falling or staying asleep, or sleeping too much? ': 'dep_q3',
            '4. In a semester, how often have you been feeling tired or having little energy? ': 'dep_q4',
            '5. In a semester, how often have you had poor appetite or overeating? ': 'dep_q5',
            '6. In a semester, how often have you been feeling bad about yourself - or that you are a failure or have let yourself or your family down? ': 'dep_q6',
            '7. In a semester, how often have you been having trouble concentrating on things, such as reading the books or watching television? ': 'dep_q7',
            "8. In a semester, how often have you moved or spoke too slowly for other people to notice? Or you've been moving a lot more than usual because you've been restless? ": 'dep_q8',
            '9. In a semester, how often have you had thoughts that you would be better off dead, or of hurting yourself? ': 'dep_q9',
            'Depression Label': 'depression_label'}, inplace=True)

    # Podział na oddzielne data sety
    print(df.columns.tolist())
    dfAnxiety = df[[
        'anx_q1', 'anx_q2', 'anx_q3', 'anx_q4', 'anx_q5',
        'anx_q6', 'anx_q7', 'anxiety_label']]

    dfStress = df[[
        'str_q1', 'str_q2', 'str_q3', 'str_q4', 'str_q5',
        'str_q6', 'str_q7', 'str_q8', 'str_q9', 'str_q10', 'stress_label']]

    dfDepression = df[[
        'dep_q1', 'dep_q2', 'dep_q3', 'dep_q4', 'dep_q5',
        'dep_q6', 'dep_q7', 'dep_q8', 'dep_q9', 'depression_label']]

    print(dfAnxiety.head())
    print(dfAnxiety.shape)
    print(dfStress.head())
    print(dfStress.shape)
    print(dfDepression.head())
    print(dfDepression.shape)
    if dataToGet == "Anxiety":
        return dfAnxiety
    elif dataToGet == "Depression":
        return dfDepression
    elif dataToGet == "Stress":
        return dfStress
