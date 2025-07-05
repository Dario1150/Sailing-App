import streamlit as st
import pandas as pd
from datetime import datetime

# App title
st.title("⛵ Sailing Logbook")

# Create empty DataFrame to store log entries
if "log_data" not in st.session_state:
    st.session_state["log_data"] = pd.DataFrame(columns=[
        "Date", "Time", "Location", "Wind", "Course", "Speed", "Engine", "Notes"
    ])

# Entry form
with st.form("log_form"):
    st.subheader("New Log Entry")

    date = st.date_input("Date", value=datetime.now().date())
    time = st.time_input("Time", value=datetime.now().time())
    location = st.text_input("Location (e.g. 45.3N, 14.5E or 'Krk harbor')")
    wind = st.text_input("Wind (e.g. 10kn NW)")
    course = st.text_input("Course (e.g. 120°)")
    speed = st.text_input("Speed (knots)")
    engine = st.selectbox("Engine", ["Off", "On"])
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Add Entry")

    if submitted:
        # Create new row
        new_entry = {
            "Date": date,
            "Time": time,
            "Location": location,
            "Wind": wind,
            "Course": course,
            "Speed": speed,
            "Engine": engine,
            "Notes": notes
        }
        st.session_state["log_data"] = pd.concat(
            [st.session_state["log_data"], pd.DataFrame([new_entry])],
            ignore_index=True
        )
        st.success("✅ Log entry added!")
