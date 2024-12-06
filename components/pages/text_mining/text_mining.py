import  streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import  numpy as np
from  components.pages.text_mining.pre_procesing import corpus_stemmatisation

#Pre_processing


#wordCloud
corpus_text = " ".join(corpus_stemmatisation())
mask = np.array(Image.open("assets/istockphoto-2166588847-1024x1024.jpg"))
wordCloud = WordCloud(width=800, height=800, mask=mask, background_color='white', contour_color= 'black', contour_width=5).generate(corpus_text)
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(wordCloud, interpolation='antialiased')
ax.axis('off')

st.pyplot(fig)