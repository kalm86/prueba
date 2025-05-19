## Dashboard de Mortalidad en Colombia – Año 2019
Este proyecto presenta un análisis visual e interactivo de las **estadísticas de mortalidad en Colombia durante el año 2019**, a partir de datos oficiales y categorizados por causa de muerte, región, sexo y grupo etnico.

La aplicación fue desarrollada con **Python, Dash, Pandas y Plotly**, permitiendo la exploración intuitiva de la información a través de **gráficas dinámicas** (líneas, barras, histogramas, tortas, mapas) y una **tabla de datos**.

## Tabla de Contenido

- [Objetivo del Proyecto](#objetivo-del-proyecto)
- [Características principales](#características-principales)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instrucciones de instalación](#instrucciones-de-instalación)
- [Enlace de aplicación](#enlace-de-aplicación)
- [Fuente de datos](#fuente-de-datos)
- [Autores](#autores)

## Objetivo del Proyecto
El objetivo de este proyecto es desarrollar un dashboard interactivo que permita visualizar, analizar y comprender las estadísticas de mortalidad en Colombia durante el año 2019. A través de gráficos dinámicos y una interfaz accesible, se busca facilitar la interpretación de los datos por parte de investigadores, profesionales de la salud, estudiantes y ciudadanos interesados, promoviendo la toma de decisiones informadas y la conciencia social sobre las principales causas de muerte en el país.

## Características principales

- ✅ Visualización de causas de muerte por género, edad y departamento.
- ✅ Gráficas interactivas tipo líneas, barras, tortas, histogramas y mapas.
- ✅ Tabla de datos con formato Bootstrap.
- ✅ Navegación tipo SPA con menú superior.
- ✅ Datos procesados desde archivo Excel.

## Tecnologías utilizadas

- [Python 3.8+](https://www.python.org/)
- [Dash (Plotly)](https://dash.plotly.com/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Bootstrap 5](https://getbootstrap.com/)
- [openpyxl](https://openpyxl.readthedocs.io/)

## Estructura del Proyecto
```bash
project-root/
├── src/                            # Carpeta que contiene el código fuente
    └── assets                      # Carpeta para Hojas de estilo y codigos en javascript
        └── custom.css              # Hoja de estilo de pagina web
    └── controllers                 # Carpeta para controladores
        └── chart_controller.py     # Archivo con logica de graficos
    └── data                        # Carpeta con archivos de datos
        └── CodigosMuerte.xlsx      # Listado de codigos de muerte
        └── Divipola.xlsx           # Listado de departamentos y municipios
        └── estadisticas_muerte.db  # Datawarehouse consolidador de todos los archivos de Excel
        └── NoFelta.xlsx            # Archivo con estadistica de muertes no fetales
    └── layout                      # Carpeta con layout o estilos de vista
        └── main_layout.py          # Layout principal para mostrar los graficos e información
    └── models                      # Carpeta de modelos
        └── data_model.py           # Archivo con lógica para acceder a los datos
    └── app.py                      # Código principal de la aplicación Dash
        └── server = app.server     # Exposición del servidor Flask utilizado por Dash
├── render.yaml                     # Archivo de configuración de Render
├── requirements.txt                # Dependencias necesarias para la aplicación
└── README.md                       # Documentación del proyecto
```
## Instrucciones de instalación

1. Clona este repositorio:
```bash
git clone https://github.com/kalm86/prueba
cd Mortalidad-CO
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
python app.py
```

4. Abre tu navegador en:
```
http://127.0.0.1:8050/
```

---

## Enlace de aplicación

Si deseas ver la funcinalidad de la aplicación, presiona el siguiente link:

👉 [Ver demo del dashboard](https://prueba-bce6.onrender.com/line)

---

## Fuente de datos

Los datos utilizados en este proyecto fueron obtenidos del **Departamento Administrativo Nacional de Estadística (DANE)**, específicamente del módulo de defunciones vitales correspondiente al año 2019.

---

## Autores

- Wilfer Salgar
- Kelvin Martinez