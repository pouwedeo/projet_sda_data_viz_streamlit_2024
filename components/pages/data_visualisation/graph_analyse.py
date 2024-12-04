import plotly.express as px
import streamlit as st
import  pandas as pd

# State graphe
def stat_graph(data_graph):

    try:
        # State count
        stat_count = data_graph["state"].value_counts().reset_index()
        stat_count.columns = ["State", "Count"]
        stat = px.pie(stat_count,names="State", values="Count", title="Répartition des campagnes par statut", color_discrete_sequence=px.colors.qualitative.Set3)
        stat.update_layout(width = 700, height= 700)
        st.plotly_chart(stat)
    except Exception as e:
        st.error(f"State graphe error: {e}")


#Projects repartitions

def rep_graph(data_graph):

    try:
        data_graph["launched_at"] = pd.to_datetime(data_graph["launched_at"])

        # Groupement par année et pays, puis comptage des occurrences de `name`
        grouped_data = data_graph.groupby([data_graph["launched_at"].dt.year, "country"])["name"].count()

        # Conversion en DataFrame si besoin
        grouped_data_df = grouped_data.reset_index(name="Count")

        fig_graph =  px.density_heatmap(grouped_data_df, x='launched_at', y='country', z='Count',
                           color_continuous_scale="Viridis", title="Répartition du nombre de projets par pays et par année",
                            labels={
                                          "launched_at": "Année de lancement",  # Nom de l'axe X
                                           "country": "Pays",  # Nom de l'axe Y
                                           "Count": "projects"  # Nom de la dimension Z
                                       } )
        fig_graph.update_layout(width = 700, height = 700)
        st.plotly_chart(fig_graph)
    except Exception as e:
        st.error(f"Graphe error: {e}")


#Project correlation

def correlation_graph(data):

        try:

            fig_correl = px.scatter(data, y="usd_pledged", x="backers_count",
                      size_max=55, range_x=[0, 100000], range_y=[0, 500000000])

            st.plotly_chart(fig_correl)

        except Exception as e:
            st.error(f"Correlation graphe: {e}")



#Répartition des campagnes par catégorie
def categorie_rep(data):
    try:
        category_counts = data["category"].value_counts().head(30).reset_index()
        category_counts.columns = ["category", "Count"]      # Affiche uniquement les 30 catégories principales
        fig_cat = px.bar(category_counts, y='Count', x='category', text='Count', color='category',
                         title="Répartition des campagnes par catégorie",
                         labels={'Count':'Nombre', 'category':'Categories'})
        fig_cat.update_layout(width=1000, height=500, xaxis_tickangle=-45, uniformtext_minsize=7)

        st.plotly_chart(fig_cat)

    except Exception as e:
        st.error(f"Correlation graphe: {e}")


#Relation entre la durée des campagnes et le nombre moyen de contributeurs
def backers_by_duration(data):
    try:
        avg_backers_by_duration = data.groupby("duration")["backers_count"].mean().reset_index(name="backers_count")
        fig_backer = px.line(avg_backers_by_duration, x='duration', y='backers_count')
        fig_backer.update_layout(title="Relation entre la durée des campagnes et le nombre moyen de contributeurs",
                               xaxis_title='Durée des campagnes (jours)', yaxis_title='Nombre moyen de contributeurs')
        st.plotly_chart(fig_backer)
    except Exception as e:
        st.error(f"Backers: {e}")


#Evolution du nombre de projets, du succès et l'echec des projets par année
def year_stat_project(data):
    try:
        data["year"] = pd.to_datetime(data["launched_at"]).dt.year

        # Groupement et agrégation
        campaigns_by_year = data.groupby("year").agg({
            "state": lambda x: x.value_counts().to_dict(),
            "name": "count"
        })

        # Ajouter une colonne pour les campagnes "successful"
        campaigns_by_year["successful_count"] = campaigns_by_year["state"].apply(lambda x: x.get("successful", 0))
        campaigns_by_year["failed_count"] = campaigns_by_year["state"].apply(lambda x: x.get("failed", 0))
        campaigns_by_year = campaigns_by_year.reset_index()
        fig_year = px.line(campaigns_by_year, x='year', y=['name', 'successful_count', 'failed_count'],
                           labels={'year': 'Années', 'successful_count': 'Succès', 'failed_count': 'Echec'})
        fig_year.update_layout(title="Evolution du nombre de projets, du succès et l'echec des projets par année",
                          xaxis_title='Années', yaxis_title='Nombre')
        st.plotly_chart(fig_year)
    except Exception as e:
        st.error(f"Backers: {e}")