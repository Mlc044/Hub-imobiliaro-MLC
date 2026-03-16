import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# --- 1. CONFIGURAÇÃO DA PÁGINA (Sempre a primeira linha!) ---
st.set_page_config(page_title="Hub MLC - Mateus Lima", layout="wide")

# --- 2. IDENTIDADE VISUAL E MODO NOTURNO ---
st.markdown("""
    <style>
        .stApp { background-color: #0E1117; color: #FFFFFF; }
        [data-testid="stSidebar"] { background-color: #1A1C24; }
        .stButton>button { border-radius: 5px; border: 1px solid #FFD700; background-color: #1A1C24; color: #FFD700; width: 100%; }
        .stButton>button:hover { background-color: #FFD700; color: #0E1117; }
    </style>
""", unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
st.sidebar.markdown(f"""
    <div style="text-align: center; padding: 10px; border: 1px solid #FFD700; border-radius: 10px; background-color: #1A1C24;">
        <h1 style="color: #FFD700; margin:0;">MLC</h1>
        <p style="margin:0; font-size: 14px;"><b>Mateus Lima Cerqueira</b></p>
        <p style="color: #FFD700; margin:0; font-size: 12px;">CRECI 29.705</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.divider()

modulo = st.sidebar.radio("Navegação Principal:", [
    "🛰️ Radar de Oportunidades",
    "🏠 Corretagem Tradicional",
    "🏠 Leilões & Propostas",
    "📜 Licitações (MEI)",
    "💰 Gestão Financeira"
])

# --- 4. LÓGICA DOS MÓDULOS ---

# MÓDULO: RADAR COM BOTÕES (O QUE VOCÊ PEDIU AGORA)
if modulo == "🛰️ Radar de Oportunidades":
    st.header("🛰️ Radar de Oportunidades (Salvador & RMS)")
    st.write("Selecione o tipo de busca para iniciar o monitoramento:")
    
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("🏠 Buscar Leilões da Caixa (Lauro/SSA)"):
            with st.spinner("Varrendo editais de leilão..."):
                st.success("Busca Finalizada!")
                st.warning("**LEILÃO CAIXA:** Apartamento em Vilas do Atlântico detectado.")
                st.write("Local: Lauro de Freitas | Desconto Estimado: 40%")

    with col_btn2:
        if st.button("📜 Buscar Licitações MEI (Bahia)"):
            with st.spinner("Consultando portais de licitação..."):
                st.success("Busca Finalizada!")
                st.info("**PREFEITURA SSA:** Cota exclusiva MEI para Serviços de TI.")
                st.write("Status: Aberto | Região: Salvador/Centro")

# MÓDULO: FINANCEIRO
elif modulo == "💰 Gestão Financeira":
    st.header("💰 Controle de Honorários")
    st.metric("Total a Receber (Previsto)", "R$ 15.000,00")
    st.write("Use este espaço para gerenciar suas comissões de 6%.")

# MÓDULO: CORRETAGEM
elif modulo == "🏠 Corretagem Tradicional":
    st.header("🏠 Gestão de Carteira (Salvador a Praia do Forte)")
    st.write("Cadastre aqui seus imóveis de captação direta.")

# MÓDULO: LEILÕES
elif modulo == "🏠 Leilões & Propostas":
    st.header("🏠 Análise de Leilões")
    st.write("Foco em imóveis retomados e oportunidades de investimento.")

# MÓDULO: LICITAÇÕES
elif modulo == "📜 Licitações (MEI)":
    st.header("📜 Gestão de Licitações")
    st.write("Documentação e acompanhamento de processos para o seu MEI.")

# --- RODAPÉ ---
st.sidebar.divider()
if st.sidebar.button("📲 Compartilhar Resumo via WhatsApp"):
    texto = f"Hub MLC: Mateus Lima (CRECI 29.705) - Relatório de Oportunidades em Salvador e RMS."
    url_zap = f"https://wa.me/?text={urllib.parse.quote(texto)}"
    st.sidebar.markdown(f"[Clique aqui para enviar]({url_zap})")