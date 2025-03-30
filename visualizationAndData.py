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
#to make visualiztion first wee need to imagine the basic KPI we want to implement 
def Graph_one(Brand_name): # the visualization of the price distrbution of specific brand 
    data=pd.read_csv("D:\DownLoad\projects\plotly-dash-visualization\data\car_price_dataset.csv") # read csv
    df=pd.DataFrame(data)
    brand_df=df[df['Brand']==Brand_name]
    fig=px.histogram(brand_df,x='Price',nbins=10,title=f"the price distribution of {Brand_name}")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    fig.show()
def Graph_two(Brand_name): # how many people own a specific brand
    data=pd.read_csv("D:\DownLoad\projects\plotly-dash-visualization\data\car_price_dataset.csv")
    df=pd.DataFrame(data)
    brand_df=df[df['Brand']==Brand_name]
    Y=brand_df.groupby("Model")['Owner_Count'].sum().reset_index()
    fig=px.bar(Y,x="Model",y="Owner_Count",title=f"the Owner count of {Brand_name}")
    fig.show()

def Graph_three(Brand_name): # how many people own a specifc Brand type of Transmission
    data=pd.read_csv("D:\DownLoad\projects\plotly-dash-visualization\data\car_price_dataset.csv")
    df=pd.DataFrame(data)
    Brand_df=df[df['Brand']==Brand_name]
    Transmission_count=Brand_df.groupby("Transmission")['Owner_Count'].sum().reset_index()
    fig=px.bar(Transmission_count,x="Transmission",y="Owner_Count",title=f"the owner count in of each Transmission in {Brand_name}")
    fig.show()







#testing area 
#Graph_one("Kia")
#Graph_two("Kia")
#Graph_three("Kia")




        

 

        



