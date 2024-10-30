import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor, TabularDataset # pip install autogluon --no-deps


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

    #Podział na oddzielne data sety
    print(df.columns.tolist())
    dfAnxiety = df[[
        '1. Age', '2. Gender', '4. Department', '5. Academic Year',
        '7. Did you receive a waiver or scholarship at your university?',
        '1. In a semester, how often you felt nervous, anxious or on edge due to academic pressure? ',
        '2. In a semester, how often have you been unable to stop worrying about your academic affairs? ',
        '3. In a semester, how often have you had trouble relaxing due to academic pressure? ',
        '4. In a semester, how often have you been easily annoyed or irritated because of academic pressure?',
        '5. In a semester, how often have you worried too much about academic affairs? ',
        '6. In a semester, how often have you been so restless due to academic pressure that it is hard to sit still?',
        '7. In a semester, how often have you felt afraid, as if something awful might happen?', 'Anxiety Label']]

    dfStress = df[[
        '1. Age', '2. Gender', '4. Department', '5. Academic Year',
        '7. Did you receive a waiver or scholarship at your university?',
        '1. In a semester, how often have you felt upset due to something that happened in your academic affairs? ',
        '2. In a semester, how often you felt as if you were unable to control important things in your academic affairs?',
        '3. In a semester, how often you felt nervous and stressed because of academic pressure? ',
        ('4. In a semester, how often you felt as if you could not cope with all the mandatory academic activities? (e.g, '
        'assignments, quiz, exams) '),
        '5. In a semester, how often you felt confident about your ability to handle your academic / university problems?',
        '6. In a semester, how often you felt as if things in your academic life is going on your way? ',
        '7. In a semester, how often are you able to control irritations in your academic / university affairs? ',
        '8. In a semester, how often you felt as if your academic performance was on top?',
        '9. In a semester, how often you got angered due to bad performance or low grades that is beyond your control? ',
        ('10. In a semester, how often you felt as if academic difficulties are piling up so high that you could not '
        'overcome them? '), 'Stress Label']]

    dfDepression = df[[
        '1. Age', '2. Gender', '4. Department', '5. Academic Year', ('7. Did you receive a waiver or scholarship at your '
        'university?'), '1. In a semester, how often have you had little interest or pleasure in doing things?',
        '2. In a semester, how often have you been feeling down, depressed or hopeless?',
        '3. In a semester, how often have you had trouble falling or staying asleep, or sleeping too much? ',
        '4. In a semester, how often have you been feeling tired or having little energy? ',
        '5. In a semester, how often have you had poor appetite or overeating? ',
        ('6. In a semester, how often have you been feeling bad about yourself - or that you are a failure or have let '
        'yourself or your family down? '), ('7. In a semester, how often have you been having trouble concentrating on '
        'things, such as reading the books or watching television? '), ("8. In a semester, how often have you moved or spoke "
        "too slowly for other people to notice? Or you've been moving a lot more than usual because you've been restless? ")
        , '9. In a semester, how often have you had thoughts that you would be better off dead, or of hurting yourself? ',
        'Depression Label']]

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


def model(predictedLabel, df, savePath):
    print("Predicting:", predictedLabel)
    trainData, testData = train_test_split(df, test_size=0.3, random_state=42)
    trainDataTabular = TabularDataset(trainData)
    print(trainDataTabular.head())
    print(trainData[predictedLabel].describe())

    predictor = TabularPredictor(label=predictedLabel, path=savePath).fit(trainDataTabular, presets='medium_quality')
    predictor.predict(TabularDataset(testData))

    lds = predictor.leaderboard(testData)
    print(lds)
    print(predictor.evaluate(testData))


def anxiety_model():
    dfAnxiety = data_preparation("Anxiety")
    predictedLabel = "Anxiety Label"
    model(predictedLabel, dfAnxiety, "AutogluonModels/Anxiety")


def depression_model():
    dfDepression = data_preparation("Depression")
    predictedLabel = "Depression Label"
    model(predictedLabel, dfDepression, "AutogluonModels/Depression")


def stress_model():
    dfStress = data_preparation("Stress")
    predictedLabel = "Stress Label"
    model(predictedLabel, dfStress, "AutogluonModels/Stress")


if __name__ == "__main__":
    anxiety_model()
    depression_model()
    stress_model()
