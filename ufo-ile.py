import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split

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

data = data.drop(columns=['city', 'state', 'comments', 'duration (hours/min)', 'date posted'])
data = data.dropna(axis='index', how='any')

print(list(data.columns))
print(data)

y = data.pop("duration")    # Designate a value(column) for prediction and remove it from the dataset
X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.2, random_state=42)

#TODO: create and train a model