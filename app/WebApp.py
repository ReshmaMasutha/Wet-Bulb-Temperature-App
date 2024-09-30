import streamlit as st
import math
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Wet Bulb Temperature Calculation Function
def wet_bulb_temperature(temp, humidity):
    wet_temp = temp * math.atan(0.151977 * math.sqrt(humidity + 8.313659)) + \
               math.atan(temp + humidity) - math.atan(humidity - 1.676331) + \
               0.00391838 * (humidity ** 1.5) * math.atan(0.023101 * humidity) - \
               4.686035
    return wet_temp

def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    api_key = "add7ad83856484eceb2aec51ff88c449" 
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
        }
    return None

# Function to display the home page
def home_page():
    st.title("🌡️ Wet Bulb Temperature")
    st.header("1. What is Wet Bulb Temperature? 🌡️")
    st.markdown("""
    **Definition**: Wet Bulb Temperature (WBT) is the lowest temperature air can achieve through the process of evaporation, combining the effects of both heat and humidity.  
    **Key Concept**: Unlike regular temperature, WBT reflects the capacity of the air to hold moisture, making it an important measure for understanding heat stress in humid conditions.
    """)
#Section 2:why wet builb temp matters!
    st.header("2. Why Wet Bulb Temperature Matters? ❗")
    st.markdown("""
- **Heat Stress Indicator**: WBT is crucial for predicting the risk of heat stress, particularly in environments with high humidity where the human body struggles to cool itself.  
- **Human Survival Threshold**: WBT exceeding **35°C** is recognized as the upper survivability limit for humans in prolonged exposure. Above this threshold, the body cannot release enough heat, leading to dangerous health conditions.  
- **Workplace and Outdoor Safety**: WBT provides essential information for protecting outdoor workers, athletes, and military personnel from heat-related illnesses like heat stroke.
""")

# Section 3: Real-World Applications of Wet Bulb Temperature
    st.header("3. Real-World Applications of Wet Bulb Temperature 🌍")
    st.markdown("""
- **Climate Change Monitoring**: WBT is an important tool for climate scientists to assess the increasing risks posed by heatwaves in a warming world.  
- **Disaster Preparedness**: By understanding regions prone to extreme WBT, governments and organizations can implement safety measures during heat waves and reduce the risk of heat-related mortality.  
- **Public Health**: WBT informs public health advisories, especially for vulnerable populations such as the elderly, children, and those with pre-existing health conditions.
""")

# Section 4: Effects of Wet Bulb Temperature on Human Health
    st.header("4. Effects of Wet Bulb Temperature on Human Health ⚠️")
    st.markdown("""
- **Heat Stress**: As WBT rises, sweat evaporation becomes less efficient, limiting the body's ability to cool down. When WBT reaches **35°C**, this cooling mechanism fails.  
- **Fatal Heat Conditions**: Sustained exposure to a WBT above **35°C** leads to potentially fatal heatstroke, especially without air conditioning or cooling methods.  
- **Extreme Caution**: Even WBT values between **30°C and 35°C** can cause severe discomfort and health risks, such as dehydration, heat cramps, and fatigue.
""")

# Section 5: Importance of Wet Bulb Temperature in Everyday Life
    st.header("5. Importance of Wet Bulb Temperature in Everyday Life 🌱")
    st.markdown("""
- **Weather Monitoring**: WBT can be a more accurate reflection of dangerous conditions than regular temperature, making it critical for weather forecasting during heatwaves.  
- **Agriculture and Animal Health**: Farmers use WBT to assess how livestock and crops may be affected by heat and humidity, ensuring proper safety measures are taken to avoid heat stress.  
- **Energy Efficiency**: Understanding WBT helps in designing efficient cooling systems in buildings, reducing energy consumption in high-humidity areas.
""")

# Section 6: Unique and Lesser-Known Aspects of Wet Bulb Temperature
    st.header("6. Unique and Lesser-Known Aspects of Wet Bulb Temperature 💡")
    st.markdown("""
- **WBT and Evaporative Cooling**: Wet bulb temperature is used in evaporative cooling technologies, which are highly efficient in hot, dry climates. This process leverages the cooling effect of water evaporation to reduce temperatures in buildings and machinery.  
- **Microclimates**: WBT can vary significantly within small geographic areas, particularly between urban and rural environments, due to factors like vegetation, water bodies, and infrastructure. This concept of "urban heat islands" showcases how cities experience higher WBT compared to surrounding rural areas.  
- **Impact on Aviation**: High WBT affects aircraft performance. In hot and humid conditions, planes may require longer runways for takeoff due to the air density changes caused by high WBT.
""")

# Section 7: How the Wet Bulb Temperature App Works
    st.header("7. How the Wet Bulb Temperature App Works 📱")
    st.markdown("""
- **Weather Information for Cities**: Users can input a city name to get real-time weather data, including temperature, humidity, and WBT.  
- **Wet Bulb Temperature Calculator**: Allows users to calculate WBT using current temperature and humidity data.  
- **Historical Data Visualization**: Users can view graphs of historical WBT trends, helping them understand the changing climate patterns in their area.  
- **Health and Safety Alerts**: The app provides warnings when WBT exceeds dangerous levels (e.g., **35°C**), encouraging users to take precautions.
""")


# WET CALCULATOR PAGE
def calculator_page():
    st.title("Wet Bulb Temperature Calculator")
    temperature = st.number_input("Enter the temperature (°C):", min_value=-30.0, max_value=50.0, step=0.1)
    humidity = st.slider("Select the relative humidity (%):", 0, 100, step=1)
    
    if st.button("Calculate Wet Bulb Temperature"):
        wet_temp = wet_bulb_temperature(temperature, humidity)
        st.write(f"**Wet Bulb Temperature:** {wet_temp:.2f}°C")
        
        if wet_temp > 35:
            st.error("Dangerous Wet Bulb Temperature! Take caution.")
        elif wet_temp > 30:
            st.warning("High Wet Bulb Temperature. Be careful.")
        else:
            st.success("Wet Bulb Temperature is within safe limits.")


# WEATHER INFORMATION PAGE
def weather_info_page():
    st.title("Weather Information")
    city = st.text_input("Enter the city name:")
    
    # If city is entered, display weather data
    if city:
        api_key = "add7ad83856484eceb2aec51ff88c449"  # Using Streamlit's secrets management
        weather_info = fetch_weather(city, api_key)

        if weather_info:
            st.write(f"City: {city}")
            st.write(f"**Temperature:** {weather_info['temperature']}°C")
            st.write(f"**Humidity:** {weather_info['humidity']}%")
            st.write(f"**Wet Bulb Temperature:** {weather_info['wet_bulb']}°C")
        else:
            st.error("City not found. Please enter a valid city name.")
            
# Function to fetch weather data
def fetch_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        # Check if the city was found (status code 200)
        if response.status_code == 200:
            data = response.json()
            
            # Extract temperature and humidity
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            
            # Calculate wet bulb temperature using an approximation formula
            wet_bulb = calculate_wet_bulb(temperature, humidity)
            
            return {'temperature': temperature, 'humidity': humidity, 'wet_bulb': wet_bulb}
        elif response.status_code == 404:
            # City not found
            return None
        else:
            st.error(f"Error: Unable to retrieve data (status code: {response.status_code})")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None




# Function to calculate wet bulb temperature
def calculate_wet_bulb(temp, humidity):
    tw = temp * math.atan(0.151977 * math.sqrt(humidity + 8.313659)) \
         + math.atan(temp + humidity) \
         - math.atan(humidity - 1.676331) \
         + 0.00391838 * (humidity ** 1.5) * math.atan(0.023101 * humidity) \
         - 4.686035
    return round(tw, 2)

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


# HEAT STRESS ALERTS PAGE
def alerts_page():
    st.title("🌡️ Heat Stress Alerts")
    
    # User input for city name
    city = st.text_input("Enter City Name:", placeholder='City name')
    
    if st.button("Get Weather Info"):
        if city:
            api_key = "add7ad83856484eceb2aec51ff88c449"  # Your OpenWeatherMap API key
            weather_info = fetch_weather(city, api_key)
            
            if weather_info:
                temp = weather_info['temperature']
                humidity = weather_info['humidity']
                wet_temp = wet_bulb_temperature(temp, humidity)

                st.write(f"** 🌡️ Wet Bulb Temperature for {city}:** {wet_temp:.2f}°C")
                
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
                    st.write("1. Stay Hydrated 💧: Encourage drinking plenty of water throughout the day to maintain hydration levels.")
                    st.write("2. Enjoy Outdoor Activities ☀️: Conditions are generally safe for outdoor activities; consider taking advantage of the weather.")
                    st.write("3. Wear Light Clothing 👕: Suggest wearing breathable and light clothing to stay comfortable.")
                    st.write("4. Plan Activities Wisely 🗓️: If planning outdoor activities, try to do them in the cooler parts of the day, such as early morning or late evening.")
                    st.write("5. Monitor Conditions 📱: Remind users to keep an eye on the weather forecast for any sudden changes, especially during heatwaves.")                 
                
                # User custom alerts
                custom_threshold = st.slider("Set Custom Alert Threshold (°C):", min_value=20, max_value=45, value=35)
                if wet_temp > custom_threshold:
                    st.warning(f"⚠️ Custom Alert! Wet Bulb Temperature exceeds your set threshold of {custom_threshold}°C.")
            else:
                st.error("City not found. Please try again.")
        else:
            st.error("Please enter a city name.")

# FEEDBACK FORM
def feedback_page():
    st.title("Feedback Form")
    st.write("We value your feedback! Please fill out the form below to provide your comments and suggestions.")
    
    # Replace with your Google Form link
    google_form_url = "https://forms.gle/BbVVTY3UGYgZCwDm9"
    
    # Embed Google Form in Streamlit
    st.markdown(f'<iframe src="{google_form_url}" width="640" height="700" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', unsafe_allow_html=True)
# SLIDEBAR FOR NAVIGATION 
st.sidebar.title("Navigation")
# GitHub repository link
github_url = "https://github.com/reshmamasutha/wet-bulb-temperature-app"

# Display the clickable GitHub icon in the center of the page
st.sidebar.markdown(f"""
    <a href="{github_url}" target="_blank">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width:30px;">
    </a>
    """, unsafe_allow_html=True)


page = st.sidebar.radio("Go to", ["🏠 Homepage", "🧮 Wet Bulb Temperature Calculator", "🌤️ Weather Info For Cities", "📊 Historical Data Visualisation", "🔥 Heat Stress Alert", "📝 Feedback"])

if page == "🏠 Homepage":
    home_page()
elif page == "🧮 Wet Bulb Temperature Calculator":
    calculator_page()
elif page == "🌤️ Weather Info For Cities":
    weather_info_page()
elif page == "📊 Historical Data Visualisation":
    visualization_page()
elif page == "🔥 Heat Stress Alert":
    alerts_page()
elif page == "📝 Feedback":
    feedback_page()
    
