import streamlit as st
from  components.elements.sidebar import menu
from  components.elements.footer import footer
from  components.elements.auth_form import AuthForm

#Page configuration

st.set_page_config(
    page_title="Dashboard Kickstarter_2020",
    page_icon="assets/logo.png",
    layout="wide",
)

#Auth class
autForm =  AuthForm()
authenticator = autForm.auth()

#Connexion
result = authenticator.login(location="main", key="Login")

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.write(f'Bienvenue *{st.session_state["name"]}*')
    st.sidebar.divider()
    menu()
    footer()
elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrecte")
elif st.session_state["authentication_status"] is None:
    st.warning('Veuillez vous connecter')



