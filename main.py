import kagglehub
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset
import os

# Download latest version
path = kagglehub.dataset_download("giovamata/airlinedelaycauses")

file_path = os.path.join(path, "DelayedFlights.csv")
df = pd.read_csv(file_path)
reference = df.sample(10000, random_state=42)


current = reference.copy()
current['WeatherDelay'] = 2.5
current['CarrierDelay']= 2.0
current['NASDelay'] += 50


report = Report([
    DataDriftPreset(),
])

my_eval = report.run(current, reference)

report.run(reference_data=reference, current_data=current).save_html("result.html")



