def search(query, model, index, texts, k=3):
    query_vec = model.encode([query])
    distances, indices = index.search(query_vec, k)
    
    results = []
    for i, idx in enumerate(indices[0]):
        results.append((texts[idx], distances[0][i]))
    
    return results