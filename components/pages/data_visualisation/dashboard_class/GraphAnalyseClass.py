import  streamlit as st
import plotly.express as px
import  pandas as pd
import numpy as np
import plotly.figure_factory as ff
from  components.pages.data_visualisation.dashboard_class.DashboardClass import  Dashboard

#Class to define analyse projects distribution graph
class GraphAnalyseClass(Dashboard):
    def __init__(self, data):
        super().__init__(data)
        self.data = data


    # State graphe
    def stat_graph(self):
        st.markdown("""
                  <style>
                      .streamlit-expanderHeader {
                          font-size: 20px;
                          font-weight: bold;
                      }
                      .user-select-none svg-container {
                          border-radius: 15px;
                          box-shadow: 5px 5px 5px 5px rgba(0, 0, 0, 0.1);
                      }
                  </style>
              """, unsafe_allow_html=True)
        try:
            # State count
            stat_count = self.data["state"].value_counts().reset_index()
            stat_count.columns = ["State", "Count"]
            stat = px.pie(stat_count, names="State", values="Count", title="Répartition des campagnes par statut",
                          color_discrete_sequence=px.colors.qualitative.Set3)
            stat.update_layout(width=700, height=700, paper_bgcolor="white",
                               font=dict(family="Arial", size=14, color="black"))

            st.plotly_chart(stat)
        except Exception as e:
            st.error(f"State graphe error: {e}")




    # Projects repartitions

    def rep_graph(self):

        try:
            self.data["launched_at"] = pd.to_datetime(self.data["launched_at"])

            # Groupement par année et pays, puis comptage des occurrences de `name`
            grouped_data = self.data.groupby([self.data["launched_at"].dt.year, "country"])["name"].count()

            # Conversion en DataFrame si besoin
            grouped_data_df = grouped_data.reset_index(name="Count")

            fig_graph = px.density_heatmap(grouped_data_df, x='launched_at', y='country', z='Count',
                                           color_continuous_scale="Viridis",
                                           title="Répartition du nombre de projets par pays et par année",
                                           labels={
                                               "launched_at": "Année de lancement",
                                               "country": "Pays",
                                               "Count": "Projects"
                                           })
            fig_graph.update_layout(width=700, height=700)
            st.plotly_chart(fig_graph)
        except Exception as e:
            st.error(f"Graphe error: {e}")





    # Project correlation
    def correlation_graph(self):

        try:
            self.data["year"] = self.data["launched_at"].dt.year
            fig_correl = px.scatter(self.data, y="usd_pledged", x="backers_count",log_x=True,
                                    range_y=[0, 90000], hover_name="country", size="goal",
            size_max=55, animation_frame="year", animation_group="country", color="state",
            labels={'usd_pledged': 'Montant collecté (USD)', 'backers_count': 'Nombre de contributeurs',
                   'country': 'Pays', 'year': 'Années', 'state':'Etat du projet','goal': 'Montant demandé'},
                title= 'Analyse des montants collectés sur Kickstarter 2020')

            st.plotly_chart(fig_correl)

        except Exception as e:
            st.error(f"Correlation graphe: {e}")




    # Répartition des campagnes par catégorie
    def categorie_rep(self):
        try:
            category_counts = self.data["category"].value_counts().head(30).reset_index()
            category_counts.columns = ["category", "Count"]  # Affiche uniquement les 30 catégories principales
            fig_cat = px.bar(category_counts, y='Count', x='category', text='Count', color='category',
                             title="Répartition des campagnes par catégorie",
                             labels={'Count': 'Nombre de projets', 'category': 'Categories'})
            fig_cat.update_layout(width=1000, height=500, xaxis_tickangle=-45, uniformtext_minsize=7)

            st.plotly_chart(fig_cat)

        except Exception as e:
            st.error(f"Correlation graphe: {e}")



    # Relation entre la durée des campagnes et le nombre moyen de contributeurs
    def backers_by_duration(self):
        try:
            avg_backers_by_duration = self.data.groupby("duration")["backers_count"].mean().reset_index(name="backers_count")
            fig_backer = px.line(avg_backers_by_duration, x='duration', y='backers_count')
            fig_backer.update_layout(title="Relation entre la durée des campagnes et le nombre moyen de contributeurs",
                                     xaxis_title='Durée des campagnes (jours)',
                                     yaxis_title='Nombre moyen de contributeurs')
            st.plotly_chart(fig_backer)
        except Exception as e:
            st.error(f"Backers: {e}")



    # Evolution du nombre de projets, du succès et l'echec des projets par année
    def year_stat_project(self):
        try:
            self.data["year"] = pd.to_datetime(self.data["launched_at"]).dt.year

            # Groupement et agrégation
            campaigns_by_year = self.data.groupby("year").agg({
                "state": lambda x: x.value_counts().to_dict(),
                "name": "count",
                "backers_count": "sum"
            })

            # Ajouter une colonne pour les campagnes "successful"
            campaigns_by_year["successful_count"] = campaigns_by_year["state"].apply(lambda x: x.get("successful", 0))
            campaigns_by_year["failed_count"] = campaigns_by_year["state"].apply(lambda x: x.get("failed", 0))
            campaigns_by_year = campaigns_by_year.reset_index()

            fig_year = px.line()

            fig_year.add_scatter(
                x=campaigns_by_year["year"],
                y=campaigns_by_year["backers_count"],
                mode="lines",
                name="Nombre de contributeurs",
                yaxis="y1"
            )

            fig_year.add_scatter(
                x=campaigns_by_year["year"],
                y=campaigns_by_year["name"],
                mode="lines",
                name="Nombre de projets",
                yaxis="y2"  # Deuxième axe y
            )

            fig_year.add_scatter(
                x=campaigns_by_year["year"],
                y=campaigns_by_year["successful_count"],
                mode="lines",
                name="Nombre de projets réussis",
                yaxis="y2"
            )

            fig_year.add_scatter(
                x=campaigns_by_year["year"],
                y=campaigns_by_year["failed_count"],
                mode="lines",
                name="Nombre de projets échoués",
                yaxis="y2"
            )

            # Mettre à jour la disposition
            fig_year.update_layout(
                title="Évolution des campagnes par année",
                xaxis_title="Années",
                yaxis=dict(title="Nombre de contributeurs", side="left"),
                yaxis2=dict(title="Nombre de projets", overlaying="y", side="right"),
                legend=dict(title="Légende",  x=1,  y=1.1, xanchor="center", yanchor="bottom" ) )

            st.plotly_chart(fig_year)
        except Exception as e:
            st.error(f"Backers: {e}")


    def pledged_distribution(self):
      try:
       """ fig = px.histogram(
            self.data,
            y="pledged",
            nbins=100,
            height=500,
            title="Distribution des montants collectés (USD)",
            labels={"pledged": "Montant collecté (USD)"},
            color_discrete_sequence=["skyblue"]
        )

        fig.update_layout(
            title= "Analyse des montants collectés sur Kickstarter",
            yaxis_title="Montant collecté (USD)",
            xaxis_title="Nombre de projets",
            bargap=1
        )
        st.plotly_chart(fig)"""

      except Exception as e:
          st.error(f"pledged: {e}")