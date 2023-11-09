#Task 1

import time

def calculate_execution_time(func):
    
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper


@calculate_execution_time
def add(a: int, b: int) -> int:
    return a + b


add_result = add(1, 2)
add_result


# Task 2
import os
from dotenv import load_dotenv

load_dotenv()  

import requests


API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_forecast(city_name):
    """ Get weather forecast information for the given city name. """
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        
        data = response.json()
        
        first_forecast = data['list'][0]
        temp = first_forecast['main']['temp']
        weather_description = first_forecast['weather'][0]['description']
        return temp, weather_description
    else:
        print("Error:", response.status_code, response.text)
        return None, None

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    temperature, weather_description = get_forecast(city_name)
    
    if temperature is not None and weather_description is not None:
        print(f"Forecast for {city_name}: {temperature}°C, {weather_description}")
    else:
        print("Failed to get the weather forecast data")
