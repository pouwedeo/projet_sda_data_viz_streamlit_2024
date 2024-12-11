import streamlit as st
import spacy
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network



# Extraction des relations

def extract_relations(text):
    nlp = spacy.load("fr_core_news_md")
    doc = nlp(text)
    G = nx.DiGraph()

    for token in doc:
        if token.dep_ in ("nsubj", "dobj", "pobj"):
            G.add_edge(token.head.text, token.text)

    return G


#Implementation des relations
def text_analyse(df):
    #DataFrame extraction
    full_text = " ".join(row[1] for row in df)
    G = extract_relations(full_text)
    st.markdown(
        f"""<h3  style="padding: 0px 5px 5px 5px;text-align-last: center;font-weight: bold;color: gray; ">Visualisation des relations entre concepts</h3>""",
        unsafe_allow_html=True)
    # Visualisation statique avec NetworkX
    with st.container():
        st.markdown(f"""<h3  style=" padding: 0px 5px 5px 5px;text-align-last: center;font-weight: bold;color: purple; ">Visualisation statique</h3>""", unsafe_allow_html=True)

        plt.figure(figsize=(10, 10))
        nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=12)
        st.pyplot(plt.gcf())


    #Visualisation interactive avec Pyvis
    with st.container():

        st.markdown(f"""<h3  style=" padding: 25px 5px 5px 5px;text-align-last: center;font-weight: bold;color: purple; ">Visualisation interactive</h3>""", unsafe_allow_html=True)

        net = Network(notebook=True, height="500px", width="100%", layout=True, font_color="purple")
        for node in G.nodes:
            net.add_node(node, label=node)
        for edge in G.edges:
            net.add_edge(edge[0], edge[1])

        net.save_graph("components/pages/text_mining/graphe.html")
        with open("components/pages/text_mining/graphe.html", "r") as f:
            st.components.v1.html(f.read(), height=550)

