def search(query, model, index, texts, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(query_vec, k)
    
    results = [texts[i] for i in indices[0]]
    return results