import streamlit as st
import urllib.parse
from fpdf import FPDF
import base64

# --- 1. CONFIGURAÇÃO DA PÁGINA (Sempre a primeira linha!) ---
st.set_page_config(page_title="Hub MLC - Mateus Lima (CRECI 29.705)", layout="wide")

# --- 2. ESTILO VISUAL (TEMA CLARO E BOTÕES MODERNOS - ADAPTADO DE image_0.png) ---
st.markdown("""
    <style>
        .stApp { background-color: #FFFFFF; color: #333333; }
        [data-testid="stSidebar"] { background-color: #F8F9FA; border-right: 1px solid #E0E0E0; }
        
        # --- ESTILO PARA BOTÕES DE NAVEGAÇÃO MODERNOS (SIMULANDO O MOBILE) ---
        .nav-btn {
            background-color: #E6EEF5; 
            border: 2px solid #E6EEF5;
            color: #0E3B6C;
            border-radius: 12px;
            padding: 10px 15px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: start;
            margin-bottom: 12px;
            transition: all 0.3s;
            cursor: pointer;
        }
        .nav-btn:hover {
            background-color: #0E3B6C;
            color: #FFFFFF;
            border: 2px solid #0E3B6C;
        }
        .nav-icon { margin-right: 12px; font-size: 1.2rem; }
        .active-btn { background-color: #0E3B6C !important; color: #FFFFFF !important; border: 2px solid #0E3B6C !important; }
        
        # --- ESTILO PARA CARDS DE IMÓVEIS ---
        .property-card { border: 1px solid #E0E0E0; padding: 20px; border-radius: 12px; margin-bottom: 25px; background-color: #FFFFFF; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .stButton>button { border-radius: 8px !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. BARRA LATERAL COM LOGO E NAVEGAÇÃO ---
with st.sidebar:
    # --- LOGOMARCA MLC NO TOPO (CONFORME image_0.png) ---
    st.markdown(f"""
        <div style="text-align: center; padding: 10px 0;">
            <div style="display: inline-block; width: 60px; height: 60px; background-color: #0E3B6C; border-radius: 50%; border: 3px solid #FFD700; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px;">
                <h1 style="color: #FFD700; margin: 0; font-size: 1.5rem;">MLC</h1>
            </div>
            <h4 style="color: #333333; margin:0;">Mateus Lima Cerqueira</h4>
            <p style="color: #0E3B6C; margin:0; font-size: 0.9rem;">CRECI {CRECI_NUM}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # --- SIMULANDO NAVEGAÇÃO MOBILE NO PC ---
    st.markdown("### Navegação")
    
    # Criando botões modernos na lateral
    btn_radar = st.button("🛰️ Radar", key="nav_radar", type="primary" if "radar" in st.session_state and st.session_state.radar else "secondary")
    btn_modelos = st.button("📂 Modelos", key="nav_modelos", type="primary" if "modelos" in st.session_state and st.session_state.modelos else "secondary")
    btn_financeiro = st.button("💰 Financeiro", key="nav_financeiro", type="primary" if "financeiro" in st.session_state and st.session_state.financeiro else "secondary")
    btn_alertas = st.button("🔔 Alertas", key="nav_alertas", type="primary" if "alertas" in st.session_state and st.session_state.alertas else "secondary")

    # Lógica de seleção
    if btn_radar: st.session_state.modulo = "🛰️ Radar"
    elif btn_modelos: st.session_state.modulo = "📂 Modelos"
    elif btn_financeiro: st.session_state.modulo = "💰 Financeiro"
    elif btn_alertas: st.session_state.modulo = "🔔 Alertas"
    
    # Define o módulo inicial se não houver seleção
    if "modulo" not in st.session_state:
        st.session_state.modulo = "🛰️ Radar"

modulo = st.session_state.modulo

# --- 4. LÓGICA DO CONTEÚDO (RADAR NO PC) ---
if modulo == "🛰️ Radar":
    st.title("🛰️ Radar de Oportunidades - PC")
    
    # Exemplo de Card de Imóvel (CONFORME image_0.png)
    st.markdown('<div class="property-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=400")
    with col2:
        st.warning("**LEILÃO CAIXA - APARTAMENTO 3Q**")
        st.write("📍 **Local:** Vilas do Atlântico, Lauro de Freitas/BA")
        st.write("💰 **Lance Inicial:** R$ 330.000,00 (40% OFF)")
        st.link_button("🌐 Ver Detalhes no Portal Oficial", "https://venda-imoveis.caixa.gov.br/")
    st.markdown('</div>', unsafe_allow_html=True)

    # Exemplo de Card de Imóvel 2
    st.markdown('<div class="property-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=400")
    with col2:
        st.warning("**LEILOEIRO OFICIAL - LOTE RESIDENCIAL**")
        st.write("📍 **Local:** Praia do Forte, Mata de São João/BA")
        st.write("📈 **Potencial:** Alta valorização")
        st.link_button("🌐 Ver Edital e Matrícula", "https://www.rjleiloes.com.br/")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. OUTROS MÓDULOS (MODELOS, FINANCEIRO) ---
elif modulo == "📂 Modelos":
    st.title("📂 Fábrica de Documentos")
    st.write("Selecione o modelo abaixo:")
    # (Lógica de documentos...)

elif modulo == "💰 Financeiro":
    st.title("💰 Controle Financeiro")
    st.write("Gestão de comissões.")