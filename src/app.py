from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
from flask import Flask, render_template
from layout.main_layout import layout
from controllers import chart_controller
from models.data_model import ProcesaDatawarehouse
import pandas as pd

""" Crea datawarehouse """
#ProcesaDatawarehouse()

# Inicializa la aplicación Dash
app = Dash(__name__, 
           external_stylesheets=[
                                    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
                                ])

server = app.server

app.title = "Dashboard de Mortalidad en Colombia"
app.layout = layout

# Registrar los callbacks
chart_controller.realizar_callback(app)

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)


