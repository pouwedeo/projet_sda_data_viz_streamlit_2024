import  streamlit as st
from  components.pages.data_visualisation.graph_fact import categorie_fact_stat, categorie_fact_project, time_fact, place_fact, amount_fact
from  components.pages.data_visualisation.graph_analyse import stat_graph, rep_graph, correlation_graph,categorie_rep, backers_by_duration, year_stat_project

#Distributions dashboards show
def distribution_show(data):
    st.markdown("""
             <style>
               .graphTitle{
                 padding: 20px 5px 5px 5px;
                 text-align-last: center;
                 font-weight: bold;
                 color: gray;
               }
             </style>
             <h5 class="graphTitle">Analyse de la distribution ainsi que les tendances des campagnes </h5>

        """, unsafe_allow_html=True)

    # dashboard display

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



#Factors dashboards show
def fact_show(data):
    # Fact graphe
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