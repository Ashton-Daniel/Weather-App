#Weather App 2
# Import the json and requests modules
import json
from pip._vendor import requests

#API Key
api_key = 'fc68bc547ba57d7677f8482110cb5d8e'

# While loop to keep asking for a location
while True:
    # Ask user for a location
    location = input("Enter a location: ") # <-- get location from user

    # Function to get weather
    def get_weather(location): 
        # API endpoint for current weather
        current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

        # Make a GET request to the API
        response = requests.get(current_weather_url)

        # Convert the response to JSON
        weather_data = response.json()

        # Extract the weather description from the JSON
        description = weather_data['weather'][0]['description']

        # Extract the temperature from the JSON
        temperature = weather_data['main']['temp']

        # Print the weather description and temperature
        print(f"The weather in {location} is {description} with a temperature of {temperature}°C")

    # Call the function and pass the location
    get_weather(location)
