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

# load the data
df = load_data()

st.title('Hotel Booking Insights')
with st.sidebar:
    viz = st.radio("Select a Visualization Below to View", ('Home','Statistical Overview', 'viz2','viz3','blah','test'), 0) #rename as needed

#vena-------
if viz == 'Home':
    st.write('ITCS 4122/5122 - Visual Analytics, Spring 2022')
    st.write('Project Team 6: Allyson Vasquez, Alex Miller, Vena Khamvanthong, Mandev Doshi')

    st.subheader('Project Overview')
    st.write(
        "For our visualization project, we chose to use the Kaggle dataset,[Hotel Booking](https://www.kaggle.com/datasets/mojtaba142/hotel-booking). "+
        "This dataset contains over 110,000 entries representing hotel bookings made between July 1, 2015 and August 31, 2017. "+ 
        "Our goals for this visualization are to determine that factors that influence booking cancellations and to find relationships between booking details, average daily rates, and final reservation status"
    )

    with st.expander("Dataset Attributes"):
        st.write(
            'The hotel booking dataset consisted of 36 attributes and 119,390 rows. For this project, we chose to focus on the ' +
            'following key attributes:'
        )
        data_col1, data_col2, data_col3 = st.columns(3)
        with data_col1:
            """
                Key Categorical Attributes
                * adr (average daily rate)
                * is_canceled
                * is_repeated_guest
                * customer_type
                * distribution_channel
            """

        with data_col2:
            """
                Key Quanitative Attributes
                * lead_time
                * arrival_date
                * previous_cancellations
                * previous_bookings_not_canceled
                * booking_changes
                * total_special_requests
                * reservation_status_date
            """
    with st.expander("Data Cleaning"):
        st.write('The hotel booking dataset contained columns that were either artificially generated or not necessary for our ' + 
                    'final visualizations and were dropped from the final dataframe. These columns include:')
        """
            * agent
            * company
            * name
            * email
            * phone-number
            * credit_card
            * arrival_date_month
            * reservation_status_date
            * reservation_status
        """
        st.write('In addition, there were a few instances of columns that have "na" or "Nan" values. These were the "children" and "country" columns.' +
                    ' In the case of the children" column, since only four entries are affected, we dropped these entries altogether. The "country" column on the other hand had a significant number of affected entries. In this case, we changed all "na" values to "Unknown."'
        )

    with st.expander("Target Demographic"):
        st.write('We designed our visualization to provide useful data concerning the trends that hotel bookings follow. The information would be most useful for indivduals in the hotel industry that would like to maximize profits '
        )
    with st.expander("Application Implementation"):
        st.write('The web framework we used for our project was Streamlit, which allowed us the ease of creating a web ' +
                    'without having to use HTML or CSS. For our visualizations, we created charts and graphs in Altair to ' +
                    'allow for interactivity with the dataset. We also utilized the Pandas and Numpy in Python in order to '+
                    'explore and clean the dataset.'
        )
#-------

#allyson-------
if viz == 'Statistical Overview':
    st.header('Analysis & Statistical Overview')
    st.subheader('The Dataset:')
    st.write(df)

    option = st.selectbox('Select Your Hotel Type to Look at stats:', ('Resort Hotel', 'City Hotel'))
    st.write('You selected:', option)
#-------



if viz == 'viz2':
    #your viz here
    st.write('hi')