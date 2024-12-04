import  streamlit as st

def menu():
    st.logo("assets/logo.png", size="large")
    pages = [st.Page("components/pages/data_visualisation/dashboard.py", title="Tableau de bord"),
             st.Page("components/pages/descriptions/description.py", title="Description"),
             st.Page("components/pages/text_mining/text_mining.py")
             ]


    # Chargement des pages

    page = st.navigation(pages)
    page.run()
