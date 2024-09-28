import streamlit as st
import requests
import math

# Function to fetch weather data
def fetch_weather_data(city):
    api_key = 'add7ad83856484eceb2aec51ff88c449'  # Your API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
        }
    else:
        return None

# Function to calculate wet bulb temperature
def wet_bulb_temperature(temp, humidity):
    wet_temp = temp * math.atan(0.151977 * math.sqrt(humidity + 8.313659)) + \
               math.atan(temp + humidity) - math.atan(humidity - 1.676331) + \
               0.00391838 * ((humidity) ** (3/2)) * math.atan(0.023101 * humidity) - \
               4.686035
    return wet_temp

# Streamlit app starts here
st.title("🌡️ Heat Stress Alerts")

# User input for city name
city = st.text_input("Enter City Name:", placeholder='City name')

if st.button("Get Weather Info"):
    if city:
        weather_info = fetch_weather_data(city)
        
        if weather_info:
            temp = weather_info['temperature']
            humidity = weather_info['humidity']
            wet_temp = wet_bulb_temperature(temp, humidity)

            st.write(f"**Wet Bulb Temperature for {city}:** {wet_temp:.2f}°C")
            
            # Alerts based on wet bulb temperature
            if wet_temp > 35:
                st.warning("⚠️ Extreme danger! Wet Bulb Temperature exceeds 35°C.")
                st.subheader("Health Tips for Extreme Heat ⚠️")
                st.write("1. **Stay Hydrated**: Drink plenty of water throughout the day. 💧")
                st.write("2. **Wear Appropriate Clothing**: Loose, lightweight clothing is best. 👕")
                st.write("3. **Limit Outdoor Activities**: Avoid strenuous activities during peak heat. ☀️")
            elif wet_temp > 32:
                st.warning("⚠️ Critical heat stress! Wet Bulb Temperature is above 32°C.")
                st.subheader("Health Tips for High Heat Stress 🌞")
                st.write("1. **Stay Hydrated**: Drink water regularly. 💧")
                st.write("2. **Wear Light Clothing**: Choose breathable, light-colored clothing. 👕")
                st.write("3. **Take Breaks**: Rest in the shade if outdoors. 🌳")
            elif wet_temp > 30:
                st.warning("⚠️ High heat stress risk. Stay hydrated and avoid outdoor activities.")
                st.write("1. **Monitor Your Activity**: Limit exposure to heat. 🏃")
                st.write("2. **Eat Light Meals**: Consume lighter foods. 🍽️")
            else:
                st.success("🌈 Conditions are safe. Enjoy your day!")
                st.subheader("SOME HEALTH TIPS")
                st.write("1.Stay Hydrated 💧: Encourage drinking plenty of water throughout the day to maintain hydration levels.")
                st.write("2.Enjoy Outdoor Activities ☀️: Conditions are generally safe for outdoor activities; consider taking advantage of the weather.")
                st.write("3.Wear Light Clothing 👕: Suggest wearing breathable and light clothing to stay comfortable.")
                st.write("4.Plan Activities Wisely 🗓️: If planning outdoor activities, try to do them in the cooler parts of the day, such as early morning or late evening.")
                st.write("5.Monitor Conditions 📱: Remind users to keep an eye on the weather forecast for any sudden changes, especially during heatwaves.")                 
                
            # User custom alerts
            custom_threshold = st.slider("Set Custom Alert Threshold (°C):", min_value=20, max_value=45, value=35)
            if wet_temp > custom_threshold:
                st.warning(f"⚠️ Custom Alert! Wet Bulb Temperature exceeds your set threshold of {custom_threshold}°C.")

        else:
            st.error("City not found. Please try again.")
    else:
        st.error("Please enter a city name.")

# Additional educational resources
st.markdown("### Learn More About Heat Stress:")
st.write("Understanding heat stress is vital for safety during hot weather. "
         "Visit [CDC - Extreme Heat](https://www.cdc.gov/disasters/extremeheat/index.html) for more information.")

# Adding a footer with contact information or additional resources
st.markdown("#### Contact Us for More Information")
st.write("If you have any questions, feel free to reach out!")
