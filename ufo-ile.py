import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor, TabularDataset

# -----------------------
# Dataset:
# https://www.kaggle.com/datasets/NUFORC/ufo-sightings/data
#
# -----------------------

# Download latest version
path = kagglehub.dataset_download("NUFORC/ufo-sightings")
path = path+"/scrubbed.csv"

print("Path to dataset files:", path)

data = pd.read_csv(path)
# print(list(data.columns))

data = data.drop(columns=['city', 'state', 'comments', 'duration (hours/min)', 'date posted', 'shape'])
data = data.dropna(axis='index', how='any')
data = data.rename(columns={'longitude ': 'longitude'})
data.loc[data["duration (seconds)"] == "2`"] = 120.0

print(list(data.columns))
print(data)

predicted_label="duration (seconds)"
# y = data.pop(predicted_label)    # Designate a value(column) for prediction and remove it from the dataset
data_train, data_test = train_test_split(data, test_size=0.2, random_state=42)

train_data_tabular = TabularDataset(data_train)
train_data_tabular['latitude'] = train_data_tabular['latitude'].astype("float")
train_data_tabular['longitude'] = train_data_tabular['longitude'].astype("float")
train_data_tabular[predicted_label] = train_data_tabular[predicted_label].astype("float")

predictor = TabularPredictor(label=predicted_label, problem_type='regression').fit(train_data_tabular, presets='medium_quality')
predictor.predict(TabularDataset(data_test))

lds = predictor.leaderboard()
print(lds)


