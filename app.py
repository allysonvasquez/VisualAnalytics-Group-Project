import matplotlib.pyplot as plt
import seaborn as sns
from turtle import color
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

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

# load the data
df = load_data()
page = st.sidebar.radio("Select a Visualization Below to View", ('About the Data','Statistical Overview', 'Comparing Cost','Correlations','Bookings Analytics')) #rename as needed

#vena----
if page == 'About the Data':
    st.header('About the Data')
    st.write('ITCS 4122/5122 - Visual Analytics, Spring 2022')
    st.write('Project Team 6: Allyson Vasquez, Alex Miller, Vena Khamvanthong, Mandev Doshi')

    st.subheader('Project Overview')
    st.write(
        "For our visualization project, we chose to use the Kaggle dataset, [Hotel Booking](https://www.kaggle.com/datasets/mojtaba142/hotel-booking). " +
        "This dataset contains over 110,000 entries representing hotel bookings made between July 1, 2015 and August 31, 2017. " + 
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

#allyson-------
if page == 'Statistical Overview':
    st.header('Analysis & Statistical Overview')
    st.subheader('The Dataset:')
    st.dataframe(df)
    df_total_days_stayed = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]

    feature_list=['is_canceled', 'arrival_date_year','adults', 'children', 'babies', 'is_repeated_guest', 'previous_cancellations','adr','total_of_special_requests', 'total_days_stayed']
    feature = st.selectbox('Select to view statistics on the following numeric features in the dataset:', (feature_list))
    if feature:
        if feature == 'total_days_stayed':
            desc = df_total_days_stayed.describe()
            st.table(desc)
        else:
            desc = df[feature].describe()
            st.table(desc)

#allyson-------
if page == 'Comparing Cost':
    option = st.selectbox('View the Average Cost of a Hotel Stay By...', ('Hotel Type', 'Country', 'Month', 'Year'))

    st.subheader('Average Cost of Hotel Stay by ' + option)
    if option == 'Hotel Type':
        st.write(alt.Chart(df).mark_bar(color='purple').encode(x=alt.X('hotel:O', axis=alt.Axis(title='Hotel Type')), y=alt.Y('mean(adr)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=700,height=400))
    elif option == 'Country':
        st.write(alt.Chart(df).mark_bar(color='orange').encode(x=alt.X('country', axis=alt.Axis(title='Country (Abbreviated)')), y=alt.Y('mean(adr)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=2000,height=800))
    elif option == 'Month':
        st.write(alt.Chart(df).mark_bar(color='blue').encode(x=alt.X('arrival_date_month:O', axis=alt.Axis(title='Month')), y=alt.Y('mean(adr)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=800,height=600))
    elif option == 'Year':
        st.write(alt.Chart(df).mark_bar(color='green').encode(x=alt.X('arrival_date_year:O', axis=alt.Axis(title='Year')), y=alt.Y('mean(adr)', axis=alt.Axis(title='Average Hotel Cost (USD)'))).properties(width=600,height=300))

#alex-----
if page == "Correlations":
    st.header('Viewing correlations between 2 statistics')
    options_list = ('Number of nights stayed', 'Average Daily Rate', 'Lead Time', 'Booking Changes', 'Total Special Requests')
    option1 = st.selectbox('X - axis', options_list)
    option2 = st.selectbox('Y - axis', options_list, index=1)

    df_total_days_stayed = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]

    data_map = {
        'Number of nights stayed':df_total_days_stayed,
        'Average Daily Rate':df['adr'],
        'Lead Time':df['lead_time'],
        'Booking Changes':df['booking_changes'],
        'Total Special Requests':df['total_of_special_requests']
    }


    chart_data = pd.DataFrame({
       option1: data_map.get(option1),
       option2: data_map.get(option2)
    })

    chart = alt.Chart(chart_data).mark_line().encode(
    x=option1,
    y=option2,
    ).properties(
    width=700,
    height=500
    )

    st.altair_chart(chart)


#mandev----
if page == 'Bookings Analytics':
    st.header('Percentage of bookings per year. ')

    fig = plt.figure ( figsize = (10,5))
    ax1 = fig.add_axes ([0,0,1,1])
    ax2 = fig.add_axes ([0.75,0,1,1])
    sns.countplot(data=df, x='arrival_date_day_of_month', ax=ax1, 
              hue='arrival_date_year', order=df['arrival_date_day_of_month'].value_counts().index, palette="Set1")

    years = dict(df['arrival_date_year'].value_counts())
    ax2.pie(x=list(years.values()), labels=list(years.keys()), explode=[0.03]*3, autopct='%1.1f', shadow=True)
    st.pyplot(fig)

    st.header('Percentage of bookings in different countries. ')

    fig1 = plt.figure(figsize=(13, 8))

    sns.countplot(data=df, x='country', order=df['country'].value_counts().keys(), palette="Set2").set_xlim(0, 9)
    st.pyplot(fig1)

    st.header('Percentage of bookings based on market segment. ')

    fig2 = plt.figure(figsize=(13, 8))
    sns.countplot(data=df, x='market_segment', order=df['market_segment'].value_counts().keys(),  palette="Set1").set_xlim(0, 9)
    st.pyplot(fig2)
    
