import  streamlit as st
from  components.pages.data_visualisation.dashboard_class.DashboardClass import Dashboard

#Class for define metric data
class MetricClass(Dashboard):

    def __init__(self, data):
        super().__init__(data)
        self.data = data

    #countData metric
    def count_data(self):
        try:
            nbr_data = len(self.data)
            return nbr_data
        except Exception as e:
            st.error(f"Error in countData: {e}")


    #sumGoal metric
    def sum_goal(self):
        try:
            sum_data = self.data["goal"].sum()
            formatted_sum = f"${sum_data / 1000000:,.2f}M"
            return formatted_sum
        except Exception as e:
            st.error(f"Error in sumGoal: {e}")

    #sumPledged metric
    def sum_pledged(self):
        try:

            sum_data = self.data["pledged"].sum()
            formatted_sum = f"${sum_data / 1000000:,.2f}M"
            return formatted_sum
        except Exception as e:
            st.error(f"Error in sumPledged: {e}")

    #sumSuccess metric
    def sum_success(self):

        #Select success rows in dataframe
        total = self.data[self.data['state'] == "successful"]

        try:
            sum_data = len(total)
            return sum_data
        except Exception as e:
            st.error(f"Error in sumSuccess: {e}")
