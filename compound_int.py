import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title("Compound Interest Calculator (Annual Compounding)")

# Sidebar inputs for user selections
st.sidebar.header("Input Parameters")

# Allow user to input the principal amount
principal = st.sidebar.number_input("Principal Amount ($)", min_value=1, value=1_000_000)

# Year selection (multi-select)
years_options = [0.5, 1, 3, 5, 7, 10, 13, 15, 20]
selected_years = st.sidebar.multiselect("Select number of years", years_options, default=[10])

# Interest rate range slider
interest_rate_range = st.sidebar.slider("Select interest rate range (%)", 1.0, 10.0, (1.0, 10.0), step=0.1)

# Interest rate fine resolution
interest_rates = np.arange(interest_rate_range[0], interest_rate_range[1] + 0.1, 0.1) / 100

# Specify the interest rates to be labeled
label_interest_rates = np.arange(max(1, int(interest_rate_range[0])), min(11, int(interest_rate_range[1]) + 1), 1)

# Initialize the plot
plt.figure(figsize=(10, 6))

max_future_value = 0  # Variable to store the maximum future value

# Loop over the selected years and compute future values with annual compounding
for year in selected_years:
    future_values = principal * (1 + interest_rates) ** year  # Annual compounding
    # Track the maximum future value across the iterations
    max_future_value = max(max_future_value, np.max(future_values))
    
    plt.plot(interest_rates * 100, future_values, label=f'{year} Years')
    
    # Annotate points at the specified interest rates
    for rate in label_interest_rates:
        # Use np.isclose to find the closest matching index
        idx = np.where(np.isclose(interest_rates * 100, rate))[0]
        if len(idx) > 0:  # Only proceed if a matching index is found
            idx = idx[0]
            plt.text(rate, future_values[idx], f'{future_values[idx]:,.0f}', fontsize=8, ha='right', rotation=45)
    
    # Always label the maximum interest rate in the selected range
    max_rate = interest_rate_range[1]
    max_idx = np.where(np.isclose(interest_rates * 100, max_rate))[0]
    if len(max_idx) > 0:  # Only proceed if a matching index is found
        max_idx = max_idx[0]
        plt.text(max_rate, future_values[max_idx], f'{future_values[max_idx]:,.0f}', fontsize=8, ha='left', rotation=45)


# Plot settings
plt.title(f'Future Value of ${principal:,} with Annual Compounding')
plt.xlabel('Annual Interest Rate (%)')
plt.ylabel('Future Value ($)')
plt.grid(True)
plt.xticks(np.arange(int(interest_rate_range[0]), int(interest_rate_range[1]) + 1, 1))  # Dynamically adjust x-axis ticks
plt.legend()

# Show the plot
st.pyplot(plt)

# Show selected values as information
st.write(f"Selected Years: {selected_years}")
st.write(f"Interest Rate Range: {interest_rate_range[0]}% - {interest_rate_range[1]}%")
st.write(f"Maximum Future Value: ${max_future_value:,.0f}")
