import pandas as pd
from extract import extract_weather_data
from transform import transform_weather_data
from load import load_to_postgresql

def main():
    lat = 30.063
    lon = 31.250

    # Extract data
    api_data = extract_weather_data(lat, lon)

    if api_data:
        # Transform data
        df_transformed = transform_weather_data(api_data)

        # Load data
        table_name = 'weather'
        load_to_postgresql(df_transformed, table_name)

if __name__ == "__main__":
    main()
