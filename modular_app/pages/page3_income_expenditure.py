import streamlit as st
import pandas as pd
from datetime import datetime

def get_user_country():
    countries = ['Singapore', 'United States', 'Canada', 'Australia', 'United Kingdom', 'Germany', 
                 'India', 'China', 'France', 'Japan', 'South Korea', 'Other']
    
    selected_country = st.selectbox("Select your country", options=countries, index=countries.index('Singapore'))
    
    if selected_country == 'Other':
        selected_country = st.text_input("Please enter your country", "")
    
    return selected_country

def income_expenditure_tracker():
    st.header("Daily Income and Expenditure Tracker")

    # Input fields for daily income and expenditure
    daily_income = st.number_input("Enter your daily income ($)", min_value=0.0, value=0.0)
    daily_expenditure = st.number_input("Enter your daily expenditure ($)", min_value=0.0, value=0.0)

    # Get current date/time
    current_datetime = datetime.now()

    # Select the user's country
    country = get_user_country()

    # Ensure location is selected
    if country:
        # Save button to save the entry to the CSV file
        if st.button("Save Entry"):
            # Prepare data to save
            data = {
                "date": [current_datetime],
                "country": [country],
                "income": [daily_income],
                "expenditure": [daily_expenditure]
            }
            df = pd.DataFrame(data)

            # CSV file path
            csv_file = "https://raw.githubusercontent.com/seanlam74/Compound_interest/main/modular_app/income_expenditure.csv"

            # Save data to CSV (append to the existing file or create a new one)
            df.to_csv(csv_file, mode='a', header=False, index=False)

            st.success(f"Entry saved successfully! {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}, Location: {country}")

        # Show the existing CSV file if it exists
        try:
            st.subheader("Previous Entries")
            df_existing = pd.read_csv("https://raw.githubusercontent.com/seanlam74/Compound_interest/main/modular_app/income_expenditure.csv")
            st.write(df_existing)
        except FileNotFoundError:
            st.info("No entries found yet.")
    else:
        st.warning("Please select or enter your country.")
