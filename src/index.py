import faiss
import os

def create_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def save_index(index, path="data/index.faiss"):
    faiss.write_index(index, path)

def load_index(path="data/index.faiss"):
    if os.path.exists(path):
        return faiss.read_index(path)
    return None