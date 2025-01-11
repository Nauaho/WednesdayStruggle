import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor, TabularDataset # pip install autogluon --no-deps
from data_prep import data_preparation


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
    predictedLabel = "anxiety_label"
    model(predictedLabel, dfAnxiety, "AutogluonModels/Anxiety")


def depression_model():
    dfDepression = data_preparation("Depression")
    predictedLabel = "depression_label"
    model(predictedLabel, dfDepression, "AutogluonModels/Depression")


def stress_model():
    dfStress = data_preparation("Stress")
    predictedLabel = "stress_label"
    model(predictedLabel, dfStress, "AutogluonModels/Stress")


if __name__ == "__main__":
    anxiety_model()
    depression_model()
    stress_model()
