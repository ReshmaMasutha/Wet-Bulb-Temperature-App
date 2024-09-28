import streamlit as st
import requests

# Function to fetch weather data
def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return {
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "description": data['weather'][0]['description'],
            "wind_speed": data['wind']['speed']
        }
    else:
        st.error("City not found. Please enter a valid city name.")
        return None

# Input city name
st.title("Weather Information")
city = st.text_input("Enter the city name:")

# If city is entered, display weather data
if city:
    api_key = "add7ad83856484eceb2aec51ff88c449"  # Your OpenWeatherMap API key
    weather_info = fetch_weather(city, api_key)
    if weather_info:
        st.write(f"**City:** {city}")
        st.write(f"**Temperature:** {weather_info['temperature']}°C")
        st.write(f"**Humidity:** {weather_info['humidity']}%")
        st.write(f"**Weather:** {weather_info['description']}")
        st.write(f"**Wind Speed:** {weather_info['wind_speed']} m/s")
