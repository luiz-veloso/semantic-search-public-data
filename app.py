from src.generate import generate_answer
from src.ingest import load_data
from src.embed import generate_embeddings, model
from src.index import create_index, save_index, load_index
from src.query import search

def main():
    print("Carregando dados...")
    texts = load_data("data/202601_Compras.csv")

    print("Verificando índice FAISS...")
    index = load_index()

    if index is None:
        print("Gerando embeddings...")
        embeddings = generate_embeddings(texts)
        
        print("Criando índice FAISS...")
        index = create_index(embeddings)
        
        print("Salvando índice...")
        save_index(index)
    else:
        print("Índice carregado com sucesso!")

    print("\nPronto para buscas!\n")

    while True:
        try:
            q = input("Pergunta (ou 'sair'): ").strip()

            if not q:
                continue

            if q.lower() in ["sair", "exit", "quit"]:
                print("Encerrando...")
                break

            results = search(q, model, index, texts)

            contexts = [r[:500] for r, _ in results]

            answer = generate_answer(q, contexts)

            print("\nResposta:")
            print(answer)
            print("\nTrechos usados:")
            for r, score in results:
                print(f"[score: {score:.2f}] {r}")
            print()

        except KeyboardInterrupt:
            print("\nEncerrado pelo usuário.")
            break


if __name__ == "__main__":
    main()