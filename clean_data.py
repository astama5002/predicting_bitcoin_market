import pandas as pd
import requests

# Fetching fresh data directly to avoid manual copy-paste errors
try:
    url = "https://api.alternative.me/fng/?limit=600"
    response = requests.get(url).json()
    df = pd.DataFrame(response['data'])
    
    # Keep it simple: Date and the Value
    df = df[['timestamp', 'value']]
    df.columns = ['Date', 'FnG_Value']
    
    # Save a clean version
    df.to_csv('fear_greed.csv', index=False)
    print("Clean 'fear_greed.csv' created successfully!")
except Exception as e:
    print(f"Error: {e}")

