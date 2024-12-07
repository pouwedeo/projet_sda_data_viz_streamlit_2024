import streamlit as st
from  components.pages.data_visualisation.metric_data import count_data, sum_goal, sum_pledged, sum_success
from components.elements.metric_card import custom_metric


def metric_show(data):
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


