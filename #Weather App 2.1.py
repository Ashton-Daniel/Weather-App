# Weather App 2.0
# Import the json, requests and os modules
import json
from pip._vendor import requests
import os

#API Key
api_key = 'fc68bc547ba57d7677f8482110cb5d8e'

# clear the terminal
os.system("cls")

# Function to get weather
def get_weather():
    # Define a loop variable
    loop = True
    while loop == True:
        print("")
        # Ask user for a location
        location = input("Enter a location (type 'help' for a command list): \n").lower()
        
        # If the user wants to see a list of commands
        if location == "help":
            print("")
            print("Type 'back' to go back to the main menu")
            print("Type 'clear' to clear the terminal")
            print("Type 'quit' to exit the program")
            print("Type a city to get the weather of that city")
            print("")
            continue

        # If the user wants to go back to the main menu
        if location == "back":
            loop = False
            return
        
        # If the user wants to clear the terminal
        if location == "clear":
            os.system("cls")
            continue
        
        # If the user wants to quit the program
        if location == "quit":
            break

        # Capitalize the first letter of the location and lowercase the rest of the letters
        location = location.capitalize()

        # API endpoint for current weather
        current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

        # Make a GET request to the API
        response = requests.get(current_weather_url)

        # Convert the response to JSON
        weather_data = response.json()

        # Extract the weather description from the JSON
        # Use a try-except block to handle KeyError
        try:
            description = weather_data['weather'][0]['description']
            
        except KeyError:
            print("Location not found")
            return

        # Extract the temperature from the JSON
        temperature = weather_data['main']['temp']

        # Print the weather description and temperature
        print("")
        print(f"The weather in {location} is {description} with a temperature of {temperature}°C")

        # Record the locations that the user has input into a file
        locations_file = open("Location.txt", "a")
        locations_file.write(location + "\n")
        locations_file.close()
        # print("Location has been recorded")

# Function to get the location history
def get_location():
    print("")
    print("Location History:")
    locations_file = open("Location.txt", "r")
    print(locations_file.read())
    locations_file.close()

# Function to delete the location history
def delete_location():
    locations_file = open("Location.txt", "w")
    locations_file.write("")
    locations_file.close()
    print("")
    print("Locations have been deleted")

# Funtion that asks whether you want to see locations or delete the locations
def location_task():
    # Define a loop variable
    loop = True
    while loop == True:
        # Ask the user what they want to do with their location history
        print("")
        location_task = input("What would you like to do with your location history? (type 'help' for a list of commands at any time) \n").lower()
        
        # If the user wants to read the locations
        if location_task == "read":
            get_location()
            continue
        
        # If the user wants to delete the locations
        elif location_task == "delete":
            delete_location()
            continue

        # If the user wants to clear the terminal
        elif location_task == "clear":
            os.system("cls")
            continue

        # If the user wants to help
        elif location_task == "help":
            print("")
            print("read: to see the locations you have searched for")
            print("delete: to delete the locations you have searched for")
            print("back: to go back to the main menu")
            print("clear: to clear the terminal")
            continue
        
        # If the user wants to go back to the main menu
        elif location_task == "back":
            loop = False
            return
        
        # If the user inputs an invalid command
        else:
            print("Invalid input. Please type 'help' for a list of commands")
            continue

# While loop to keep the program running
while True:
    loop = True
    print("")
    current_Task = input("What would you like to do? (type 'help' for a list of commands at any time): \n").lower()

    # If the user wants to quit the program
    if current_Task == "quit":
        break
    elif current_Task == "location history" or current_Task == "locations":
        # Call the location_task function
        location_task()
        continue
    elif current_Task == "weather":
        # Call the get_weather function
        get_weather()
        continue
    elif current_Task == "help":
        print("")
        print("Type 'weather' to get the weather of a location")
        print("Type 'location history' to get the locations you have searched for")
        print("Type 'quit' to exit the program")
        print("Type 'clear' to clear the terminal")
        print("")
        continue
    elif current_Task == "clear":
        os.system("cls")
        continue
    else:
        print("Invalid input. Please type 'help' for a list of commands")
        continue
