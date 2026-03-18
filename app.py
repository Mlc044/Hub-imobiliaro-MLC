# --- MÓDULO: RADAR COM LINKS EXTERNOS ---
if modulo == "🛰️ Radar de Oportunidades":
    st.header("🛰️ Radar de Oportunidades (Salvador & RMS)")
    st.caption(f"Monitoramento Profissional | Mateus Lima - CRECI {CRECI_NUM}")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        btn_imoveis = st.button("🏠 Buscar Leilões da Caixa (Lauro/SSA)")
    with col_btn2:
        btn_mei = st.button("📜 Buscar Licitações MEI (Bahia)")

    st.divider()

    # RESULTADOS DE IMÓVEIS (LEILÕES)
    if btn_imoveis:
        st.subheader("📍 Oportunidades em Destaque")
        
        # Exemplo 1: Imóvel em Lauro de Freitas
        with st.container(border=True):
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=300")
            with c2:
                st.warning("**LEILÃO CAIXA:** Apartamento 3Q - Vilas do Atlântico")
                st.write("📍 **Local:** Lauro de Freitas/BA")
                st.write("💰 **Lance Inicial:** R$ 330.000,00")
                
                # LINK PARA O SITE DA CAIXA
                url_caixa = "https://venda-imoveis.caixa.gov.br/sistema/busca-imovel.asp?sBtn=S&sEstado=BA&sCidade=4557"
                st.link_button("🌐 Ver Detalhes no Site da Caixa", url_caixa)

    # RESULTADOS DE LICITAÇÕES (MEI)
    if btn_mei:
        st.subheader("🏢 Editais para o seu MEI")
        
        # Exemplo 2: Licitação em Salvador
        with st.container(border=True):
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image("https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=300")
            with c2:
                st.info("**PREFEITURA SSA:** Manutenção de Hardware")
                st.write("📍 **Órgão:** Prefeitura de Salvador")
                
                # LINK PARA O PORTAL DE COMPRAS
                url_licitacao = "https://www.compras.salvador.ba.gov.br/"
                st.link_button("🌐 Ver Edital no Portal de Compras", url_licitacao)