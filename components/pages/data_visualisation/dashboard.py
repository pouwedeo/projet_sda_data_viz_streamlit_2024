import streamlit as st
from  components.pages.data_visualisation.filtrage import  filtre_data
from components.elements.metric_card import custom_metric
from  components.pages.data_visualisation.metric_data import count_data, sum_goal, sum_pledged, sum_success
from  components.pages.data_visualisation.graph_analyse import stat_graph, rep_graph, correlation_graph,categorie_rep, backers_by_duration, year_stat_project
from  components.pages.data_visualisation.graph_fact import categorie_fact_stat, categorie_fact_project, time_fact, place_fact, amount_fact

#Observation choice
st.session_state.horizontal = True
st.sidebar.subheader("Type d'observation")
view_choice = st.sidebar.radio(
    "",
    ["Distribution", "Facteur"],
    horizontal=st.session_state.horizontal,
)

st.sidebar.divider()

# Data initialisation
data = filtre_data()


#KPI metrics
col1, col2, col3, col4 = st.columns(4)

with col1:

    custom_metric(
        label="Éléments",
        value=count_data(data),
        delta="",
        data_testid="metric-nombre",
        background_color="#ede7f6 ",
        text_color="#4527a0",
        delta_color="#d500f9",
    )

with col2:
    custom_metric(
        label="Objectifs",
        value=sum_goal(data["goal"]),
        data_testid="metric-goal",
        background_color="#fff3e0",
        text_color="#ef6c00",
        delta_color="#ffa726",
    )

with col3:
    custom_metric(
        label="Objectifs Atteints",
        value=sum_pledged(data["pledged"]),
        data_testid="metric-goal",
        background_color="#fff3e0",
        text_color="#ef6c00",
        delta_color="#ffa726",
    )

with col4:
    total = data[data['state'] == "successful"]
    custom_metric(
        label="Projets Réussis",
        value=sum_success(total),
        delta="",
        data_testid="metric-success",
        background_color="#e8f5e9",
        text_color="#1b5e20",
        delta_color="#4caf50",
    )


# Analyse des graphes
if view_choice == "Distribution":

    st.markdown("""
         <style>
           .graphTitle{
             padding: 20px 5px 5px 5px;
             text-align-last: center;
             font-weight: bold;
             color: gray;
           }
         </style>
         <h5 class="graphTitle">Analyser de la distribution et les tendances des campagnes </h5>
       
    """, unsafe_allow_html=True)


    #dashboard display

    with st.container():
         stat_graph(data)


    with st.container():
         categorie_rep(data)

    with st.container():
         rep_graph(data)

    with st.container():
        backers_by_duration(data)

    with st.container():
         year_stat_project(data)

elif view_choice == "Facteur":
     #Fact graphe
    st.markdown("""
         <style>
           .graphTitle{
             padding: 20px 5px 5px 5px;
             text-align-last: center;
             font-weight: bold;
             color: gray;
           }
         </style>
         <h5 class="graphTitle">Facteurs influençant le succès des projets </h5>
    
    """, unsafe_allow_html=True)


    with st.container():
        categorie_fact_project(data)

    with st.container():
        categorie_fact_stat(data)


    with st.container():
        time_fact(data)

    with st.container():
        amount_fact(data)

    with st.container():
         place_fact(data)