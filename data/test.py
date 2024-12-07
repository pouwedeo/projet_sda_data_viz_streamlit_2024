import streamlit as st
import pandas as pd
import re
from unidecode import unidecode
from nltk.stem import SnowballStemmer
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from components.pages.text_mining.scrape_text import scrape_kickstarter, save_to_csv

# URL par défaut
url = "https://www.kickstarter.com/articles/pbc2020?lang=fr"
# Scraping de l'url
def scrapin_url(self):
    return scrape_kickstarter(self.url)

# Génération du fichier csv
def text_read(self):
    if text_read:
     save_to_csv(text_read)


# Définition du corpus
df = pd.read_csv("data/kickstarter.csv")
corpus = df[['Title', 'Content']].to_records(index=False).tolist()


# Analyse du corpus

def corpus_analyse(corpus):
    try:
        corpus_length = len(corpus)
        corpus_doc = []
        i = 1
        for doc in corpus:
            corpus_doc.append({'Index': i, 'Longueur': len(doc)})
            i += 1

        set_corpus_shap = {
            "Longuer": corpus_length,
            "Documents": corpus_doc
        }
        return print(f"Corpus: {set_corpus_shap}")
    except Exception as e:
        st.error(f"Impossible d'analyser le corpus: {e}")


# Liste des mots
def word_list(corpus): return [("".join(doc)).split() for doc in corpus]


# Conversion du document en chine de caractère et en minuscules
def corpus_convert(corpus):
    corpus_to_str_lower = [str((" ".join(doc).lower())) if type(doc) != str else doc.lower() for doc in corpus]
    return corpus_to_str_lower


# Suppréssion des accents

def corpus_delete_accents(corpus):
    corpus_no_accent = [unidecode(doc) for doc in corpus_convert(corpus)]
    return corpus_no_accent


# Transformation des chiffres

def corpus_delete_number(corpus):
    corpus_no_number = [re.sub(r'[0-9]{1}', 'year', doc) for doc in corpus_delete_accents(corpus)]
    return corpus_no_number


# Suppresion des \n

def corpus_delete_chario(corpus):
    corpus_no_chario = [re.sub(r'\n', '', doc) for doc in corpus_delete_number(corpus)]
    return corpus_no_chario


# Suppression des caractères
def corpus_delete_caracter(corpus):
    corpus_no_caracter = [re.sub(r'[^a-z\s]', '', doc) for doc in corpus_delete_chario(corpus)]
    return corpus_no_caracter


# Suppresion des stopword

def corpus_delete_stopwords(corpus):
    stopwords_init = set(stopwords.words('english'))
    stopwords_clean = [unidecode(sw) for sw in stopwords_init]
    corpus_no_stopword_splited = [' '.join([word for word in doc.split() if word not in stopwords_clean]) for doc in
                                  corpus_delete_caracter(corpus)]
    return corpus_no_stopword_splited


# Stemmatisation
def corpus_stemmatisation():
    stemmer = SnowballStemmer('english')
    corpus_stemmer = [" ".join([stemmer.stem(word) for word in doc.split()]) for doc in corpus_delete_stopwords(corpus)]
    return corpus_stemmer