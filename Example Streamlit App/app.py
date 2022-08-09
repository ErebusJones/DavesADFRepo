import streamlit as st
from calc import monthly_compounding


def app():
    st.title("Will I be rich? :money_with_wings:")
    initial = float(st.number_input("Please input initial value: "))
    monthly = float(st.number_input("Please input the value of consistent monthly contributions: "))
    annual_rate = float(st.number_input("Please input the annual percent floaterest rate, as a decimal between 0 and 1: "))
    years = int(st.slider("Please input how many years you will be invested for: ", min_value=0, max_value=100))
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)
    st.markdown(f'After {int(years)} years you would have:\n{final_sum} :sunglasses:')

if __name__ == "__main__":
    app()