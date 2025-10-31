import pandas as pd, joblib, os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "raw" / "dados_sinteticos.csv"
MODEL_PATH = ROOT / "src" / "Motor_de_Insights_Streamlit" / "models" / "modelo_sintetico.pkl"
LOG_PATH = ROOT / "src" / "Motor_de_Insights_Streamlit" / "logs.csv"

def carregar_dados():
    return pd.read_csv(DATA_PATH, parse_dates=["date"])

import joblib
import os
from pathlib import Path

def carregar_modelo():
    # Caminho dinâmico baseado no local deste arquivo
    base_path = Path(__file__).resolve().parent
    model_path = base_path / "models" / "modelo_sintetico.pkl"

    # Mostra o caminho real no terminal para debug
    print(f"Tentando carregar modelo de: {model_path}")

    # Verifica se o arquivo existe
    if not model_path.exists():
        raise FileNotFoundError(f"Modelo não encontrado em: {model_path}")

    # Carrega o modelo
    info = joblib.load(model_path)

    # Garante compatibilidade com dict ou objeto direto
    if isinstance(info, dict):
        return info.get("model"), info.get("scaler"), info.get("features", [])
    else:
        return info, None, []
    #Previsão
import numpy as np

def prever(model, scaler, features, input_df):
    try:
        # Seleciona apenas as colunas que existem no modelo
        X = input_df[features].values if features else input_df.values

        # Aplica o scaler somente se ele existir
        if scaler is not None:
            Xs = scaler.transform(X)
        else:
            Xs = X  # usa os valores brutos

        # Faz a previsão
        preds = model.predict(Xs)
        return preds

    except Exception as e:
        print(f"Erro durante previsão: {e}")
        return [0]
#Login
def log_user(username, action="login"):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    ts = datetime.utcnow().isoformat()
    line = f"{ts},{username},{action}\n"
    with open(LOG_PATH, "a") as f:
        f.write(line)

def read_logs():
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH,"r") as f:
        rows = [r.strip().split(",") for r in f if r.strip()]
    return rows
