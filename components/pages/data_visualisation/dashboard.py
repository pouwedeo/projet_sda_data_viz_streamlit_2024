import streamlit as st
from  components.pages.data_visualisation.filtrage import  filtre_data
from components.pages.data_visualisation.dashboard_show_page.metric_show import metric_show
from components.pages.data_visualisation.dashboard_show_page.dashboard_show import distribution_show, fact_show
from  components.pages.data_visualisation.dashboard_show_page.prediction_show import prdiction

#Observation choice
st.session_state.horizontal = True
st.sidebar.subheader("Type d'observation")
view_choice = st.sidebar.radio(
    "",
    ["Distribution", "Facteur", "Prédiction"],
    horizontal=st.session_state.horizontal,
)

st.sidebar.divider()

# Data initialisation
data = filtre_data()


#KPI metrics
metric_show(data)

# Analyse des graphes
if view_choice == "Distribution":
    # Distributions dashboards show
    distribution_show(data)


elif view_choice == "Facteur":
    # Factors dashboards show
    fact_show(data)
#elif view_choice == "Prédiction":
      #prdiction(data)