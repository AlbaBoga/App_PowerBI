import streamlit as st

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
# Tenemos dos opciones de layout, wide or center. Wide te lo adapta a la ventana
# mientras que center, lo centra.
st.set_page_config(page_title='Dashboard', page_icon='🧮', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

st.title('Manufacturer Analysis')

link = '<iframe title="Report Section" width="1024" height="1060" src="https://app.powerbi.com/view?r=eyJrIjoiNTMzM2Q3ODItMTlhNy00ZGQ4LThkNGUtMjYxZWIyNDMwYjc2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>'

st.markdown(link, unsafe_allow_html=True)