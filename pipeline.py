import requests
import pandas as pd
import sqlite3

def extract():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=42.0&longitude=21.43&current_weather=true"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:

        print(f"Error occurred while extracting data: {e}")
        return None

data = extract()

def transform(data):  
    current = data['current_weather']
    weather = {
    
        "temperature": current['temperature'],
        "windspeed": current['windspeed'],
        "winddirection": current['winddirection'],
        "weathercode": current['weathercode'],
        "time": current['time']
}

    df = pd.DataFrame([weather])
    return df

df = transform(data)
print(df)

def load(df):


    DB_NAME = "weather.db"

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            temperature REAL,
            windspeed REAL,
            winddirection REAL,
            weathercode INTEGER,
            time TEXT
        )
''')

    df.to_sql('weather', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

    load(df)