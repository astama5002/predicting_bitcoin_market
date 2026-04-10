import requests
import pandas as pd

# Fetch the last 600 days to be safe
response = requests.get("https://api.alternative.me/fng/?limit=600")
data = response.json()['data']

# Create the DataFrame
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

# Select only the date and the score
df = df[['timestamp', 'value']]
df.columns = ['date', 'fng_score']

# Save as fear_greed.csv in your project folder
df.to_csv('fear_greed.csv', index=False)
print("Dataset upgraded: fear_greed.csv now has 600 rows.")

