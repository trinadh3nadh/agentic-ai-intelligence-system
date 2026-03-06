import streamlit as st
import networkx as nx
from pyvis.network import Network


@st.cache_data
def extract_entities(text):

    triples = []

    lines = text.split("\n")

    for line in lines:

        parts = line.split()

        if len(parts) >= 3:

            subject = parts[0]
            relation = parts[1]
            obj = " ".join(parts[2:])

            triples.append((subject, relation, obj))

    return triples


@st.cache_data
def build_graph(triples):

    G = nx.DiGraph()

    for s, r, o in triples:

        G.add_node(s)
        G.add_node(o)

        G.add_edge(s, o, label=r)

    return G


def visualize_graph(G):

    net = Network(height="550px", width="100%", directed=True)

    for node in G.nodes:
        net.add_node(node, label=node)

    for source, target, data in G.edges(data=True):
        net.add_edge(source, target, label=data["label"])

    path = "kg.html"

    net.save_graph(path)

    return path