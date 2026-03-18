import streamlit as st
from fpdf import FPDF
import urllib.parse

# --- CONFIGURAÇÕES BÁSICAS ---
NOME_COMPLETO = "Mateus Lima Cerqueira"
CRECI_NUM = "29.705"

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Hub MLC - Mateus Lima", layout="wide")

# --- 2. ESTILO VISUAL (TEMA CLARO E MODERNO) ---
st.markdown("""
    <style>
        .stApp { background-color: #FFFFFF; color: #333333; }
        [data-testid="stSidebar"] { background-color: #F8F9FA; border-right: 1px solid #E0E0E0; }
        .stButton>button { 
            border-radius: 20px; 
            border: 1px solid #0E3B6C; 
            background-color: #FFFFFF; 
            color: #0E3B6C; 
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover { background-color: #0E3B6C; color: #FFFFFF; }
        .property-card { 
            border: 1px solid #E0E0E0; 
            padding: 15px; 
            border-radius: 15px; 
            margin-bottom: 20px; 
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. BARRA LATERAL COM SUA LOGO MLC ---
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; padding: 20px 0;">
            <div style="display: inline-block; width: 80px; height: 80px; background-color: #0E3B6C; border-radius: 50%; border: 3px solid #FFD700; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px;">
                <h1 style="color: #FFD700; margin: 0; font-size: 1.8rem;">MLC</h1>
            </div>
            <h3 style="color: #333333; margin:0; font-size: 1.1rem;">{NOME_COMPLETO}</h3>
            <p style="color: #0E3B6C; margin:0; font-weight: bold;">CRECI {CRECI_NUM}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    modulo = st.radio("Selecione o Módulo:", 
                     ["🛰️ Radar de Oportunidades", "📂 Modelos de Documentos", "💰 Financeiro"])

# --- 4. LÓGICA DO RADAR (VISUAL NOVO) ---
if modulo == "🛰️ Radar de Oportunidades":
    st.title("🛰️ Radar de Oportunidades")
    st.subheader("Salvador, Lauro de Freitas e Região")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🏠 Buscar Leilões Caixa"):
            st.session_state.busca = "caixa"
    with col2:
        if st.button("📜 Buscar Licitações MEI"):
            st.session_state.busca = "mei"

    # Exemplo de resultado com o botão de link direto
    st.markdown('<div class="property-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400")
    with c2:
        st.info("**DESTAQUE:** Apartamento em Vilas do Atlântico")
        st.write("📍 Lauro de Freitas/BA | 💰 Lance: R$ 330.000,00")
        st.link_button("🌐 Abrir no Site Oficial", "https://venda-imoveis.caixa.gov.br/")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. MODELOS DE DOCUMENTOS ---
elif modulo == "📂 Modelos de Documentos":
    st.title("📂 Modelos de Documentos")
    st.write("Em breve: Minutas de doação e recibos personalizados.")

# --- 6. FINANCEIRO ---
elif modulo == "💰 Financeiro":
    st.title("💰 Gestão Financeira")
    st.metric("Comissões Previstas", "R$ 15.000,00", "6%")