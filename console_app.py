from autogluon.tabular import TabularPredictor
import pandas as pd

predictor = TabularPredictor.load("AutogluonModels/ag-20241022_165723")
                                                        # Example data:
latitude = float(input('Enter latitude: '))             # 47
longitude = float(input('Enter longitude: '))           # -123
country = str(input('Enter country: '))                 # us
observation_date = str(input('Input date: '))           # 10/23/2024

for_prediction = {
    "datetime": observation_date,
    "country": country,
    "latitude": [latitude],
    "longitude": [longitude]
}

for_prediction = pd.DataFrame(for_prediction)
print(f"Predicting on: \n{for_prediction}")

result_seconds_pdSeries = predictor.predict(for_prediction)
print(f"Predicted duration is {result_seconds_pdSeries.values[0]:.2f} seconds.")

# Recommend launching this script with -i switch like "python3 -i console_app.py" to keep the interpreter context.
