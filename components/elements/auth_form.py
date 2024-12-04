import streamlit as st
from security.auth import fetch_users

import streamlit_authenticator as stauth


# Load user credentials from the database
class AuthForm:


    def load_credentials(self):
        users = fetch_users()
        credentials = {"usernames": {}}
        for user in users:
            username, hashed_password, name, email = user
            credentials["usernames"][username] = {
                "name": name,
                "password": hashed_password,
                "email":  email if email else "john@example.com",
            }
        return credentials


    def auth(self):
        credentials = self.load_credentials()
        authenticator = stauth.Authenticate(
            credentials,
            "project123",
            "auth_cookie",
            cookie_expiry_days=30,
        )
        return authenticator



