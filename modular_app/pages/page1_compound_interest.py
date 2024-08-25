import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def compound_interest_calculator():

    # Set the title of the page
    st.header("Compound Interest Calculator (Annual Compounding)")

    # Use columns to organize the inputs in the main content area
    col1, col2, col3 = st.columns(3)

    # Place controls in different columns
    with col1:
        # Allow user to input the principal amount
        principal = st.number_input("Principal Amount ($)", min_value=1, value=1_000_000)   

    with col2:
        # Year selection (multi-select)
        years_options = [0.5, 1, 3, 5, 7, 10, 13, 15, 20]
        selected_years = st.multiselect("Select number of years", years_options, default=[10])

    with col3:
        interest_rate_range = st.slider("Select interest rate range (%)", 1.0, 10.0, (1.0, 10.0), step=0.1)

    # Interest rate fine resolution
    interest_rates = np.arange(interest_rate_range[0], interest_rate_range[1] + 0.1, 0.1) / 100

    # Specify the interest rates to be labeled
    label_interest_rates = np.arange(max(1, int(interest_rate_range[0])), min(11, int(interest_rate_range[1]) + 1), 1)

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    max_future_value = 0  # Variable to store the maximum future value

    # Loop over the selected years and compute future values with annual compounding
    for year in selected_years:
        future_values = principal * (1 + interest_rates) ** year  # Annual compounding
        # Track the maximum future value across the iterations
        max_future_value = max(max_future_value, np.max(future_values))
        
        ax.plot(interest_rates * 100, future_values, label=f'{year} Years')
        
        # Annotate points at the specified interest rates
        for rate in label_interest_rates:
            # Use np.isclose to find the closest matching index
            idx = np.where(np.isclose(interest_rates * 100, rate))[0]
            if len(idx) > 0:  # Only proceed if a matching index is found
                idx = idx[0]
                ax.text(rate, future_values[idx], f'{future_values[idx]:,.0f}', fontsize=8, ha='right', rotation=45)
        
        # Always label the maximum interest rate in the selected range
        max_rate = interest_rate_range[1]
        max_idx = np.where(np.isclose(interest_rates * 100, max_rate))[0]
        if len(max_idx) > 0:  # Only proceed if a matching index is found
            max_idx = max_idx[0]
            ax.text(max_rate, future_values[max_idx], f'{future_values[max_idx]:,.0f}', fontsize=8, ha='left', rotation=45)

    # Plot settings
    ax.set_title(f'Future Value of ${principal:,} with Annual Compounding')
    ax.set_xlabel('Annual Interest Rate (%)')
    ax.set_ylabel('Future Value ($)')
    ax.grid(True)
    ax.legend()

    # Show the plot using Streamlit
    st.pyplot(fig)
    
    # Show selected values as information
    st.write(f"Selected Years: {selected_years}")
    st.write(f"Interest Rate Range: {interest_rate_range[0]}% - {interest_rate_range[1]}%")
    st.write(f"Maximum Future Value: ${max_future_value:,.0f}")

