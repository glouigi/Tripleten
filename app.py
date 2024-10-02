# IMPORTAR LIBRERIAS
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# TITULO DE LA APP
st.title('Vehiculos de EEUU publicitados - By GIO')


# LEER EL ARCHIVO .csv
car_data = pd.read_csv('vehicles_us.csv')

######################################################################################################
# CREAR BOTON HISTOGRAMA - Button1

#Defino el estado del button1 a false (escondido)
if 'button1' not in st.session_state:
   st.session_state.button1 = False
    
def click_button():
    st.session_state.button1 = not st.session_state.button1
    
st.button('Construir histograma', on_click=click_button)

if st.session_state.button1:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

######################################################################################################
# CREAR BOTON DIAGRAMA DISPERSION - Button2

#Defino el estado del button2 a false (escondido)

if 'button2' not in st.session_state:
   st.session_state.button2 = False
    
def click_button():
    st.session_state.button2 = not st.session_state.button2
    
st.button('Construir diagrama dispersion', on_click=click_button) # crear un botón
        
if st.session_state.button2: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
            
    # crear un diagrama de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)