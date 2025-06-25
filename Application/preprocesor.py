import re
import pandas as pd

def Preprocessing(data):
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}\s[APMapm]{2})\s-\s([^:]+):\s(.*)'
    matches = re.findall(pattern, data)

    df = pd.DataFrame(matches, columns=['Date', 'Time', 'user', 'Message'])

    # Use correct format for 2-digit years
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%m/%d/%y %I:%M %p', errors='coerce')

    # Extract datetime features
    df['year'] = df['DateTime'].dt.year
    df['month'] = df['DateTime'].dt.month
    df['day'] = df['DateTime'].dt.day

    return df
