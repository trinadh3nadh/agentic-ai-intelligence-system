from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")

dimension = 384
index = faiss.IndexFlatL2(dimension)

memory_store = []


def store_memory(text):

    embedding = model.encode([text])

    index.add(np.array(embedding))

    memory_store.append(text)


def retrieve_memory(query):

    if len(memory_store) == 0:
        return []

    q_embedding = model.encode([query])

    D, I = index.search(np.array(q_embedding), k=3)

    results = []

    for idx in I[0]:
        if idx < len(memory_store):
            results.append(memory_store[idx])

    return results