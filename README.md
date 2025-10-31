# FTL BOOTCAMP - ANGOLA - GRUPO Nº 17 - Projecto Final
# Motor de Insights para Planeamento Turístico Sustentável
# Ano: 2025  
# Equipa: Abel Chimbua Wanda, Bruno Yonng Leopoldo, Dorivaldo Albano Manuel, Eliano Ricardo Tavares, José Arão, Liliane Patrícia Neto, Mário Délcio da Silva


# Descrição
O Motor de Insights é uma plataforma de apoio à decisão e gestão desenvolvida para o **Ministério do Turismo de Angola**, que integra:
**Análise de dados turísticos**, **Previsões inteligentes** com *Machine Learning*, e uma **interface interativa web** para gestores públicos e analistas.
O sistema combina um **notebook analítico** (para geração e treino de modelos) com uma **versão web administrativa** desenvolvida em **Streamlit**, permitindo exploração, previsões e relatórios sobre o turismo sustentável em Angola.

# Objetivos Principais
- Centralizar e analisar dados turísticos nacionais.  
- Prever fluxos de visitantes e tendências sazonais.  
- Apoiar o planeamento económico e ambiental.  
- Promover a sustentabilidade no setor do turismo.

# Estrutura do Projeto
<img width="828" height="584" alt="Captura de Tela (42)" src="https://github.com/user-attachments/assets/45aaf46e-1baa-44dd-931c-fb0421f5b394" />

                      

# Instalação e Requisitos

### Dependências Principais
- Python ≥ 3.13  
- Pandas, Numpy: Para manipulação de dados.    
- Scikit-learn: Para modelagem preditiva (Random Forest, Regressão Linear)  
- Streamlit: para interface web interativa  
- Joblib: para facilitar e acelerar tarefas intensivas  
- Prophet / Statsmodels: para previsões temporais
- Matplotlib / Plotly: para visualização de dados  

Se quiser instalar todas as dependências de uma vez:
No seu cmd coloque o seguinte comando:
pip install -r requirements.txt

# Como executar o Projecto:
## 1º Faça download/fork do projecto na sua máquina;

## 2º Rodar o Python notebook, encontra-se em:
notebooks/motor-insights-turismo-angola.ipynb

## Instrução:
1. Abre o Jupyter Notebook ou VSCode.  
2. Executa todas as células em ordem.  
3. O notebook vai fazer o seguinte:
   - Gerar o dataset sintético ( em: data/raw/dados_sinteticos.csv);
   - Treinar o modelo RandomForest;
   - Avaliar as métricas (MAE, RMSE, R²);
   - Salvar o modelo em: src/Motor_de_Insights_Streamlit/models/modelo_sintetico.pkl.

Após a execução, o modelo e o dataset ficam prontos para uso no app Streamlit.

## 3º Executar a Aplicação Web (Streamlit)

### Passos:
1. No terminal, entra na pasta principal do projeto:
   cd src/Motor_de_Insights_Streamlit

2. Executa o app com este comando:
   streamlit run app.py
   
3. O Streamlit abrirá automaticamente no navegador (por padrão em:  
   http://localhost:8501)

##Para acessar a Área Administrativa
## Credenciais de Acesso

| Usuário     | Palavra-passe |
|--------------|----------------|
| admin        | @dorivalldo     |
| analista     | @brunoyonng     |
| analista1    | @lilianeneto    |

Os acessos e logouts ficam registados em `src/Motor_de_Insights_Streamlit/logs.csv.

# Funcionalidades Principais
✅ **Área Pública**
- Curiosidades turísticas, gastronomia e cultura.  
- Indicadores gerais (visitantes totais, taxa de ocupação média).  
- Links úteis para: (Governo de Angola, INE, PNUD, UNWTO).  

✅ **Área Administrativa (após login)**
- **Painel de Controlo** — métricas e indicadores principais.  
- **Explorar Dados** — filtro e visualização por província.  
- **Previsões** — previsão de visitantes futuros (modelo RandomForest).  
- **Comparar Províncias** — análise comparativa temporal.  
- **Sustentabilidade** — visualização de índices ambientais e mobilidade.  
- **Gerar Relatórios** — exportação (demo, pronto para PDF/DOCX/PPTX).  
- **Logs** — registo de sessões de utilizadores.

# Tecnologias Utilizadas
| Categoria | Tecnologias |
|------------|-------------|
| Linguagem  | Python |
| Análise de Dados | Pandas, NumPy, Scikit-learn |
| Visualização | Matplotlib, Streamlit Charts |
| Modelo de IA | RandomForestRegressor |
| Armazenamento | CSV, PKL (Joblib) |
| Interface Web | Streamlit |
| Documentação | Markdown / Notebook (Jupyter) |

# Fases de Desenvolvimento

| Fase | Descrição                           |         Resultado                           |
|------|-------------------------------------|---------------------------------------------|
| 1    | Planeamento e definição do problema | Estrutura conceptual                        |
| 2    | Levantamento de requisitos          | Variáveis e indicadores turísticos          |
| 3    | Modelo conceptual e tecnológico     | Fluxo de dados e arquitetura                |
| 4    | Preparação dos dados                | Criação de dataset sintético                |
| 5    | Modelagem e validação               | Modelos preditivos e métricas de desempenho |
| 6    | Implementação                       | Protótipo web interativo (Streamlit).       |

# Licença
Este projeto foi desenvolvido com fins académicos e de demonstração.  
Todos os dados sintéticos são simulados para uso educacional e não representam valores oficiais.
Este protótipo une ciência de dados, sustentabilidade e gestão pública — transformando informações em decisões inteligentes para o turismo angolano.

# Referências
Adepoju, A., & Akinsola, O. (2021). Digital transformation and tourism development in Sub-Saharan Africa. African Journal of Sustainable Development, 11(3), 45–62. 
Gunter, U., & Önder, I. (2022). Forecasting tourism demand with machine learning models: An empirical comparison. Tourism Management, 91, 104489. 
Hu, Y., & Song, H. (2023). Smart tourism governance and data-driven decision making. Journal of Sustainable Tourism, 31(4), 621–640. 
World Bank. (2023). International tourism, number of arrivals (Angola). World Development Indicators. 
UNDP. (2022). Digital transformation for sustainable development: Policy guidance for Africa. New York: United Nations Development Programme.
