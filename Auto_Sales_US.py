import pandas as pd
import plotly.graph_objs as go
import streamlit as st

st.header('Analysis of Auto Sales in the U.S.')
st.subheader("Q. When did America's love affair with SUVs and Pick-up Trucks take off?")

#Load data
data = pd.read_csv('https://github.com/mike-ua/Streamlit-Data/blob/3ecf48e67e9a15e5fa57e8a11a734426c3aa10de/LightTruck_Auto_Sales.csv?raw=true')

st.text("Light Trucks = Pickup trucks, SUVs, minivans, vans, crossovers")
st.text("Passenger Cars = sedans, coupes, convertibles, hatchbacks, station wagons")


#Create traces for the SAAR of each category
trace1 = go.Scatter(x=data['Date'], y=data['Light_Truck'], 
                    fill='tozeroy', name='Light Trucks', 
                    yaxis='y1', line=dict(color='blue'))

trace2 = go.Scatter(x=data['Date'], y=data['Passenger_Cars'], 
                    fill='tozeroy', name='Passenger Cars', 
                    yaxis='y1', line=dict(color='lightblue'))

#Create the layout with DUAL y-axes
layout = go.Layout(
    title='U.S. Vehicle Sales - SAAR',
    xaxis=dict(title='Quarter'),
    yaxis=dict(title='SAAR (Millions)', side='left'),
    yaxis2=dict(title='Vehicle Count', side='right', overlaying='y'),
    legend=dict(x=0.1, y=1.1, orientation='h'),
)

#Combine the traces into a figure
fig = go.Figure(data=[trace1, trace2], layout=layout)



# Display the chart in Streamlit
st.plotly_chart(fig)
st.markdown("source: https://data.bts.gov/Research-and-Statistics/Monthly-Transportation-Statistics/crem-w557/about_data")

st.markdown("**Note 1:** Statistics based on 'Sales Seasonally Adjusted Annual Rate', or SAAR")
st.markdown("**Note 2:** Although this dataset does not break down the 'Light Truck' category into it's components (Pick-up truck, SUV, Van, etc.) the assumption is that most of the gains are in SUV's and Pick-up trucks based on widely accepted popularity and trends")


st.divider()

st.subheader('Data Analysis Tools Used')
st.markdown('**Dataset:** .csv file')
st.markdown('**Python:** create the basic script')
st.markdown('**Pandas:** data manipulation')
st.markdown('**Plotly:** create the main visualization')
st.markdown('**Streamlit:** Python framework to share the script, e.g. web app')
st.markdown('**Github:** developer platform for hosting the script and data file')
