from dash import html
from dash import dcc 
from visualizationAndData import basic_visualization
import dash_bootstrap_components as dbc

layout = html.Div( children=[
    html.Link(rel='stylesheet',href='D:\DownLoad\projects\plotly-dash-visualization\\assets\styles.css'),
    html.Div( id='header' , children=[
    html.H1("Welcome to Car Pricing Dashboard",id="main_header"),
    html.H2("Overview of the data",id="overview_header"),
    html.P("This analysis demonstrates the principal determinant of pricing differentials.",id='overview_paragraph')
    ]),
    html.Div( id='charts' , children=[dcc.Graph(figure=basic_visualization()[0],id='chart1'),dcc.Graph(figure=basic_visualization()[1],id='chart2'),dcc.Graph(figure=basic_visualization()[2],id='chart3' ) 
    ],),
    ]
)