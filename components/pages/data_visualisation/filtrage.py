import streamlit as st
import pandas as pd
import datetime

# Filtering function

def filtre_data():

    #DataFrame creation
    data = pd.read_csv("data/Kickstarter_2020.csv")

    #Global filtering
    st.sidebar.header("Filtres globaux")

    #Categories filtering
    selected_category = st.sidebar.multiselect(
        "Sélectionnez une ou plusieurs catégories",
        options=data['category'],
        key="categories_key"
    )
    #Location filtering
    selected_location = st.sidebar.multiselect(
        "Sélectionnez une ou plusieurs localisation",
        options=data['location'],
        key="location_key"

    )

   #State filtering
    selected_state = st.sidebar.multiselect(
        "Sélectionnez un ou plusieurs état",
        options=data['state'],
        key="state"
    )

    # Date filtering
    st.sidebar.write("Sélectionnez les dates")
    data["launched_at"] = pd.to_datetime(data["launched_at"])

    # Sidebar date inputs
    first_date = st.sidebar.date_input("Début", value=data['launched_at'].min().date())
    last_date = st.sidebar.date_input("Fin", value=data['launched_at'].max().date())

    # Convert to datetime.datetime
    first_date = datetime.datetime.combine(first_date, datetime.datetime.min.time())
    last_date = datetime.datetime.combine(last_date, datetime.datetime.max.time())


    # Common conditions
    is_in_category = data['category'].isin(selected_category)
    is_in_date_range = (data['launched_at'] >= first_date) & (data['launched_at'] <= last_date)
    is_in_location = data['location'].isin(selected_location)
    is_in_state = data['state'].isin(selected_state)

    # Combine conditions in table

    subsets = {
        "category_range_location_state": data[(is_in_category & is_in_date_range & is_in_location & is_in_state)],
        "category_range_location": data[(is_in_category & is_in_date_range & is_in_location)],
        "category_range_state": data[(is_in_category & is_in_date_range & is_in_location)],
        "range_location_state": data[(is_in_date_range & is_in_location & is_in_state)],
        "category_range": data[(is_in_category & is_in_date_range)],
        "range_location": data[(is_in_date_range & is_in_location)],
        "range_state": data[(is_in_date_range & is_in_state)],
        "in_range": data[is_in_state]
    }

    for subset_name, subset in subsets.items():
        if not subset.empty:
            return subset

    return data