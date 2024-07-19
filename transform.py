import pandas as pd
from datetime import datetime

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def transform_weather_data(api_data):
    weather_data = []
    for hour in api_data['list']:
        date_time = datetime.utcfromtimestamp(hour['dt']).strftime('%Y-%m-%d %H:%M:%S')
        temp = kelvin_to_celsius(hour['main']['temp'])
        feels_like = kelvin_to_celsius(hour['main']['feels_like'])
        pressure = hour['main']['pressure']
        humidity = hour['main']['humidity']
        weather_main = hour['weather'][0]['main']
        weather_description = hour['weather'][0]['description']
        wind_speed = hour['wind']['speed']
        wind_description = hour['wind']['deg']
        cloudiness = hour['clouds']['all']
        rain_volume = hour.get('rain', {}).get('3h', 0)
        snow_volume = hour.get('snow', {}).get('3h', 0)

        weather_data.append({
            'date_time': date_time,
            'temp': temp,
            'feels_like': feels_like,
            'pressure': pressure,
            'humidity': humidity,
            'weather_main': weather_main,
            'weather_description': weather_description,
            'wind_speed': wind_speed,
            'wind_description': wind_description,
            'cloudiness': cloudiness,
            'rain_volume': rain_volume,
            'snow_volume': snow_volume
        })

    return pd.DataFrame(weather_data)
