
# Motor de Insights - Protótipo Streamlit
# Comentários simples, estilo aprendiz.

import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime
from PIL import Image

logo = Image.open("assets/brasao_angola.png")
modelo = joblib.load("models/modelo_demo.pkl")

def fake_prophet_forecast(serie, periods=6):
    last = serie[-12:]
    base = np.mean(last)
    season = np.sin(np.linspace(0, 2*np.pi, periods)) * (np.std(last)/4)
    return (base + season).round().astype(int).tolist()

st.set_page_config(page_title="Motor de Insights - Demo", layout="wide")
col1, col2 = st.columns([1,6])
with col1:
    st.image(logo, width=150)
with col2:
    st.title("Motor de Insights para Planeamento Turístico Sustentável")
    st.caption("Protótipo institucional - Acesso reservado aos técnicos do Ministério")

st.sidebar.title("Acesso")
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    usuario = st.sidebar.text_input("Usuário")
    senha = st.sidebar.text_input("Senha", type="password")
    if st.sidebar.button("Iniciar Sessão"):
        if usuario == "gestor" and senha == "turista123":
            st.session_state['autenticado'] = True
            st.experimental_rerun()
        else:
            st.sidebar.error("Credenciais inválidas - demo")
else:
    st.sidebar.success("Autenticado como gestor")

if not st.session_state['autenticado']:
    st.info("Por favor inicie sessão com credenciais administrativas para aceder ao portal (demo).")
    st.stop()

menu = st.sidebar.radio("Menu", ["Página Inicial","Painel de Turismo","Previsões","Relatórios","Gestão Administrativa"])
df = pd.read_csv("data_demo.csv")
df['data'] = pd.to_datetime(df['data'])

if menu == "Página Inicial":
    st.header("Página Inicial")
    st.write("Bem-vindo ao Motor de Insights. Esta demonstração mostra como o portal pode ajudar o Ministério a tomar decisões.")
    st.markdown("- Ferramenta: previsões, dashboards e relatórios\n- Utilidade: apoiar planeamento sustentável e económico")

elif menu == "Painel de Turismo":
    st.header("Painel de Turismo")
    st.write("Indicadores principais por província.")
    prov = st.selectbox("Escolha a província", ["Todas"] + sorted(df['provincia'].unique().tolist()))
    if prov != "Todas":
        dfp = df[df['provincia']==prov]
    else:
        dfp = df.copy()
    col1, col2, col3 = st.columns(3)
    col1.metric("Visitantes (último mês)", int(dfp['visitantes'].iloc[-1]))
    col2.metric("Ocupação (%)", f"{dfp['ocupacao_hoteleira'].iloc[-1]:.1f}")
    col3.metric("Receita Total (Kz)", f"{dfp['receita_total'].iloc[-1]:.0f}")
    st.line_chart(dfp.set_index('data')[['visitantes','ocupacao_hoteleira']])

elif menu == "Previsões":
    st.header("Previsões")
    st.write("Gerar previsões de visitantes e taxa de ocupação (demo).")
    prov = st.selectbox("Província para previsão", sorted(df['provincia'].unique().tolist()))
    periodo = st.number_input("Meses para frente", min_value=1, max_value=12, value=6)
    if st.button("Gerar Previsão"):
        dfr = df[df['provincia']==prov].sort_values('data')
        visitantes_series = dfr['visitantes'].values
        forecast = fake_prophet_forecast(visitantes_series, periods=periodo)
        st.subheader(f"Previsão de visitantes para {prov} (próximos {periodo} meses)")
        st.write(forecast)
        st.subheader("Previsão de ocupação (estimativa pelo modelo demo)")
        last = dfr.iloc[-1]
        occ = float(last['ocupacao_hoteleira'])
        recpc = float(last['receita_total']/last['visitantes'])
        saz = float(dfr['visitantes'].pct_change().fillna(0).iloc[-1])
        Xnew = np.array([[occ, recpc, saz]])
        pred_visit = modelo.predict(Xnew)[0]
        st.write(f"Estimativa visitantes próxima época: {int(pred_visit)}")

elif menu == "Relatórios":
    st.header("Relatórios")
    st.write("Gerar e exportar relatórios (CSV).")
    prov = st.selectbox("Província para relatório", ["Todas"] + sorted(df['provincia'].unique().tolist()))
    if st.button("Exportar CSV"):
        if prov == "Todas":
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV - Dados completos", data=csv, file_name="relatorio_turismo.csv")
        else:
            csv = df[df['provincia']==prov].to_csv(index=False).encode('utf-8')
            st.download_button(f"Download CSV - {prov}", data=csv, file_name=f"relatorio_{prov}.csv")

elif menu == "Gestão Administrativa":
    st.header("Gestão Administrativa")
    st.write("Área para gerir utilizadores e logs. (Funcionalidade simulada)")
    st.write("Usuários administrativos (demo): gestor")
    if st.button("Ver logs (demo)"):
        st.write("Logs de acesso - demonstração:")
        st.write({"usuario":"gestor","acao":"login","horario":str(datetime.now())})
