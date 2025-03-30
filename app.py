from visualizationAndData import data_profiling
from dash import Dash
from pages.Layout1 import main_layout
#this will be the main file for the mini project 
#first we need to make ydata profiling to understand the data
#data_profiling()
#then we will start the visualization part
#Due to the data profiling we found out that the data is about cars and their prices and it is cleaned and ready to be visualized

app=Dash(__name__)
app.layout=main_layout
app.run_server(debug=True)
