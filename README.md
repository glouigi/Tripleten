# APLICACION WEB PARA VISUALIZACION DE DATA DE VEHICULOS DE U.S.

## VISTA GENERAL DEL PROYECTO

Este proyecto se basa en crear y gestionar entornos virtuales de Python, desarrollar una aplicación web y desplegarla en un servicio en la nube de acceso público RENDER.

El proyecto utilizó un conjunto de datos de anuncios de venta de coches "vehicles_us.csv" aunque no se centró principalmente en el conjunto de datos o en el análisis del mismo.


## PASOS:

### PASO 1: REQUISITOS DEL PROYECTO

- Crea una cuenta en GitHub e inicié un nuevo repositorio con los archivos README.md y .gitignore.
- Instala los paquetes necesarios, incluyendo pandas, streamlit, y plotly-express.
- Crea una cuenta en Render.com y la vinculelo con el repositorio del proyecto en GitHub.
- Instalale y configure VS Code, estableciendo el intérprete de Python para que coincida con el entorno virtual.

### PASO 2: ADQUISICION DE DATOS

- Descarga la base de datos "vehicles_us.csv" y ubique en el directorio de su proyecto.

### PASO 3: ANALISIS Y VISUALIZACION DE LA DATA

- Crea un libro en Jupyter Noteboo llamado EDA.ipynb y realice una observacion de la data
- Crea histogramas y diagramas de dispercion usando plotly-express library.
- Los diagramas realizados en Jupyter fueron el primer prototipo del proyecto web.

### PASO 4: DESARROLLO DE LA APLICACION WEB

- Crear el archivo python app.py en el directorio del proyecto.
- Importa las librerias necesarias streamlit, pandas, y plotly_express.
- Carga la data de l archivo "vehicles_us.csv" usando Pandas y crea la DataFrame "car_data".
- Incorpora elementos de Streamlit en la app como Titulo, botones, histogramas, diagramas de dispersion y mensajes.
- Actualiza el archivo README con la descripcion del proyecto, instrucciones y cada cambio que se realice.

### PASO 5: DESPLIEGUE EN RENDER

- Añade el archivo de configuración de streamlit al repositorio de GitHub llamado "config.toml"
- Crea un servicio web vinculado al repositorio GitHub en Render.
- Configura el servicio web Render para instalar los paquetes necesarios usando el archivo "requirements.txt" y ejecuta el archivo app.py, todo esto con el comando: 
    - BULILD COMMAND: pip install --upgrade pip && pip install -r requirements.txt
    - START COMMAND: streamlit run app.py
- Despliega la versión final de la aplicación en Render.
- Verificada la accesibilidad de la aplicación en el link: https://tripleten-project-spring-6.onrender.com/

## CONCLUCION

Esta aplicación Streamlit proporciona una visualización interactiva del conjunto de datos "vehicle_us.csv". La aplicación se desarrolló como parte de la práctica de tareas de Ciencia de Datos, a saber, la creación de entornos virtuales Python, el desarrollo de una aplicación web y su despliegue en un servicio en la nube. La aplicación está activa y se puede acceder a ella. https://tripleten-project-spring-6.onrender.com/

PROYECTO DE: GIORGIO RAMIREZ