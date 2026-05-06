from src.ingest import load_data
from src.embed import generate_embeddings, model
from src.index import create_index
from src.query import search

texts = load_data("data/202601_Compras.csv")
embeddings = generate_embeddings(texts)
index = create_index(embeddings)

while True:
    q = input("Pergunta: ")
    results = search(q, model, index, texts)
    
    print("\nResultados:")
    for r in results:
        print("-", r)
    print()