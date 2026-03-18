import streamlit as st
import urllib.parse

# --- 1. CONFIGURAÇÃO (Sempre a primeira linha!) ---
st.set_page_config(page_title="Hub MLC - Mateus Lima", layout="wide")

# --- 2. IDENTIDADE VISUAL ---
st.markdown("""
    <style>
        .stApp { background-color: #0E1117; color: #FFFFFF; }
        [data-testid="stSidebar"] { background-color: #1A1C24; }
        .stButton>button { border-radius: 5px; border: 1px solid #FFD700; background-color: #1A1C24; color: #FFD700; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- 3. MENU LATERAL (AQUI DEFINIMOS A VARIÁVEL 'MODULO') ---
st.sidebar.markdown(f"""
    <div style="text-align: center; padding: 10px; border: 1px solid #FFD700; border-radius: 10px;">
        <h2 style="color: #FFD700; margin:0;">MLC</h2>
        <p style="margin:0;"><b>Mateus Lima Cerqueira</b></p>
        <p style="color: #FFD700; margin:0;">CRECI 29.705</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.divider()

# Variável 'modulo' criada ANTES de ser usada
modulo = st.sidebar.radio("Navegação:", [
    "🛰️ Radar de Oportunidades",
    "🏠 Leilões & Propostas",
    "💰 Gestão Financeira"
])

# --- 4. LÓGICA DO RADAR (DIRETO PARA OS SITES) ---
if modulo == "🛰️ Radar de Oportunidades":
    st.header("🛰️ Radar de Oportunidades (Salvador & RMS)")
    
    col1, col2 = st.columns(2)
    with col1:
        btn_imoveis = st.button("🏠 Buscar Leilões (Caixa/Leiloeiros)")
    with col2:
        btn_mei = st.button("📜 Buscar Licitações (MEI)")

    if btn_imoveis:
        st.subheader("📍 Oportunidades em Salvador e Lauro de Freitas")
        
        # CARD CAIXA
        with st.container(border=True):
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=300", caption="Leilão Caixa")
            with c2:
                st.warning("**LEILÃO CAIXA ECONÔMICA**")
                st.write("📍 Filtro: Imóveis Retomados na Bahia")
                st.link_button("🌐 Abrir Portal de Imóveis Caixa", "https://venda-imoveis.caixa.gov.br/sistema/busca-imovel.asp?sEstado=BA")

        # CARD LEILOEIRO OFICIAL (BAHIA)
        with st.container(border=True):
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image("https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=300", caption="Leiloeiros BA")
            with c2:
                st.warning("**LEILOEIROS OFICIAIS - BAHIA**")
                st.write("📍 Oportunidades em Lauro de Freitas e Linha Verde")
                st.link_button("🌐 Ver Leilões Judiciais/Extrajudiciais", "https://www.rjleiloes.com.br/")

    if btn_mei:
        st.subheader("🏢 Licitações para o seu MEI")
        with st.container(border=True):
            st.info("**PORTAL NACIONAL DE CONTRATAÇÕES (PNCP)**")
            st.write("📍 Filtro: Oportunidades em Salvador e Camaçari")
            st.link_button("🌐 Abrir PNCP (Editais Abertos)", "https://www.gov.br/pncp/pt-br")

# --- OUTROS MÓDULOS ---
elif modulo == "🏠 Leilões & Propostas":
    st.header("🏠 Gestão de Propostas (CRECI 29.705)")
    st.write("Área para análise técnica de viabilidade.")

elif modulo == "💰 Gestão Financeira":
    st.header("💰 Controle de Comissões")
    st.write("Gestão de honorários (6% corretagem / Taxas MEI).")