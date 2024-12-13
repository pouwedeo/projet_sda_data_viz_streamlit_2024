## Read me project sda data viz streamlit 2024
## Predicting the Success of Kickstarter Projects
   An interactive application that estimates the probability of success of a Kickstarter project based on various factors.
### Project Description
   This project aims to predict the likelihood of success for a Kickstarter project using data such as:

- The project's category.
- The campaign duration.
- The financial goal set.
- The country where the project is launched.

The application is built with Streamlit, providing an interactive and user-friendly experience.

### Features
- Input parameters for Kickstarter projects.
- Real-time prediction of success probability.
- Visualization of factors influencing success.
- Project distribution 
- Text Mining

## Installation

### Prerequisites
- Python 3.8 or higher 
- pip (Python package installer)

### Clone the Repository
    git clone https://github.com/pouwedeo/projet_sda_data_viz_streamlit_2024.git
    cd projet_sda_data_viz_streamlit_2024

## Create and Activate Virtual Environment (Optional but Recommended)

### On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

### On Windows
    python -m venv venv
    venv\Scripts\activate

## Install Dependencies
    pip install -r requirements.txt

## Running the Application
To start the Streamlit application, run the following command from the root directory of the project:
 
    
    streamlit run app.py

## Authentifation 
   UserName: user1
   password: password23

## Project Structure



##### projet_sda_data_viz_streamlit_2024/

      
     
      ├── .streamlit/                     #Configuration files for Streamlit.
      ├── assets/                         #Contains static assets such as images, icons.
      ├── components/
      ├── element/
      │    __init__.py
      │   ├── auth_form.py                #Handles user authentication forms.
      │   ├── footer.py                   #Defines the footer for the application.
      │   ├── metric_card.py              #Component for displaying key metrics.
      │   └── sidebar.py                  #Manages the sidebar layout and navigation.
      ├── pages/                          #Streamlit pages for modularized views.
      │   ├── data_visualisation/         #Contains classes and scripts for data visualization.
      │   │   ├── dashboard_class/        
      │   │   │   ├── DashboardClass.py   #Manages dashboard layout and data interactions.
      │   │   │   ├── GraphAnalyseClass.py #andles analytical graph generation.
      │   │   │   ├── GraphFactClass.py    #Generates factors graphs.
      │   │   │   └── MetricClass.py       #Manages metric computations and displays.
      │   │   ├── dashboard_show_page/
      │   │   │   ├── dashboard_show.py    #Displays the main dashboard.
      │   │   │   ├── metric_show.py       #Displays metric-related data
      │   │   │   └── prediction_show.py   #Handles prediction-related displays.
      │   │   ├── dashboard.py             #dashboard functionalities.
      │   │   └── filtrage.py              #Implements data filtering logic.
      ├── descriptions/
      │   └── description.py               #Manages descriptive text and metadata.
      ├── text_mining/
      │   ├── text_analyse/
      │   │   ├── word_cloud.py            #erforms sentiment analysis.
      │   │   └── text_analyse_sentiment.py #Generates word clouds from text data.
      │   │    
      │   ├── text_extration/
      │   │   ├── pre_procesing.py          #Prepares text for analysis.
      │   │   └── scrape_text.py            # Extracts text from web or other sources.
      │   └── text_mining.py
      ├── data/                             # Dataset used
      │   ├── .ipynb_checkpoints/
      │   ├── kickstarter.csv                #Corpus
      │   ├── Kickstarter_2020.csv           #DataFrame
      │   └── users.db                       #Database for storing user information.
      ├── lib/
      ├── security/                          #Contains files and scripts for securing the application.
      ├── app.py                             # Main Streamlit application file
      ├── README.md            
      └── requirements.txt                   # Project dependencies
      


