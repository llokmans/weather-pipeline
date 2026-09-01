# Weather Data Pipeline

An ETL pipeline that fetches live weather data, transforms it, and stores it in a database.

## What it does
- **Extract**: fetches current weather from the Open-Meteo API
- **Transform**: parses the nested JSON into a clean structured format with pandas
- **Load**: stores each reading in a SQLite database, appending over time

## Tech
Python · requests · pandas · sqlite3

## How to run
​```
pip install requests pandas
python pipeline.py
​```
Each run fetches the current weather and adds a new row to the database.