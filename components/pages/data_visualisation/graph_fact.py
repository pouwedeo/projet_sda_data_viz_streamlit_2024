import plotly.express as px
import streamlit as st
import  pandas as pd

# Taux de succès par catégorie (Top catégories qui ont plus de projets)
def categorie_fact_project(data):
   try:
       success_rate_by_category = data.groupby("category")["state"].apply(
           lambda x: (x == "successful").mean() * 100
       ).reset_index(name="success_rate")

       # Ajouter une colonne pour le nombre total de projets par catégorie
       success_rate_by_category["total_projects"] = data.groupby("category")["state"].count().values

       # Trier par le nombre total de projets (décroissant)
       success_rate_by_category = success_rate_by_category.sort_values(by="total_projects", ascending=False)

       # Garder uniquement les N premières catégories les plus importantes
       top_categories = success_rate_by_category.head(10)
       top_categories.columns = ["category", "success_rate", 'total_projects']

       fig_cat_fact = px.bar(top_categories, x='category', y='success_rate',hover_data='total_projects', hover_name='total_projects', title='Taux de succès par catégorie (Top catégories qui ont plus de projets)',
              labels={'category': 'Categories', 'success_rate': 'Taux de succès', 'total_projects': 'Nombre de projets'}, text='success_rate')
       fig_cat_fact.update_layout(width = 700, height = 500, xaxis_tickangle=-25, uniformtext_minsize=7)
       fig_cat_fact.update_traces(texttemplate= '%{text:.2s}')

       st.plotly_chart(fig_cat_fact)
   except Exception as e:
       st.error(f"Categorie: {e}")

#Taux de succès par catégorie (Top catégories)
def categorie_fact_stat(data):
   try:
       success_rate_by_category = data.groupby("category")["state"].apply(
           lambda x: (x == "successful").mean() * 100
       ).reset_index(name="success_rate")

       # Ajouter une colonne pour le nombre total de projets par catégorie
       success_rate_by_category["total_projects"] = data.groupby("category")["state"].count().values

       # Trier par le nombre total de projets (décroissant)
       success_rate_by_category = success_rate_by_category.sort_values(by="success_rate", ascending=False)

       # Garder uniquement les N premières catégories les plus importantes
       top_categories = success_rate_by_category.head(10)
       top_categories.columns = ["category", "success_rate", 'total_projects']

       fig_cat_fact = px.bar(top_categories, x='category', y='success_rate', text='success_rate',
                             title='Taux de succès par catégorie (Top catégories)',color='success_rate',
                             labels={'category': 'Categories', 'success_rate': 'Taux de succès'}, barmode='group')
       fig_cat_fact.update_layout(width = 700, height = 500, xaxis_tickangle=-45, uniformtext_minsize=7)
       fig_cat_fact.update_traces(texttemplate='%{text:.2s}')
       st.plotly_chart(fig_cat_fact)
   except Exception as e:
       st.error(f"Categorie: {e}")


#Taux de succès en fonction de la durée de la campagne
def time_fact(data):
    try:
        data["duration_bins"] = pd.cut(data["duration"], bins=[0, 10, 20, 30, 40, 50, float('inf')],
                                     labels=["<10 jours", "10-20 jours", "20-30 jours", "30-40 jours", "40-50 jours",">50 jours"])

        # Calculer le taux de succès pour chaque intervalle
        success_rate_by_duration = data.groupby("duration_bins")["state"].apply(
            lambda x: (x == "successful").mean() * 100).reset_index(name="success_rate")

        fig_time_fact = px.bar(success_rate_by_duration, x='duration_bins', y='success_rate',text='success_rate',
                              title='Taux de succès en fonction de la durée de la campagne',
                              labels={'duration_bins': 'Durée de la campagne', 'success_rate': 'Taux de succès en %'}, barmode='group')
        fig_time_fact.update_layout(width=700, height=500, xaxis_tickangle=-45, uniformtext_minsize=7)
        fig_time_fact.update_traces(texttemplate='%{text:.2s}')

        st.plotly_chart(fig_time_fact)
    except Exception as e:
        st.error(f"Time: {e}")


#Taux de succès par pays
def place_fact(data):
    try:
        success_rate_by_country = data.groupby("country")["state"].apply(
            lambda x: (x == "successful").mean() * 100).reset_index(name="success_rate")
        # Trier par taux de succès décroissant
        success_rate_by_country = success_rate_by_country.sort_values(by="success_rate", ascending=False)

        fig_place_fact = px.bar(success_rate_by_country, x='country', y='success_rate',text='success_rate',
                           title='Taux de succès par pays',
                           labels={'country': 'Pays', 'success_rate': 'Taux de succès en %'},
                           barmode='group')
        fig_place_fact.update_layout(width=700, height=500, xaxis_tickangle=-45, uniformtext_minsize=7)
        fig_place_fact.update_traces(texttemplate='%{text:.2s}')

        st.plotly_chart(fig_place_fact)
    except Exception as e:
        st.error(f"Place: {e}")


#Taux de succès en fonction du montant demandé
def amount_fact(data):
  try:
      data["goal_bins"] = pd.cut(data["goal"], bins=[0, 1000, 5000, 10000, 50000, 100000, float('inf')],
                               labels=["<1k", "1k-5k", "5k-10k", "10k-50k", "50k-100k", ">100k"])

      # Calculer le taux de succès pour chaque intervalle
      success_rate_by_goal = data.groupby("goal_bins")["state"].apply(lambda x: (x == "successful").mean() * 100).reset_index(name="success_rate")


      fig_amount_fact = px.pie(success_rate_by_goal, names="goal_bins", values="success_rate", title="Taux de succès en fonction du montant demandé",
                    color_discrete_sequence=px.colors.qualitative.Set3, labels={'goal_bins': 'Montant demandé (USD)', 'success_rate': 'Taux de succès en %'})
      fig_amount_fact.update_layout(width=700, height=700)

      st.plotly_chart(fig_amount_fact)
  except Exception as e:
      st.error(f"Amount: {e}")