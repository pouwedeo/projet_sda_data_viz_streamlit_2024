import streamlit as st
import pandas as pd
import re
import os
from unidecode import unidecode
from nltk.stem import SnowballStemmer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from components.pages.text_mining.text_extration.scrape_text import scrape_kickstarter, save_to_csv


#Pre_processing class
class PreProcessingClass:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    # Scraping de l'url
    def scraping_url(self):
        return  scrape_kickstarter(self.url)

    #Génération du fichier csv
    def text_read(self):
        text_read = self.scraping_url()
        if text_read:
          return  save_to_csv(text_read, self.path)

    #Définition du corpus
    def corpus_create(self):
        if not os.path.exists(self.path):
            self.text_read()
        try:
            df = pd.read_csv(self.path)
            if df.empty:
                self.text_read()
                df = pd.read_csv(self.path)

            return df[['Title', 'Content']].to_records(index=False).tolist()
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    #Analyse du corpus

    def corpus_analyse(self):
        try:
            corpus= self.corpus_create()
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

    #Liste des mots
    def word_list(self):
        corpus = self.corpus_create()
        return  [("".join(doc)).split() for  doc in corpus]

    #Conversion du document en chine de caractère et en minuscules
    def corpus_convert(self):
        corpus = self.corpus_create()
        corpus_to_str_lower = [str((" ".join(doc).lower())) if type(doc) != str else doc.lower() for doc in corpus]
        return corpus_to_str_lower

    #Suppréssion des accents

    def corpus_delete_accents(self):
        corpus = self.corpus_convert()
        corpus_no_accent = [unidecode(doc) for  doc in corpus]
        return  corpus_no_accent


    #Transformation des chiffres

    def corpus_delete_number(self):
        corpus = self.corpus_delete_accents()
        corpus_no_number = [re.sub(r'[0-9]', 'year', doc) for doc in  corpus]
        return corpus_no_number


    #Suppresion des \n

    def corpus_delete_chario(self):
        corpus = self.corpus_delete_number()
        corpus_no_chario = [re.sub(r'\n', '', doc) for doc in corpus]
        return corpus_no_chario


    #Suppression des caractères
    def corpus_delete_caracter(self):
        corpus = self.corpus_delete_chario()
        corpus_no_caracter = [re.sub(r'[^a-z\s]', '', doc) for doc in corpus]
        return corpus_no_caracter


    #Suppresion des stopword

    def corpus_delete_stopwords(self):
        corpus = self.corpus_delete_caracter()
        stopwords_init = set(stopwords.words('english'))
        stopwords_clean = [unidecode(sw) for sw in stopwords_init]
        corpus_no_stopword_splited = [' '.join([word for word in doc.split() if word not in stopwords_clean]) for doc in corpus]
        return  corpus_no_stopword_splited

    #Stemmatisation
    def corpus_stemmatisation(self):
        corpus = self.corpus_delete_stopwords()
        stemmer = SnowballStemmer('english')
        corpus_stemmer = [" ".join([stemmer.stem(word) for word in doc.split()]) for doc in  corpus]
        return corpus_stemmer