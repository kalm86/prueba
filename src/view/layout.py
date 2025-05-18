from dash import html, dcc

def get_layout():
    return html.Div([
        html.H1("Estadísticas de Muertes"),
        dcc.Graph(id='grafico'),
        html.Button('Actualizar', id='btn')
    ])