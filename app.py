import streamlit as st
import math

def deg_to_rad(deg):
    return deg * math.pi / 180

def rad_to_deg(rad):
    deg = rad * 180 / math.pi
    return deg % 360  # Normalize to 0–360

def sailing_course_calculator(ship_heading, ship_speed, current_heading, current_speed):
    # Convert angles to radians
    ship_rad = deg_to_rad(ship_heading)
    current_rad = deg_to_rad(current_heading)

    # Convert to Cartesian
    ship_x = ship_speed * math.sin(ship_rad)
    ship_y = ship_speed * math.cos(ship_rad)
    current_x = current_speed * math.sin(current_rad)
    current_y = current_speed * math.cos(current_rad)

    # Add vectors
    result_x = ship_x + current_x
    result_y = ship_y + current_y

    # Back to polar
    sog = math.hypot(result_x, result_y)
    cog_rad = math.atan2(result_x, result_y)
    cog = rad_to_deg(cog_rad)

    return sog, cog

# Streamlit App UI
st.title("⛵ Sailing Course Calculator")

ship_heading = st.slider("Ship Heading (°)", 0, 359, 90)
ship_speed = st.slider("Ship Speed (knots)", 0.0, 20.0, 5.0)

current_heading = st.slider("Current Direction (°)", 0, 359, 0)
current_speed = st.slider("Current Speed (knots)", 0.0, 10.0, 2.0)

if st.button("Calculate Course Over Ground"):
    sog, cog = sailing_course_calculator(ship_heading, ship_speed, current_heading, current_speed)
    st.success(f"**Speed Over Ground (SOG):** {sog:.2f} knots")
    st.success(f"**Course Over Ground (COG):** {cog:.2f}°")
