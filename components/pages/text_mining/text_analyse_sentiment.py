import streamlit as st
from textblob import TextBlob
from transformers import pipeline
from components.elements.metric_card import custom_metric


#Analyse de sentiment avec TextBlob

def analyze_sentiment_with_textblob(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Score entre -1 (négatif) et 1 (positif)
    subjectivity = blob.sentiment.subjectivity  # Score entre 0 (objectif) et 1 (subjectif)
    return polarity, subjectivity

#Analyse de sentiment avancée avec Transformers

def analyze_sentiment_with_transformers(text):
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_analyzer(text[:512])  # Analyse des 512 premiers caractères (limite du modèle)
    return result

def sentiment_result(df):
    text = " ".join(row[1] for row in df)
    with st.spinner("Analyse des sentiments..."):
           st.markdown(
              f"""<h3  style="padding: 0px 5px 5px 5px;text-align-last: center;font-weight: bold;color: gray; ">Analyse de sentiments et ton du marketing</h3>""",
             unsafe_allow_html=True)
           col_blob, col_trans = st.columns(2)
           with col_blob:
                # Analyse avec TextBlob
                polarity, subjectivity = analyze_sentiment_with_textblob(text)
                st.markdown(f"""<h5  style=" padding: 25px 5px 5px 5px;text-align-last: center;font-weight: bold;color: purple; ">Résultats avec TextBlob</h5>""",
                    unsafe_allow_html=True)
                col_pol, col_sub = st.columns(2)
                with col_pol:
                    custom_metric(
                        label="Polarité",
                        value= "%.2f"% (polarity * 100) +"%",
                        delta="",
                        data_testid="metric-nombre",
                        background_color="#ede7f6 ",
                        text_color="#4527a0",
                        delta_color="#d500f9",
                    )
                with col_sub:
                    custom_metric(
                        label="Subjectivité",
                        value= "%.2f"%(subjectivity * 100) +"%",
                        delta="",
                        data_testid="metric-nombre",
                        background_color="#ede7f6 ",
                        text_color="#4527a0",
                        delta_color="#d500f9",
                    )
                    #st.write(f"Polarité : {polarity:.2f} (Négatif si < 0, Positif si > 0)")
                    #st.write(f"Subjectivité : {subjectivity:.2f} (0 = objectif, 1 = subjectif)")

           with col_trans:
                # Analyse avancée avec Transformers
                transformer_result = analyze_sentiment_with_transformers(text)
                st.markdown(
                    f"""<h5  style=" padding: 25px 5px 5px 5px;text-align-last: center;font-weight: bold;color: purple; ">Résultats avec Transformers</h5>""",
                    unsafe_allow_html=True)

                col_lab, col_sc = st.columns(2)
                with col_lab:
                    custom_metric(
                        label="Etat",
                        value=transformer_result[0]['label'],
                        delta="",
                        data_testid="metric-success",
                        background_color="#e8f5e9",
                        text_color="#1b5e20",
                        delta_color="#4caf50",
                    )
                with col_sc:
                    custom_metric(
                        label="Score",
                        value="%.2f"%(transformer_result[0]['score']* 100)+"%",
                        delta="",
                        data_testid="metric-success",
                        background_color="#e8f5e9",
                        text_color="#1b5e20",
                        delta_color="#4caf50",
                    )

           # Identifier le ton marketing
           if polarity > 0.5:
              st.success(f"{polarity * 100:.2f}% de sentiment(s) **positif(s)** dans TextBlob signifie que le texte a une polarité  **positive**"
                  "D'où le ton général du texte est **positif**, avec un accent sur l'enthousiasme.")
           elif polarity < -0.5:
              st.error(f"{polarity * 100:.2f}% de sentiment(s) **négatif(s)** dans TextBlob signifie que le texte a une polarité  **négative**"
                  " D'où le ton général du texte est **négatif**, avec une critique ou un manque d'optimisme.")
           else:
             st.warning(f"{polarity * 100:.2f}% de sentiment(s) **positif(s)** dans TextBlob signifie que le texte a une polarité légèrement **positive**"
                        f" D'où le ton général du texte est **neutre**, sans émotions marquées.")

           #Interpretation du résultat du transformer_result
           st.write(
               f"L'analyse de sentiment réalisée avec **Transformers** indique un résultat **{transformer_result[0]['label']}** avec un score de {transformer_result[0]['score'] * 100:.2f}%. "
               f"Cependant, ce résultat peut être limité, car l'analyse de **Transformers** est restreinte à un maximum de 512 caractères, ce qui peut ne pas refléter pleinement le ton général de l'article.")
