# IMPORTAR LIBRERIAS
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# TITULO DE LA APP
st.title('US Vehicle Advertisement Listings')


# LEER EL ARCHIVO .csv
car_data = pd.read_csv('vehicles_us.csv')

# CREAR UN BOTON
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
