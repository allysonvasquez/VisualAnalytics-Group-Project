from gettext import npgettext
from turtle import color
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from datetime import date

#PREVIOUS SUBMISSIONS FOR REF
#ref: https://webpages.charlotte.edu/eketeni/ITCS4122Final/website/index.html
#ref: https://gdp-indicators-app.herokuapp.com/
#ref: https://itcs-4122-5122-prj-team-3.github.io/demo/vis/comparison

# ---- TODO ----
# ALLYSON
#- Create section for radio buttons that will go to our visualizations
#- Create visualization displaying dataframe
#https://www.kaggle.com/code/anastasiyabirina/full-eda-and-visualization
#    - ref

# VENA
#    - Create a home page that introduces our group & topic/data (can pull info from our proposal assignment)
#https://www.kaggle.com/code/ajaysuram/hotel-booking-prediction
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
    df = pd.read_csv('hotel.csv', index_col='idx')
    return df

st.title('TITLE?')

# load the data
df = load_data()

viz = st.sidebar.radio("Select a Visualization Below to View", ('Statistical Overview', 'viz2','viz3','blah','test')) #rename as needed

# show the data in a table
if viz == 'Show DataFrame':
    st.write(df)

if viz == 'viz2':
    #your viz here
    st.write('hi')