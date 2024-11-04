# Proyecto de Detección de Objetos con OpenCV

Este proyecto captura imágenes desde la cámara durante 10 segundos, tomando una captura por segundo, y organiza estas capturas en carpetas con nombres basados en la fecha y hora de cada ejecución. Además, se guarda la información de cada captura en un archivo JSON.

## Estructura del Proyecto

La estructura de carpetas es la siguiente:

proyecto_deteccion/ │ ├── deteccion.py # Script de Python para capturar y procesar fotos ├── htdocs/ # Carpeta de XAMPP │ ├── index.html # Página principal en HTML │ ├── css/ │ │ └── styles.css # Estilos CSS │ ├── js/ │ │ └── scripts.js # Lógica de JavaScript │ ├── captures/ # Carpeta para almacenar los fotogramas │ └── data.json # Archivo JSON para guardar datos de detección └── .gitignore


## Requisitos

Asegúrate de tener instalado Python 3 y los siguientes paquetes:

## 
pip install opencv-python

Este proyecto está pensado para funcionar con OpenCV y debe tener acceso a una cámara  para capturar imágenes.

Instalación

    Clona este repositorio:

    bash

git clone https://github.com/tu-usuario/proyecto_deteccion.git

Navega hasta el directorio del proyecto:

bash

cd proyecto_deteccion

Instala las dependencias necesarias:

bash

    pip install opencv-python

Uso

    Ejecuta el script deteccion.py para iniciar la captura de imágenes:

    bash

    python deteccion.py

    El script tomará 10 capturas en 10 segundos y las almacenará en una carpeta dentro de htdocs/captures/ con el nombre de la fecha y la hora actual. Además, los datos de cada captura se guardarán en htdocs/data.json.

Funcionalidades

    Captura imágenes de la cámara cada segundo durante 10 segundos.
    Almacena las imágenes en una subcarpeta con un nombre basado en la fecha y la hora de la ejecución.
    Guarda información sobre cada captura en un archivo JSON (data.json), incluyendo la ruta de la imagen y el timestamp.
