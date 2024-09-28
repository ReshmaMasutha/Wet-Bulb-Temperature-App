import streamlit as st

# Title of the app
st.title("🌡️ Wet Bulb Temperature")

# Section 1: What is Wet Bulb Temperature?
st.header("1. What is Wet Bulb Temperature? 🌡️")
st.markdown("""
**Definition**: Wet Bulb Temperature (WBT) is the lowest temperature air can achieve through the process of evaporation, combining the effects of both heat and humidity.  
**Key Concept**: Unlike regular temperature, WBT reflects the capacity of the air to hold moisture, making it an important measure for understanding heat stress in humid conditions.
""")

# Section 2: Why Wet Bulb Temperature Matters?
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
