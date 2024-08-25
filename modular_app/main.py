import streamlit as st
from pages.page1_compound_interest import compound_interest_calculator
from pages.page2_other_module import other_module_function
from pages.page3_income_expenditure import income_expenditure_tracker

st.set_page_config(
    page_title="Financial Calculator", 
    page_icon="💰", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Set the title of the app
st.title("Financial Calculator App")

# Add tabs to navigate between different pages
tab1, tab2, tab3 = st.tabs(["Compound Interest Calculator", "Other Module", "Income & Expenditure Tracker"])


# Load the respective pages based on selected tabs
with tab1:
    compound_interest_calculator()

with tab2:
    other_module_function()

with tab3:
    income_expenditure_tracker()