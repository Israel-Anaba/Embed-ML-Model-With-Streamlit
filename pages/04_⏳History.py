# history_page.py
import streamlit as st
import pandas as pd

def history_page():
    st.title('History Page')
    # Show dataframe with previous predictions made and values entered by users
    # Example dataframe
    data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'Prediction': ['Class A', 'Class B', 'Class A'],
            'User Input': ['Input 1', 'Input 2', 'Input 3']}
    df = pd.DataFrame(data)
    st.write(df)

if __name__ == "__main__":
    history_page()






# def history_page():
#     st.title("History Page")
#     st.write("Welcome to the History Page")
#     st.write("This page shows a dataframe with previous predictions and user input values.")
#     # Display a dataframe containing previous predictions, timestamps, etc.
#     # Add more content as needed
