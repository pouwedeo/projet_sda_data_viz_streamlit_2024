import  streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import  numpy as np

def word_cloud_create(corpus_text, url):
    # wordCloud creation
    # Description of the page

    st.markdown(f"""
          <h3  style="padding: 0px 5px 5px 5px; text-align-last: center; font-weight: bold; color: purple;">Présentation du WordCloud </h3>
          <p>Le texte utilisé pour générer ce WordCloud est extrait de l'article <a href="{url}">kickstarter </a>.
           L'article met en lumière les actions de Kickstarter en tant que Public Benefit Corporation (PBC), statut adopté en 2015 pour aligner ses activités avec sa mission principale : soutenir les créateurs et leurs projets créatifs.
           </p> """, unsafe_allow_html=True)

    # WordCloud text

    # wordCloud creation with no mask
    with st.container():
        # wordCloud title
        st.markdown(f"""<h3  style=" padding: 25px 5px 5px 5px; text-align-last: center;font-weight: bold; color: purple; "> WordCloud </h3>""", unsafe_allow_html=True)

        wordcloud_show = WordCloud(width=300, height=300, background_color='black', contour_color='purple', contour_width=5).generate(corpus_text)
        fig, ax = plt.subplots(figsize=(5, 10))
        ax.imshow(wordcloud_show, interpolation='antialiased')
        ax.axis('off')
        st.pyplot(fig)

    # wordCloud creation with mask
    with st.container():
        # wordCloud title
        st.markdown(f"""<h3  style=" padding: 25px 5px 5px 15px;text-align-last: center;font-weight: bold; color: purple;"> WordCloud avec masque d'image </h3>""", unsafe_allow_html=True)

        mask = np.array(Image.open("assets/istockphoto-2166588847-1024x1024.jpg"))
        wordcloud_show = WordCloud(width=300, height=300, mask=mask, background_color='white', contour_width=1).generate(corpus_text)
        fig, ax = plt.subplots(figsize=(5, 10))
        ax.imshow(wordcloud_show, interpolation='bilinear')
        plt.tight_layout(pad=0)
        ax.axis('off')
        st.pyplot(fig)


