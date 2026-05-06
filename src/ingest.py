import pandas as pd

def load_data(path):
    df = pd.read_csv(path, sep=';', encoding='latin-1')

    texts = (
        df['Objeto'].astype(str) + " | Órgão: " + df['Nome Órgão']
    ).dropna().tolist()

    return texts[:5000]