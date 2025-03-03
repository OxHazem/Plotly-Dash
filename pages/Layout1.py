from dash import html
from dash import dcc ,Input,Output,callback
from visualizationAndData import basic_visualization

layout1 = html.Div(id='layout1', children=[
    html.Link(rel='stylesheet',href='D:\DownLoad\projects\plotly-dash-visualization\\assets\styles.css'),
    html.Div( id='header' , children=[
    html.H1("Welcome to Car Pricing Dashboard",id="main_header"),
    html.H2("Overview of the data",id="overview_header"),
    html.P("This analysis demonstrates the principal determinant of pricing differentials.",id='overview_paragraph')
    ]),
    html.Div( id='charts' , children=[dcc.Graph(figure=basic_visualization()[0],id='chart1'),dcc.Graph(figure=basic_visualization()[1],id='chart2'),dcc.Graph(figure=basic_visualization()[2],id='chart3' ) 
    ],),html.Footer(id="footer",children=[html.Button("Next Page",id='submit',n_clicks=0)]),
    
    
    ])
layout2=html.Div(id='layout2' , children=[html.H1("Welcome to Car Pricing Dashboard",id="main_header"),html.H2("Overview of the data",id="overview_header"),html.P("This analysis demonstrates the principal determinant of pricing differentials.",id='overview_paragraph')])

@callback(
    Output('layout1', 'children'),
    Input('submit', 'n_clicks')
)
def update(n_clicks):
    if n_clicks ==0:
        return layout1
    else:
        return layout2 




