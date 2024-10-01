# PROJECT SPRING 6 - PASO A PASO

## CREACION DE ENTORNO VIRTUAL VSCODE:
- Abrimos la terminal (pestana "view" -> "terminal")
- Nos ubicamos en la carpeta del proyecto con ""cd ruta""
- Ejecutamos ""python -m venv vehicles_env"" (python es el interprete, "vehicles_env" el 
nombre del entorno)
- Activamos el entorno creado "vehicles_env" ejecutando el archivo Activate.ps1 que es parte
del entorno creado, para ello ejecutamos en la terminal "".\vehicles_env\Scripts\activate""
- Veremos en la ruta de la terminal desde VSCode entre '(vehicles_env)' en color verde, 
dando a enternder que el entorno virtual esta activado


## DESACTIVAR ENTORNO VIRTUAL
- Usamos el comando 'deactivate' y se desactivara el entorno virtual previamente activado

## CONOCER QUE LIBRERIAS SE TIENEN INSTALADAS
pip list

    
## INSTALAR LIBRERIAS DENTRO DEL ENTORNO VIRTUAL UNO POR UNO
- Con el entorno virtual activado usamos el comando ""pip instal LIBRERIA""
- Librerias recomendadas para el proyecto: 
    - pip install plotly==5.24.1, https://plotly.com/python/getting-started/
    - pip install pandas,         https://pandas.pydata.org/docs/getting_started/install.html
    - pip install streamlit,      https://streamlit.io/

## CREAR ARCHIVO DE REQUERIMIENTOS DEL PROYECTO
- Este archivo contiene las librerias instaladas en el entorno virtual 
    ""pip freeze > requirements.txt""

## INSTALAR LIBRERIAS DENTRO DEL ENTORNO VIRTUAL DESDE ARCHIVO DE REQUERIMIENTO
- Si el proyecto es compartido y se desea instalar las librerias necesarias para el proyecto, este ya deberia contar con el archivo ""requirements.txt"" el cual es un estandar.
pip install -r ".\requirements.txt"

## DESINSTALAR LIBRERIAS DENTRO DEL ENTORNO VIRTUAL
- Con el entorno virtual activado usamos el comando 
    ""pip uninstall -r requirements.txt -y""