import requests
import pandas as pd

try:
    # 1. Get 600 days of clean data from the source
    print("Fetching fresh data...")
    url = "https://api.alternative.me/fng/?limit=600"
    r = requests.get(url)
    data = r.json()['data']

    # 2. Create the table
    df = pd.DataFrame(data)
    
    # 3. Keep only the columns your app needs
    # timestamp and value (which becomes FnG_Value)
    df = df[['timestamp', 'value']]
    df.columns = ['Date', 'FnG_Value']
    
    # 4. Save it with NO extra spaces or weird characters
    df.to_csv('fear_greed.csv', index=False)
    
    print("--- SUCCESS! ---")
    print("Your 'fear_greed.csv' is now fixed and has 600 rows.")
except Exception as e:
    print(f"Error: {e}")

