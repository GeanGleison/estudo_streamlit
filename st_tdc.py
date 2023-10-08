import streamlit as st
import pandas as pd
import yfinance as yf


# Configurar as dimensões da página
st.set_page_config(
    page_title="Meu App Streamlit",
    page_icon="📊",
    layout="wide",  # Pode ser "wide" ou "centered"
    initial_sidebar_state="expanded",  # Pode ser "auto" ou "expanded" ou "collapsed"
)

#prim_titulo = st.title('Primeiro teste ST_TDC')

# Usar HTML personalizado e CSS para centralizar o título

st.markdown(
    """
    <style>
    .titulo-centralizado {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Exibir o título centralizado
st.markdown("<h1 class='titulo-centralizado'>Primeiro teste ST_TDC</h1>", unsafe_allow_html=True)




st.write ('write')

# Defina as colunas e seus tamanhos
col1, col2 = st.columns([3, 5])

# Insira objetos nas colunas
with col1:
    with st.container():

        video_url = 'https://www.youtube.com/watch?v=Ck8g92smzeQ&t=307s'

        st.video(video_url)

        st.header('Coluna 1')
        st.write('Texto na coluna 1')

with col2: 

    url_imagem = 'https://scontent.fbhz1-1.fna.fbcdn.net/v/t39.30808-6/322732388_902882010869881_8458938620916680870_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=52f669&_nc_eui2=AeEPfsl1xw8SvD2LyPNmte9ivncb8im0e4O-dxvyKbR7gx7vVtAHxGQfEXPK6eMlFEQ&_nc_ohc=mq7LIRZID1AAX9GVCfK&_nc_ht=scontent.fbhz1-1.fna&oh=00_AfCEL30mW8Z22HhslENNuT2Ppy3X_2CpGD7CIKW9MGBslw&oe=6522F72B'

    # Use st.image() com a URL da imagem
    st.image(url_imagem, caption='Imagem da Internet', use_column_width=True)

    st.header('Coluna 2')
    #st.image('https://scontent.fbhz1-1.fna.fbcdn.net/v/t39.30808-6/322732388_902882010869881_8458938620916680870_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=52f669&_nc_eui2=AeEPfsl1xw8SvD2LyPNmte9ivncb8im0e4O-dxvyKbR7gx7vVtAHxGQfEXPK6eMlFEQ&_nc_ohc=mq7LIRZID1AAX9GVCfK&_nc_ht=scontent.fbhz1-1.fna&oh=00_AfCEL30mW8Z22HhslENNuT2Ppy3X_2CpGD7CIKW9MGBslw&oe=6522F72B', width=300)
    st.write('Texto na coluna 2')

st.markdown('**---')

# Você pode continuar adicionando mais colunas e objetos conforme necessário

st.subheader('subheader após criação das colunas sem informar uma coluna')

@st.cache_data
def carregar_dados():
    table = yf.download('BOVA11.SA', period='1y')['Adj Close']
    return table


df = carregar_dados()

col1, col2 = st.columns([3, 12])

# Insira objetos nas colunas
with col1:
    st.dataframe(df)

with col2:
    st.line_chart(df)

