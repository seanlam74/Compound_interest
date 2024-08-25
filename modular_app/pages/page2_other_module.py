import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def other_module_function():
    # Set the title of the page
    st.header("Savings Projection with Multiple Scenarios")

    # Input fields for user entries
    initial_cash = st.number_input("Initial Cash ($)", min_value=0, value=10000)
    
    # Number of years for the projection
    years = st.number_input("Projection Period (Years)", min_value=1, max_value=20, value=10)
    
    # Allow multiple sets of monthly savings and annual rate of return
    scenarios = st.slider("Number of Scenarios", min_value=1, max_value=5, value=1)

    scenario_data = []
    
    for i in range(scenarios):
        st.subheader(f"Scenario {i + 1}")
        monthly_savings = st.number_input(f"Monthly Savings for Scenario {i + 1} ($)", min_value=0, value=500)
        annual_rate_of_return = st.number_input(f"Annual Rate of Return for Scenario {i + 1} (%)", min_value=0.0, max_value=100.0, value=5.0)
        scenario_data.append((monthly_savings, annual_rate_of_return))

    # Create a plot to visualize the scenarios
    plt.figure(figsize=(10, 6))

    # Loop through each scenario and plot the future value projection
    for i, (monthly_savings, annual_rate_of_return) in enumerate(scenario_data):
        months = years * 12
        monthly_rate_of_return = (1 + (annual_rate_of_return / 100)) ** (1 / 12) - 1

        # Calculate the future value for each month
        future_values = []
        total_value = initial_cash
        for month in range(1, months + 1):
            total_value = total_value * (1 + monthly_rate_of_return) + monthly_savings
            future_values.append(total_value)

        # Plot the future value
        plt.plot(range(1, months + 1), future_values, label=f'Scenario {i + 1}: {monthly_savings}/mo @ {annual_rate_of_return}%')

    # Plot settings
    plt.title("Future Value Projections")
    plt.xlabel("Months")
    plt.ylabel("Future Value ($)")
    plt.legend()
    plt.grid(True)

    # Display the plot
    st.pyplot(plt)

    st.write("You can extend this with more scenarios and details to refine the projections.")
