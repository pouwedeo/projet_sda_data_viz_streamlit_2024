import  streamlit as st
from  components.pages.text_mining.pre_procesing import PreProcessingClass
from  components.pages.text_mining.word_cloud import word_cloud_create
from  components.pages.text_mining.text_analyse_sentiment import  sentiment_result

#Pre_processing initialisation
url = "https://www.kickstarter.com/articles/pbc2020?lang=fr" #article url
path = "data/kickstarter.csv"  #path to store the article content

#Pe_processing class
pre_processing = PreProcessingClass(url, path)

#WordCloud text generation
corpus_text = " ".join(pre_processing.corpus_stemmatisation())

#Article content initialisation
df = pre_processing.corpus_create()



#Menu observation
st.session_state.horizontal = True
st.sidebar.subheader("Type de traitement")
text_mining_choice = st.sidebar.radio(
    "",
    ["WordCloud", "Sentiment"],
    horizontal=st.session_state.horizontal,
)

#Pages observation
if text_mining_choice == "WordCloud":
    #wordCloud initialisation
    word_cloud_create(corpus_text, url)
elif text_mining_choice == "Sentiment":
    sentiment_result(df)