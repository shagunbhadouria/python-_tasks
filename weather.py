import time
import requests

def get_weather(city_name, api_key):
    print(f"\nFetching weather data for {city_name}...")
    time.sleep(1)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        display_weather_data(data)
    else:
        print("\nError: Could not retrieve weather data.\nCheck the city name or API key and try again.")

def display_weather_data(data):
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    condition = data['weather'][0]['description']

    print("\n--- Weather Report ---")
    print(f"Location: {city}, {country}")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Condition: {condition.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Wind Speed: {wind_speed} m/s")
    print("------------------------\n")

if __name__ == "__main__":
    print("Welcome to the Basic Weather App")
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(city, API_KEY)
    print("Thank you for using the Weather App!")
