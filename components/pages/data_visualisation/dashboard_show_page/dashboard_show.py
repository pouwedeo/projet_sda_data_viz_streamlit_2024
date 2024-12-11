import  streamlit as st
from  components.pages.data_visualisation.dashboard_class.GraphAnalyseClass import GraphAnalyseClass
from  components.pages.data_visualisation.dashboard_class.GraphFactClass import GraphFactClass



#Distributions dashboards show
def distribution_show(data):


    # Initialisation graph class
    graph_analyse_class = GraphAnalyseClass(data)

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
        graph_analyse_class.stat_graph()

    with st.container():
        graph_analyse_class.categorie_rep()

    with st.container():
        graph_analyse_class.rep_graph()

    with st.container():
        graph_analyse_class.backers_by_duration()

    with st.container():
        graph_analyse_class.year_stat_project()
    with st.container():
        graph_analyse_class.correlation_graph()



#Factors dashboards show
def fact_show(data):

    # Initialisation graph class
    graph_fact_class = GraphFactClass(data)

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
        graph_fact_class.categorie_fact_project()

    with st.container():
        graph_fact_class.categorie_fact_stat()

    with st.container():
        graph_fact_class.time_fact()

    with st.container():
        graph_fact_class.amount_fact()

    with st.container():
        graph_fact_class.place_fact()