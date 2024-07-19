import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access API_KEY
api_key = os.getenv('API_KEY')

def extract_weather_data(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error in API Request: {response.status_code}")
        return None
