import streamlit as st

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Dashboard', page_icon='🧮', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

st.title('Manufacturer Analysis')

link = '<iframe title="ManufacturerAnalysis" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=83e4c3db-d0e0-4485-9aaf-898a1921293a&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64" frameborder="0" allowFullScreen="true"></iframe>'

st.markdown(link, unsafe_allow_html=True)