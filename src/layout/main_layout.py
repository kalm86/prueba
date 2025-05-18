from dash import html, dcc

layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Captura URL
    # Navbar
    html.Nav([
        html.Div([
            html.A("Mortalidad CO", className="navbar-brand", href="#"),
            html.Button([
                html.Span(className="navbar-toggler-icon")
            ],
                className="navbar-toggler",
                **{
                    "type": "button",
                    "data-bs-toggle": "collapse",
                    "data-bs-target": "#navbarNav",
                    "aria-controls": "navbarNav",
                    "aria-expanded": "false",
                    "aria-label": "Toggle navigation"
                }
            ),
            html.Div([
                html.Ul([
                    html.Li(html.A("Mapa", href="/map", className="nav-link"), className="nav-item"),
                    html.Li(html.A("Líneas", href="/line", className="nav-link"), className="nav-item"),
                    html.Li(html.A("Barras", href="/bar", className="nav-link"), className="nav-item"),
                    html.Li(html.A("Circular", href="/pie", className="nav-link"), className="nav-item"),
                    html.Li(html.A("Tabla", href="/tabla", className="nav-link"), className="nav-item"),
                    html.Li(html.A("Histograma", href="/hist", className="nav-link"), className="nav-item"),
                    html.Li(html.A("Barras Apiladas", href="/bar_api", className="nav-link"), className="nav-item"),
                ], className="navbar-nav ms-auto")
            ], className="collapse navbar-collapse", id="navbarNav")
        ], className="container-fluid")
    ], className="navbar navbar-expand-lg navbar-dark navbar-custom"),

    # Contenido principal
    html.Main([
        html.Div([
            html.H1("Indicadores de Mortalidad en Colombia", className="display-5"),
            html.P("Año 2019", className="text-muted")
        ], className="text-center mb-4"),

        html.Div(id="plot-container") #, className="chart-container")  # aquí se cargará el gráfico
    ], className="container my-5"),

    # Footer
    html.Footer([
        html.Small("© 2025 Universidad de La Salle - Dashboard de Mortalidad")
    ], className="bg-white text-center py-3 border-top")
])