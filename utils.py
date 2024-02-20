# utils.py
# utils.py
import streamlit as st

# Define allowed usernames and passwords
ALLOWED_USERS = {
    "username1": "password1",
    "username2": "password2",
    # Add more usernames and passwords as needed
}

# Define function to authenticate users
def authenticate(username, password):
    if username in ALLOWED_USERS and ALLOWED_USERS[username] == password:
        return True
    return False

# Login function
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Logged in successfully!")
            return True
        else:
            st.error("Invalid username or password")
    return False









# # utils.py
# import streamlit as st

# def authenticate(password):
#     """
#     Authenticate users based on the provided password.
#     """
#     if password != st.secrets["password"]:
#         st.error("Incorrect password. Please try again.")
#         st.stop()






# Import necessary modules
# Updated import statement

# from data import data_page
# from dashboard import dashboard_page
# from predict import predict_page
# from history import history_page

# # Define functions to import modules
# def get_data_page():
#     return data_page

# def get_dashboard_page():
#     return dashboard_page

# def get_predict_page():
#     return predict_page

# def get_history_page():
    # return history_page

# 01_ 😀View_Data.py 
# 02_📊Dashboard.py
# 03_🤷‍♂️Predict.py
# 04_⏳History.py