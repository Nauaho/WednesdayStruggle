from autogluon.tabular import TabularPredictor, TabularDataset
from datetime import date
import pandas as pd

predictor = TabularPredictor.load("AutogluonModels/ag-20241022_165723")
                                                        # Check with:
latitude = float(input('Enter latitude: '))             # 47
longitude = float(input('Enter longitude: '))           # -123
country = str(input('Enter country: '))                 # us
observation_month = int(input('Select Month: '))        # 10
observation_month_day = int(input('Select Day: '))      # 22

observation_date = date(2024, observation_month, observation_month_day)
for_prediction = {
    "datetime": observation_date,
    "country": country,
    "latitude": latitude,
    "longitude": longitude
}
#TODO fix this :/
for_prediction = pd.DataFrame(for_prediction)
result_seconds = predictor.predict(for_prediction)

print(f"Predicted duration is {result_seconds} seconds.")

#('float', []): 2                 | ['latitude', 'longitude']
#('object', []): 1                | ['country']
#('object', ['datetime_as_object']): 1 | ['datetime']

