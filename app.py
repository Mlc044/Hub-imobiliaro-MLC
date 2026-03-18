import streamlit as st

# --- IDENTIDADE DO CORRETOR ---
NOME_CORRETOR = "Mateus Lima Cerqueira"
CRECI_NUM = "29.705"

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Hub MLC - Gestão Imobiliária", layout="wide")

# 2. ESTILO VISUAL (TEMA CLARO E MODERNO - MATEUS LIMA)
st.markdown("""
    <style>
        /* Fundo claro e textos escuros */
        .stApp { background-color: #FFFFFF; color: #1E1E1E; }
        
        /* Barra lateral estilizada */
        [data-testid="stSidebar"] { background-color: #F8F9FA; border-right: 1px solid #E0E0E0; }
        
        /* Botões Arredondados e Modernos (Azul Marinho) */
        .stButton>button {
            border-radius: 25px;
            border: 2px solid #0E3B6C;
            background-color: #FFFFFF;
            color: #0E3B6C;
            font-weight: bold;
            padding: 10px 24px;
            transition: 0.3s;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #0E3B6C;
            color: #FFFFFF;
        }
        
        /* Card de Imóveis e Documentos */
        .doc-box {
            border: 1px solid #E0E0E0;
            padding: 25px;
            border-radius: 15px;
            background-color: #FDFDFD;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL COM A LOGO MLC (DOURADO E AZUL)
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; padding: 20px 0;">
            <div style="display: inline-block; width: 80px; height: 80px; background-color: #0E3B6C; border-radius: 50%; border: 3px solid #FFD700; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px;">
                <h1 style="color: #FFD700; margin: 0; font-family: sans-serif;">MLC</h1>
            </div>
            <h3 style="margin: 0; font-size: 1.1rem; color: #1E1E1E;">{NOME_CORRETOR}</h3>
            <p style="color: #0E3B6C; font-weight: bold; margin: 0;">CRECI {CRECI_NUM}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    modulo = st.radio("Navegação:", ["🛰️ Radar de Oportunidades", "📂 Documentos Prontos", "💰 Financeiro"])

# 4. MÓDULO: RADAR (COM LINKS DIRETOS)
if modulo == "🛰️ Radar de Oportunidades":
    st.title("🛰️ Radar de Oportunidades")
    st.subheader("Salvador, Lauro de Freitas e Região")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Buscar Leilões Caixa"):
            st.toast("Varrendo portais de leilão...")
            
    with col2:
        if st.button("📜 Buscar Licitações MEI"):
            st.toast("Consultando PNCP e Prefeituras...")

    # Exemplo de Resultado com Card e Link
    st.markdown('<div class="doc-box">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400")
    with c2:
        st.warning("**DESTAQUE:** Apartamento 3Q - Vilas do Atlântico")
        st.write("📍 Lauro de Freitas/BA | 💰 Lance Inicial: R$ 330.000,00")
        st.link_button("🌐 Abrir Página Oficial do Imóvel", "https://venda-imoveis.caixa.gov.br/")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MÓDULO: DOCUMENTOS (MODELO COMPLETO DE DOAÇÃO)
elif modulo == "📂 Documentos Prontos":
    st.title("📂 Fábrica de Documentos MLC")
    
    modelo = st.selectbox("Selecione o Modelo:", [
        "Escritura de Doação de Imóvel (Pai para Filho)",
        "Recibo de Honorários (6%)",
        "Proposta de Compra para Leilão"
    ])

    if modelo == "Escritura de Doação de Imóvel (Pai para Filho)":
        st.subheader("📝 Modelo de Escritura Pública de Doação")
        
        # Preenchimento Automático
        with st.expander("📌 Preencher Dados do Doador e Imóvel", expanded=True):
            col_pai, col_imo = st.columns(2)
            with col_pai:
                nome_pai = st.text_input("Nome do Pai (Doador):", "Ex: José Lima")
                cpf_pai = st.text_input("CPF do Pai:", "000.000.000-00")
                rg_pai = st.text_input("RG do Pai:", "0000000-00")
            with col_imo:
                end_imo = st.text_input("Endereço do Imóvel:", "Lauro de Freitas/BA")
                mat_imo = st.text_input("Nº da Matrícula:", "00000")
                cid_imo = st.text_input("Cidade do Cartório:", "Lauro de Freitas")

        # Visualização do Documento
        st.markdown(f"""
        <div class="doc-box">
            <h3 style="text-align: center;">ESCRITURA PÚBLICA DE DOAÇÃO DE BEM IMÓVEL</h3>
            <p><b>DOADOR:</b> {nome_pai}, brasileiro, portador do RG nº {rg_pai} e CPF nº {cpf_pai}.</p>
            <p><b>DONATÁRIO:</b> {NOME_CORRETOR}, brasileiro, corretor de imóveis, portador do CRECI {CRECI_NUM}.</p>
            <hr>
            <p><b>CLÁUSULA 1 – OBJETO:</b> Imóvel situado à {end_imo}, Matrícula nº {mat_imo} em {cid_imo}.</p>
            <p><b>CLÁUSULA 2 – DOAÇÃO:</b> Caráter irrevogável e irretratável (Antecipação de Legítima).</p>
            <p><b>CLÁUSULA 3 – IMPOSTO:</b> Registro condicionado ao pagamento do <b>ITCMD (Bahia)</b>.</p>
            <p><b>CLÁUSULA 4 – INCOMUNICABILIDADE:</b> O imóvel não se comunica com cônjuge do Donatário.</p>
            <p><b>CLÁUSULA 5 – IMPENHORABILIDADE:</b> O imóvel não poderá ser objeto de penhora por dívidas.</p>
            <br>
            <p style="text-align: center;">________________________________________________<br>Local e Data: {cid_imo}, BA</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        # Checklist e Dicas
        c_doc, c_passo = st.columns(2)
        with c_doc:
            st.markdown("""
            ### 📑 Checklist de Documentos
            - **Doador:** RG, CPF, Certidão Casamento (atualizada).
            - **Imóvel:** Matrícula Atualizada, Certidão de Ônus, IPTU.
            """)
        with c_passo:
            st.markdown("""
            ### 🚀 Fluxo Prático
            1. Escritura de Compra e Doação simultânea.
            2. Guia de ITCMD (SEFAZ-BA).
            3. Registro no Cartório de Imóveis.
            """)

# 6. MÓDULO: FINANCEIRO
elif modulo == "💰 Financeiro":
    st.title("💰 Gestão Financeira")
    st.metric("Comissão Prevista (Corretagem)", "R$ 15.000,00", "5%")