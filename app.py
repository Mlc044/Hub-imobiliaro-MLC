import streamlit as st

# --- IDENTIDADE DO CORRETOR ---
NOME_CORRETOR = "Mateus Lima Cerqueira"
CRECI_NUM = "29.705"

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Hub MLC - Gestão Imobiliária", layout="wide")

# 2. ESTILO VISUAL (MODO CLARO E MODERNO)
st.markdown("""
    <style>
        .stApp { background-color: #FFFFFF; color: #1E1E1E; }
        [data-testid="stSidebar"] { background-color: #F0F2F6; border-right: 1px solid #E0E0E0; }
        .stButton>button { 
            border-radius: 20px; border: 2px solid #0E3B6C; 
            background-color: #FFFFFF; color: #0E3B6C; font-weight: bold; width: 100%;
        }
        .stButton>button:hover { background-color: #0E3B6C; color: #FFFFFF; }
        .doc-box { border: 1px solid #E0E0E0; padding: 20px; border-radius: 15px; background-color: #F8F9FA; }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL COM LOGO MLC
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; padding: 20px 0;">
            <div style="display: inline-block; width: 70px; height: 70px; background-color: #0E3B6C; border-radius: 50%; border: 3px solid #FFD700; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                <h2 style="color: #FFD700; margin: 0;">MLC</h2>
            </div>
            <h3 style="margin: 0; font-size: 1.1rem;">{NOME_CORRETOR}</h3>
            <p style="color: #0E3B6C; font-weight: bold;">CRECI {CRECI_NUM}</p>
        </div>
    """, unsafe_allow_html=True)
    st.divider()
    modulo = st.radio("Navegação", ["🛰️ Radar de Oportunidades", "📂 Documentos Prontos", "💰 Financeiro"])

# 4. MÓDULO: RADAR (COM LINKS DIRETOS)
if modulo == "🛰️ Radar de Oportunidades":
    st.title("🛰️ Radar de Oportunidades")
    st.info("Busca ativa em Salvador, Lauro de Freitas e Linha Verde.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Ver Leilões Disponíveis"):
            st.success("Imóvel em Vilas do Atlântico detectado!")
            st.link_button("🌐 Abrir no Portal Oficial", "https://venda-imoveis.caixa.gov.br/")
    with col2:
        if st.button("📜 Ver Licitações MEI"):
            st.info("Editais abertos na Prefeitura de Salvador.")
            st.link_button("🌐 Abrir Portal de Compras", "https://www.compras.salvador.ba.gov.br/")

# 5. MÓDULO: DOCUMENTOS (MODELOS PRONTOS)
elif modulo == "📂 Documentos Prontos":
    st.title("📂 Fábrica de Documentos MLC")
    st.write("Selecione um modelo para gerar o texto profissional:")

    modelo = st.selectbox("Escolha o Modelo:", [
        "Minuta de Doação de Imóvel (Pais para Filho)",
        "Proposta de Compra para Leilão",
        "Recibo de Honorários (6%)",
        "Contrato de Consultoria Imobiliária"
    ])

    st.divider()
    
    with st.container():
        st.markdown('<div class="doc-box">', unsafe_allow_html=True)
        col_doc1, col_doc2 = st.columns(2)
        
        with col_doc1:
            cliente = st.text_input("Nome do Cliente/Envolvido:", "Ex: João Silva")
            valor = st.text_input("Valor da Transação (R$):", "0.00")
        with col_doc2:
            documento = st.text_input("CPF/CNPJ:", "000.000.000-00")
            endereco = st.text_input("Endereço do Imóvel:", "Lauro de Freitas/BA")

        # GERAÇÃO AUTOMÁTICA DO TEXTO CONFORME O MODELO
        if modelo == "Minuta de Doação de Imóvel (Pais para Filho)":
            texto_final = f"""📝 **MINUTA DE DOAÇÃO**
            
Pelo presente instrumento, os DOADORES declaram a intenção de transferir a propriedade situada em {endereco} para o DONATÁRIO {cliente}, inscrito no CPF {documento}. 
A presente doação é feita como antecipação de legítima, com a consultoria técnica de {NOME_CORRETOR} (CRECI {CRECI_NUM})."""

        elif modelo == "Recibo de Honorários (6%)":
            texto_final = f"""📝 **RECIBO DE HONORÁRIOS**
            
Recebi de {cliente}, portador do CPF {documento}, a importância de R$ {valor}, referente aos honorários de corretagem (6%) pela intermediação do imóvel em {endereco}.
Assinado: {NOME_CORRETOR} - CRECI {CRECI_NUM}."""

        else:
            texto_final = "Modelo em fase de preenchimento..."

        st.markdown(texto_final)
        st.button("📋 Copiar Texto para o WhatsApp")
        st.markdown('</div>', unsafe_allow_html=True)

# 6. MÓDULO: FINANCEIRO
elif modulo == "💰 Financeiro":
    st.title("💰 Gestão Financeira")
    st.metric("Comissão Prevista (5%)", "R$ 15.000,00")