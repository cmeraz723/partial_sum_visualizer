import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the variable
n = sp.symbols('n')

# Function to calculate the nth term of the series based on user's choice
def series_term(n, formula):
    try:
        expr = sp.sympify(formula)
        result = expr.subs(sp.symbols('n'), n)
        return float(result)
    except (sp.SympifyError, TypeError):
        return 0

# Function to calculate partial sums
def partial_sums(num_terms, formula):
    terms = np.array([series_term(n, formula) for n in range(1, num_terms + 1)])
    partial_sums = np.cumsum(terms)
    return partial_sums

st.title("Partial Sum Visualizer")

# User input for choosing predefined series or custom formula
series_option = st.radio(
    "Choose a series type or input a custom formula",
    ("Predefined series", "Custom formula")
)

# Predefined series
predefined_series = {
    "1/n": "1/n",
    "1/n^2": "1/n^2",
    "(-1)^n / n": "(-1)**n / n"
}

if series_option == "Predefined series":
    series_type = st.selectbox("Choose a series type", list(predefined_series.keys()))
    formula = predefined_series[series_type]
else:
    formula = st.text_input("Enter the formula for the nth term (use 'n' as the variable)", "1/n^2")

# Number of terms slider
num_terms = st.slider("Number of terms", min_value=1, max_value=100, value=50)

# Calculate partial sums
sums = partial_sums(num_terms, formula)

# Plotting
fig, ax = plt.subplots()
ax.plot(range(1, num_terms + 1), sums, marker='o', linestyle='-', color='b')
ax.set_title(f'Partial Sums for the Series: $\\sum {formula}$')
ax.set_xlabel('Number of Terms')
ax.set_ylabel('Partial Sum')
ax.grid(True)

# Display the plot
st.pyplot(fig)
