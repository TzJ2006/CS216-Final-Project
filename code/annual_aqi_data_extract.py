import os
import zipfile
import pandas as pd

# Set your folder path here
folder_path = '/Users/tongtongtot/Downloads/annual_aqi'
combined_df = pd.DataFrame()

# Loop through all zip files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.zip') and filename.startswith('annual_aqi_by_cbsa_'):
        zip_path = os.path.join(folder_path, filename)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # There is only one CSV file per ZIP
            for csv_file in zip_ref.namelist():
                if csv_file.endswith('.csv'):
                    with zip_ref.open(csv_file) as file:
                        df = pd.read_csv(file)
                        combined_df = pd.concat([combined_df, df], ignore_index=True)

# Save combined DataFrame to a CSV file
combined_df.to_csv('all_aqi_data.csv', index=False)
print("Combined CSV saved as 'all_aqi_data.csv'")
