import pandas as pd
import streamlit as st
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Fetch weather data from the API
def fetch_weather(city, api_key):
    # Adjust the URL for real-time weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        # Calculate wet bulb temperature (simplified calculation)
        wet_bulb = temperature - ((100 - humidity) / 5)  # This is a simplified estimation
        return {'temperature': temperature, 'humidity': humidity, 'wet_bulb': wet_bulb}
    else:
        return None

# Visualization Page
def visualization_page():
    st.title("📊 Historical Data Visualization")

    # Input for date and city
    date_input = st.date_input("Select Date:", datetime.now())
    city_input = st.text_input("Enter City Name:", placeholder='City name')
    api_key = "add7ad83856484eceb2aec51ff88c449"  # Your OpenWeatherMap API key

    if st.button("Get Weather Info"):
        if city_input:
            # Format date to string (though OpenWeatherMap API doesn't support historical by date in free tier)
            selected_date = date_input.strftime("%Y-%m-%d")
            weather_data = fetch_weather(city_input, api_key)

            if weather_data:
                # Create a DataFrame to store the fetched data
                data = {
                    'Date': [selected_date],
                    'Temperature': [weather_data['temperature']],
                    'Humidity': [weather_data['humidity']],
                    'Wet Bulb': [weather_data['wet_bulb']]
                }
                df = pd.DataFrame(data)

                st.write("### 🗓️ Historical Weather Data")
                st.write(df)

                # Plotting historical temperature and wet bulb temperature
                st.write("### 🌡️ Temperature vs Wet Bulb Temperature")
                fig, ax = plt.subplots()

                # Create a scatter plot for clearer visualization
                ax.scatter(df['Date'], df['Temperature'], label='Temperature', color='blue', marker='o')
                ax.scatter(df['Date'], df['Wet Bulb'], label='Wet Bulb Temperature', color='red', marker='s')

                # Set axis labels
                ax.set_xlabel('Date')
                ax.set_ylabel('Temperature (°C)')
                
                # Customize title and legend
                ax.set_title('Temperature vs Wet Bulb Temperature')
                ax.legend()

                # Display the plot in Streamlit
                st.pyplot(fig)
            else:
                st.error("Weather data not found. Please try again with a valid city.")
        else:
            st.error("Please enter a city name.")

# Run the visualization page function
visualization_page()
