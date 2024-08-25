import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_to_google_sheet():
    # Use st.secrets to retrieve the credentials securely
    creds_dict = st.secrets["google_sheets"]

    # Create the credentials using the data from secrets.toml
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])

    # Authorize the clientsheet
    client = gspread.authorize(creds)

    # Open the google sheet by URL
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/19sckfKvAecswPwYjfimLH5XY05DcpyF3K7n0WCgaajM/edit?usp=sharing")

    # Select the first sheet
    worksheet = sheet.sheet1
    return worksheet

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
            worksheet = connect_to_google_sheet()

            # Data in a format suitable for Google Sheets (a list of values)
            data = [str(current_datetime), country, daily_income, daily_expenditure]

            # Append the data to the Google Sheet
            worksheet.append_row(data)

            worksheet = connect_to_google_sheet()
            worksheet.append_row(["Test Date", "Test Country", 100, 50])

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
