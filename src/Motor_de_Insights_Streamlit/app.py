
import streamlit as st
from pathlib import Path
from datetime import datetime
import pandas as pd, numpy as np
from utils import carregar_dados, carregar_modelo, prever, log_user, read_logs

# Page config
st.set_page_config(page_title="Ministério do Turismo - Motor de Insights", layout="wide", initial_sidebar_state="expanded")

# Simple CSS for styling and responsiveness
st.markdown(
    """
    <style>
    /* Header styles */
    .header-title {font-size:30px; font-weight:700; margin-bottom:0;}
    .header-sub {font-size:16px; margin-top:0;color: #2b7a4b;}
    .stApp { background-color: #ffffff; }
    /* Sidebar */
    .sidebar .sidebar-content {background-image: linear-gradient(#ffffff, #f4f8f6);} 
    /* Make charts responsive */
    .chart-container {width:100%;height:auto;}
    /* smaller text for footers */
    .small {font-size:12px;color:gray;}
    </style>
    """, unsafe_allow_html=True
)

# Multi-language support (basic)
LANG = st.sidebar.selectbox("Idioma / Language", ["PT","EN"])
TEXT = {
    "PT":{
        "title":"Ministério do Turismo",
        "subtitle":"Motor de Insights - Planejamento e Turismo Sustentável",
        "public":"Área Pública",
        "admin":"Área Administrativa",
        "explore":"Explorar Dados",
        "predict":"Previsões",
        "compare":"Comparar Províncias",
        "sustain":"Sustentabilidade",
        "reports":"Gerar Relatórios",
        "links":"Links Úteis",
        "terms":"Termos e Condições",
        "register":"Registar",
        "login":"Iniciar Sessão",
        "logout":"Terminar Sessão"
    },
    "EN":{
        "title":"Ministry of Tourism",
        "subtitle":"Insights Engine - Planning and Sustainable Tourism",
        "public":"Public Area",
        "admin":"Administrative Area",
        "explore":"Explore Data",
        "predict":"Predictions",
        "compare":"Compare Provinces",
        "sustain":"Sustainability",
        "reports":"Generate Reports",
        "links":"Useful Links",
        "terms":"Terms and Conditions",
        "register":"Register",
        "login":"Sign In",
        "logout":"Sign Out"
    }
}
t = TEXT[LANG]

# Header with logo left, title center, UNDP logo right
col1, col2, col3 = st.columns([1,5,1])
with col1:
    ""
    st.image("assets/insignia_angola.png", width=120)
with col2:
    ""
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <div class='header-title'>{t['title']}</div>
            <div class='header-sub'>{t['subtitle']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
with col3:
    ""
    st.image("assets/UNDP_logo.png", width=120)

st.write("")

# top navigation choices
area_mode = st.selectbox("", [t["public"], t["admin"]], index=0, key="area_mode")

# show datetime in top-right-ish area (simple)
st.markdown(f"<div class='small'>Data / Hora (UTC): {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}</div>", unsafe_allow_html=True)

# Hardcoded credentials for demo
USERS = {"admin":"@dorivalldo", "analista":"@brunoyonng", "analista1":"@lilianeneto"}
USER_NAMES = {"admin":"Admin", "analista":"Bruno Yonng", "analista1":"Liliane Neto"}

# PUBLIC AREA
if area_mode == t["public"]:
    st.header("Informações de Acesso Público")
    # Two-column responsive section: left content, right quick stats
    c1, c2 = st.columns([3,1])
    with c1:
        st.markdown("### Destaques e Pontos Turísticos")
        st.markdown("- **Praia do Cabo Ledo** (Namibe) — excelente para surf e ecoturismo")
        st.markdown("- **Parque Nacional da Kissama** — safaris e conservação")
        st.markdown("- **Festival Nacional de Música** — eventos culturais sazonais")
        st.markdown("### Gastronomia")
        st.markdown("Pratos típicos: Calulu, Muamba, Funje com peixe. Descubra receitas e rotas gastronômicas regionais.")
    with c2:
        df = carregar_dados()
        total_visitors = int(df['visitors'].sum())
        avg_occup = df['occupancy_rate'].mean().round(1)
        st.metric("Visitantes totais (2018-2024)", f"{total_visitors:,}")
        st.metric("Ocupação média", f"{avg_occup}%")
        st.markdown("### Links úteis")
        st.markdown("[Governo de Angola](https://https://governo.gov.ao)", unsafe_allow_html=True)
        st.markdown("[INE](https://www.ine.gov.ao)", unsafe_allow_html=True)
        st.markdown("[PNUD](https://www.undp.org)", unsafe_allow_html=True)
        st.markdown("[UNWTO](https://www.unwto.org)", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Explorar por Província")
    prov_select = st.selectbox("Escolha província", sorted(df['province'].unique()))
    prov_df = df[df['province']==prov_select]
    st.line_chart(prov_df.set_index('date')[['visitors']].resample('M').sum())

    st.markdown("---")
    st.markdown("**Termos e Condições** | **Idioma:** PT / EN ")
    st.markdown("**Registar** (Em andamento) | **Esqueci minha senha** (Em andamento)")

# ADMIN AREA (requires login)
else:
    st.header("Área Administrativa")
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.login_time = None

    if not st.session_state.logged_in:
        # login box centered
        lw1, lw2, lw3 = st.columns([1,2,1])
        with lw2:
            st.markdown("Insira suas credenciais de acesso.")
            username = st.text_input("Usuário")
            password = st.text_input("Palavra-passe", type="password")
            if st.button("Entrar"):
                if username in USERS and USERS[username] == password:
                    st.session_state.logged_in = True
                    st.session_state.user = username
                    st.session_state.login_time = datetime.utcnow().isoformat()
                    log_user(username, action="login")
                    st.success(f"Bem-vindo, {USER_NAMES.get(username, username)}")
                else:
                    st.error("Credenciais inválidas")
            st.markdown("[Registar novo usuário (Em andamento)](#)")
            st.markdown("[Esqueci minha senha (Em andamento)](#)")
    else:
        # Admin layout with top tabs
        user_display = USER_NAMES.get(st.session_state.user, st.session_state.user)
        st.sidebar.markdown(f"**Usuário:** {user_display}")
        if st.sidebar.button("Terminar Sessão"):
            log_user(st.session_state.user, action="logout")
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

        tabs = st.tabs(["Painel","Explorar Dados","Previsões","Comparar Províncias","Sustentabilidade","Relatórios","Logs"])
        df = carregar_dados()
        model, scaler, features = carregar_modelo()

        # Painel (KPIs)
        with tabs[0]:
            st.subheader("Painel de Controle")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Visitantes (total)", f"{int(df['visitors'].sum()):,}")
            col2.metric("Receita (estimada)", f"${int(df['revenue'].sum()):,}")
            col3.metric("Ocupação média", f"{df['occupancy_rate'].mean():.1f}%")
            col4.metric("Eventos (total)", f"{int(df['events_count'].sum()):,}")
            st.markdown("Visão rápida por província")
            top_prov = df.groupby('province').visitors.sum().sort_values(ascending=False).head(8)
            st.bar_chart(top_prov)

        # Explorar Dados
        with tabs[1]:
            st.subheader("Exploração de Dados")
            provs = sorted(df['province'].unique())
            sel = st.multiselect("Provincias", provs, default=provs[:3])
            filt = df[df['province'].isin(sel)]
            st.dataframe(filt[['date','province','visitors','occupancy_rate','revenue']].sort_values(['province','date']).head(500))
            st.line_chart(filt.groupby('date').visitors.sum())

        # Previsões
        with tabs[2]:
            st.subheader("Previsões (Em andamento)")
            prov = st.selectbox("Província", sorted(df['province'].unique()), key="previsoes_provincia")
            sample = df[df['province']==prov].sort_values('date').tail(1)
            st.write("Parâmetros atuais (último registo):")
            st.write(sample[["visitors","occupancy_rate","revenue","mobility_index","env_index","events_count"]])
            occ = st.number_input("Occupancy rate", value=float(sample['occupancy_rate'].iloc[0]))
            rev = st.number_input("Revenue", value=float(sample['revenue'].iloc[0]))
            mob = st.number_input("Mobility index", value=float(sample['mobility_index'].iloc[0]))
            env = st.number_input("Env index", value=float(sample['env_index'].iloc[0]))
            ev = st.number_input("Events count", value=int(sample['events_count'].iloc[0]))
            input_df = pd.DataFrame([{
                "visitors_lag1": sample["visitors"].iloc[0],
                "occupancy_rate": occ,
                "revenue_per_visitor": rev,      
                "mobility_index": mob,
                "env_index": env,
                "events_count": ev,
                "tourist_density":  np.random.uniform(0.01, 0.05)  
            }])
            pred = prever(model, scaler, features, input_df)[0]
            st.metric("Previsão de visitantes (próximo mês)", int(pred))

        # Comparar Províncias
        with tabs[3]:
            st.subheader("Comparar Províncias")
            sel = st.multiselect(
                "Escolha até 2 províncias",
                sorted(df['province'].unique()), default=sorted(df['province'].unique())[:2], max_selections=2, key="comparar_provincias"
            )
            if len(sel) >= 2:
                a, b = sel[:2]
                g1 = df[df['province']==a].groupby(df['date'].dt.year).visitors.sum()
                g2 = df[df['province']==b].groupby(df['date'].dt.year).visitors.sum()
                comp = pd.concat([g1.rename(a), g2.rename(b)], axis=1)
                st.line_chart(comp.fillna(0))

        # Sustentabilidade
        with tabs[4]:
            st.subheader("Sustentabilidade")
            prov = st.selectbox("Província", sorted(df['province'].unique()), key="sustentabilidade_provincia")
            samp = df[df['province']==prov].tail(36)
            samp = samp.set_index('date')
            st.line_chart(samp[['env_index','mobility_index']])

        # Relatórios
        with tabs[5]:
            st.subheader("Gerar Relatórios")
            st.markdown("Formato de relatório: PDF, Word (.docx) ou PowerPoint (.pptx)")
            fmt = st.selectbox("Formato", ["PDF","Word","PPTX"])
            if st.button("Gerar Relatório (Em andamento)"):
                st.success(f"Relatório {fmt} gerado (Em andamento). Implementação em utils disponível para futura integração.")

        # Logs
        with tabs[6]:
            st.subheader("Registos de Sessão")
            logs = read_logs()
            if len(logs) == 0:
                st.info("Sem registos.")
            else:
                df_logs = pd.DataFrame(logs, columns=["timestamp","user","action"])
                st.dataframe(df_logs.tail(50).sort_values("timestamp", ascending=False))
