#making a data profiling to understand the data 
from ydata_profiling import ProfileReport
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def data_profiling():
    data = pd.read_csv('D:\DownLoad\projects\plotly-dash-visualization\data\car_price_dataset.csv')#copy the path of the csv file in the data folder 
    profile = ProfileReport(data, title="Pandas Profiling Report")
    profile.to_file("D:\DownLoad\projects\plotly-dash-visualization\data\car_price_dataset_profiling.html")#copy the path of the html file in the data folder
    return profile

def basic_visualization(): # After we made the layout of charts of the layout 1 we will start the visualization part
    data = pd.read_csv('D:\DownLoad\projects\plotly-dash-visualization\data\car_price_dataset.csv') #copy the path of the csv file in the data folder
    fig=px.scatter(data,x='Year',y='Price',title='Price vs Year')
    fig2=px.scatter(data,x='Mileage',y='Price',title='Price vs Mileage')
    fig3=px.scatter(data,x='Engine_Size',y='Price',title='Price vs Engine_Size')
    return fig , fig2 , fig3



        

 

        



