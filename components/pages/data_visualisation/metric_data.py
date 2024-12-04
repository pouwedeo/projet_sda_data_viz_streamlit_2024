import  streamlit as st

#countData metric
def count_data(data):
    try:
        nbr_data = len(data)
        return nbr_data
    except Exception as e:
        st.error(f"Error in countData: {e}")


#sumGoal metric
def sum_goal(data):
    try:
        sum_data = data.sum()
        formatted_sum = f"{sum_data / 1000000:,.2f}M"
        return formatted_sum
    except Exception as e:
        st.error(f"Error in sumGoal: {e}")

#sumPledged metric
def sum_pledged(data):
    try:

        sum_data = data.sum()
        formatted_sum = f"{sum_data / 1000000:,.2f}M"
        return formatted_sum
    except Exception as e:
        st.error(f"Error in sumPledged: {e}")

#sumSuccess metric
def sum_success(data):
    try:
        sum_data = len(data)
        return sum_data
    except Exception as e:
        st.error(f"Error in sumSuccess: {e}")
