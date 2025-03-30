from dash import html, dcc, Input, Output, callback
from visualizationAndData import basic_visualization


# this will help me change between these two 
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
layout2=html.Div(id='layout2' , children=[html.Link(rel='stylesheet',href="D:\DownLoad\projects\plotly-dash-visualization\\assets\style2.css"),html.Button("Previous Page",id='submit2',n_clicks=0),html.H1("This is the second page")])

main_layout=html.Div([
    dcc.Store(id='page_tracker',data=1),
    html.Div(id="page_content",children=layout1)
])

# the next function is part will be the call backs and the function that will change between the layouts 
@callback(
  Output('page_content','children'), # wee need to locate where the change will happen
  Input('submit', 'n_clicks')  
) # to solve this we will create a new layout (main_layout)






    



