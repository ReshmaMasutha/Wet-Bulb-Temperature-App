
import streamlit as st
import math

def wet_bulb_temperature(temp, humidity):
    wet_temp = temp * math.atan(0.151977 * math.sqrt(humidity + 8.313659)) + \
                math.atan(temp + humidity) - math.atan(humidity - 1.676331) + \
                0.00391838 * (humidity ** 1.5) * math.atan(0.023101 * humidity) - \
                4.686035
    return wet_temp

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
