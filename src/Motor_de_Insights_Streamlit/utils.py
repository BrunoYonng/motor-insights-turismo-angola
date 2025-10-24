
# Ficheiro utilitário - comentários simples.
import pandas as pd

def carregar_dados(caminho):
    # Lê um CSV e devolve um DataFrame
    df = pd.read_csv(caminho)
    return df
