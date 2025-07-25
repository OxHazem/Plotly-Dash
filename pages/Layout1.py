from dash import html, dcc, Input, Output, callback
from visualizationAndData import basic_visualization ,Graph_one,Graph_two,Graph_three,Graph_four,unique_brands


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

layout2=html.Div(id='layout2' , children=[html.Link(rel='stylesheet',href="D:\DownLoad\projects\plotly-dash-visualization\\assets\style2.css"),
                                          html.Button("Previous Page",id='submit',n_clicks=0),
                                          dcc.Dropdown(unique_brands()[0],"Kia",id="dropdown_for_layout2"),
                                          html.Div(id="charts",children=[
                                              dcc.Graph(id="chart1"),
                                              dcc.Graph(id="chart2"),
                                              dcc.Graph(id="chart3")
                                          ]),
                                          dcc.Dropdown(id="dropdown_for_section2" , placeholder="choose a model"),
                                          html.Div(id="charts2",children=[
                                              dcc.Graph(id="chart12")
                                          ])
                                          ])

main_layout=html.Div([
    dcc.Store(id='page_tracker',data=1),
    html.Div(id="page_content",children=layout1)
])

# the next function is part will be the call backs and the function that will change between the layouts 
@callback(
  Output('page_content','children'),
  Output('page_tracker','data'),# wee need to locate where the change will happen
  Input('submit', 'n_clicks'), 
  Input ('page_tracker','data')
) # to solve this we will create a new layout (main_layout)
def changing_layout(n_clicks,data):
    if(data==1) :
        if(n_clicks !=0) : 
            return layout2 ,2
    elif (data==2):
        if(n_clicks!=0) : 
            return layout1,1
# we need to create another callback for the charts for layout 2 
@callback(
    Output("chart1", "figure"),
    Output("chart2","figure"),
    Output("chart3","figure"),
    Input("dropdown_for_layout2","value")
)
def changing_charts(value):
    return Graph_four(value),Graph_two(value),Graph_three(value)

@callback(
        Output("dropdown_for_section2","options"),
        Input("dropdown_for_layout2","value")
)
def changing_dictionary_values(value):
    for brand,model in unique_brands()[1].items() :
        if(brand==value) : 
            return model 







@callback(
    Output("chart12","figure"),
    Input("dropdown_for_layout2","value"), #Brand
    Input("dropdown_for_section2","value")#Model
)
def changing_chart_section2(Brand_value,Model_value):
    return Graph_one(Brand_value,Model_value)





    



