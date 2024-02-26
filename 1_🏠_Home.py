

import streamlit as st
import yaml

# Function to authenticate user
def authenticate(username, password):
    with open('users.yaml', 'r') as file:
        users = yaml.safe_load(file)['users']
        for user in users:
            if user['username'] == username and user['password'] == password:
                return True
    return False

# Function to initialize session state
def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

def main():
    init_session_state()

    # st.sidebar.title("Login")

    if not st.session_state.logged_in:
        username = st.sidebar.text_input('Username')
        password = st.sidebar.text_input('Password', type='password')
        if st.sidebar.button('Login'):
            if authenticate(username, password):
                st.session_state.logged_in = True
                st.sidebar.empty()  # Clears the sidebar
            else:
                st.sidebar.error('Invalid username or password.')
    else:
        st.title("Your Application Name")
        st.write("Welcome to your Streamlit application!")
        st.write("This application is designed to ... (provide a brief description of your application)")

        # Link to GitHub repository
        st.write("Find the source code on [GitHub](link_to_your_github_repository)")

        # Social handles
        st.write("Connect with me:")
        st.write("[GitHub](link_to_your_github_profile)")
        st.write("[LinkedIn](link_to_your_linkedin_profile)")
        st.write("[Medium](link_to_your_medium_profile)")
        # Add more social handles as needed

if __name__ == "__main__":
    main()


































# home.py
# import streamlit as st
# from pages.data import data_page
# from pages.dashboard import dashboard_page
# from pages.predict import predict_page
# from pages.history import history_page

# # Authenticate users
# def st_authenticate():
#     # Ask user for password
#     password = st.text_input("Password", type="password")

#     # Check if password is correct
#     if password == st.secrets["password"]:
#         st.success("Login successful!")
#     else:
#         st.error("Incorrect password")

# def main():
#     # Authenticate users
#     st_authenticate()

#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ["Home", "Data", "Dashboard", "Predict", "History"])

#     if page == "Home":
#         st.title("Home Page")
#         st.write("Welcome to the Home Page")
#         st.write("This page contains information about the application.")
#         st.write("Include links to GitHub, social handles, etc.")
#     elif page == "Data":
#         data_page()
#     elif page == "Dashboard":
#         dashboard_page()
#     elif page == "Predict":
#         predict_page()
#     elif page == "History":
#         history_page()

# if __name__ == "__main__":
#     main()


# # main.py
# import streamlit as st

# def main():
#     st.title("Your Application Name")
#     st.write("Welcome to your Streamlit application!")
#     st.write("This application is designed to ... (provide a brief description of your application)")

#     # Link to GitHub repository
#     st.write("Find the source code on [GitHub](link_to_your_github_repository)")

#     # Social handles
#     st.write("Connect with me:")
#     st.write("[GitHub](link_to_your_github_profile)")
#     st.write("[LinkedIn](link_to_your_linkedin_profile)")
#     st.write("[Medium](link_to_your_medium_profile)")
#     # Add more social handles as neededdd

# if __name__ == "__main__":
#     main()
