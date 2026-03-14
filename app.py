import streamlit as st
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÃO DA PÁGINA (Sempre a primeira linha!)
st.set_page_config(page_title="Hub MLC - Mateus Lima", layout="wide")

# 2. IDENTIDADE VISUAL NA BARRA LATERAL
st.sidebar.markdown(f"""
    <div style="text-align: center; padding: 10px; border: 1px solid #FFD700; border-radius: 10px;">
        <h2 style="color: #FFD700; margin:0;">MLC</h2>
        <p style="margin:0;"><b>Mateus Lima Cerqueira</b></p>
        <p style="color: #FFD700; margin:0;">CRECI 29.705</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.divider()

# 3. DEFINIÇÃO DO MENU (Aqui a variável 'modulo' é criada)
modulo = st.sidebar.radio("Navegação:", [
    "🛰️ Radar de Oportunidades",
    "🏠 Leilões & Propostas",
    "💰 Gestão Financeira",
    "📂 Fábrica de Documentos"
])

# 4. LÓGICA DOS MÓDULOS (O Python já sabe o que é 'modulo')
if modulo == "🛰️ Radar de Oportunidades":
    st.header("🛰️ Radar de Oportunidades - Salvador e RMS")
    st.write("Buscando editais em Lauro de Freitas, Salvador e Praia do Forte...")
    st.info("Dica: Use este módulo antes dos estudos para a PF para ganhar tempo!")

elif modulo == "🏠 Leilões & Propostas":
    st.header("🏠 Gestão de Leilões (CRECI 29.705)")
    st.write("Analise imóveis da Caixa aqui.")

elif modulo == "💰 Gestão Financeira":
    st.header("💰 Controle de Comissões e Honorários")
    st.metric("Meta Mensal", "R$ 15.000,00", delta="Faltam R$ 5.000")

elif modulo == "📂 Fábrica de Documentos":
    st.header("📂 Gerador de Documentos Profissionais")
    st.write("Gere minutas de doação e aluguel aqui.")