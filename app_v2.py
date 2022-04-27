from gettext import npgettext
from turtle import color
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from datetime import date
import time

#PREVIOUS SUBMISSIONS FOR REF
#ref: https://webpages.charlotte.edu/eketeni/ITCS4122Final/website/index.html
#ref: https://gdp-indicators-app.herokuapp.com/
#ref: https://itcs-4122-5122-prj-team-3.github.io/demo/vis/comparison

# ---- TODO ----
# ALLYSON
#- Create section for radio buttons that will go to our visualizations
#- Create visualization displaying dataframe & other exploratyory analysis
#https://www.kaggle.com/code/anastasiyabirina/full-eda-and-visualization
#https://www.kaggle.com/code/ajaysuram/hotel-booking-prediction
#    - ref

# VENA
#    - Create a home page that introduces our group & topic/data (can pull info from our proposal assignment)
#    - explain what all the columns mean
#    - convert some charts from here

# ALEX
#https://www.kaggle.com/code/mortrest/hotel-booking-dataset-2-4
#    - Bar chart of hotel types
#    - Pie chart showing arrival_date_year (what year was most popular to get booked)
#    - Any feature on the x-axis. Y-axis = adr 
#        (adr = avg. daily rate. It is how much $ a customer paid for their hotel stay)

# MANDEV
#https://www.kaggle.com/code/dangquangvu/hotel-booking-cleaning-data-bar-charts
#    - create visualization showing percentage of bookings per year (can use above links as reference)
#    - Convert final product into Heroku or github.io

@st.cache
def load_data(): #Function that loads s ome data, puts it in a dataframe, and converts the date 
    df = pd.read_csv('hotel.csv', index_col='index')
    return df

st.title('Hotel Booking Insights')

# load the data
df = load_data()

page = st.sidebar.radio("Select a Visualization Below to View", ('About the Data (Vena)','Statistical Overview', 'Comparing Cost','ALEX','MANDEV')) #rename as needed

#vena----
if page == 'About the Data (Vena)':
    st.header('blah')
    st.write('info')

    st.header('explain the columns')
    #note from allyson: I renamed adr column to 'total_cost'
    st.write('blah')

#allyson-------
if page == 'Statistical Overview':
    st.header('Analysis & Statistical Overview')
    st.subheader('The Dataset:')
    st.write(df)
    #TODO: show mean, std, etc.

#allyson-------
if page == 'Comparing Cost':

    option = st.selectbox('View the Average Cost of a Hotel Stay By...', ('Hotel Type', 'Country', 'Month', 'Year'))

    st.subheader('Average Cost of Hotel Stay by ' + option)
    if option == 'Hotel Type':
        st.write(alt.Chart(df).mark_bar(color='purple').encode(x=alt.X('hotel:O', axis=alt.Axis(title='Hotel Type')), y=alt.Y('mean(total_cost)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=700,height=400))
    elif option == 'Country':
        st.write(alt.Chart(df).mark_bar(color='orange').encode(x=alt.X('country', axis=alt.Axis(title='Country (Abbreviated)')), y=alt.Y('mean(total_cost)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=2000,height=800))
    elif option == 'Month':
        st.write(alt.Chart(df).mark_bar(color='blue').encode(x=alt.X('arrival_date_month:O', axis=alt.Axis(title='Month')), y=alt.Y('mean(total_cost)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=800,height=600))
    elif option == 'Year':
        st.write(alt.Chart(df).mark_bar(color='green').encode(x=alt.X('arrival_date_year:O', axis=alt.Axis(title='Year')), y=alt.Y('mean(total_cost)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=600,height=300))

if page == "ALEX":
    st.write('placeholder')

if page == "MANDEV":
    st.write('placeholder')