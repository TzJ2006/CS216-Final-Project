import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/Users/tongtongtot/Downloads/annual_aqi/all_aqi_data.csv'
df = pd.read_csv(file_path)

# Set seaborn style
sns.set_theme(style="white")

target_cities = ['Los Angeles-Long Beach-Anaheim, CA', 
                 'San Francisco-Oakland-Hayward, CA', 
                 'New York-Newark-Jersey City, NY-NJ-PA']

# Filter the dataset for the selected cities
filtered_df = df[df['CBSA'].isin(target_cities)]

# We'll re-plot using seaborn's lineplot for each city
for city in target_cities:
    city_data = filtered_df[filtered_df['CBSA'] == city]
    
    # Melt the dataframe to long format for seaborn
    melted = pd.melt(
        city_data,
        id_vars=['Year'],
        value_vars=['Max AQI', '90th Percentile AQI', 'Median AQI'],
        var_name='AQI Metric',
        value_name='AQI Value'
    )
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=melted, x='Year', y='AQI Value', hue='AQI Metric', marker='o')
    plt.title(f'AQI Trends Over Time in {city.split(",")[0]}')
    plt.xlabel('Year')
    plt.ylabel('AQI')
    plt.legend(title='Metric')
    plt.tight_layout()
    # plt.show()
    plt.savefig(f"{city}_aqi_trend.png", dpi=300)
    plt.close()
