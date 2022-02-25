from gettext import npgettext
from turtle import color
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from datetime import date

st.markdown("<h1 style='text-align: center; color: black;'>Hotel Booking Database</h1>", unsafe_allow_html=True)

sample_source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52],
    'c': [1,2,3,4,5,6,7,8,9]
})

sample_bar = alt.Chart(sample_source).mark_bar().encode(
    x='a',
    y='b'
)

sample_heatmap = alt.Chart(sample_source).mark_rect().encode(
    x='a',
    y='b',
    color = 'c'
)

sample_line = alt.Chart(sample_source).mark_line().encode(
    x='a',
    y='b'
)

sample_scatter = alt.Chart(sample_source).mark_point().encode(
    x='a',
    y='b',
    color = 'c'
)

sample_stream = alt.Chart(sample_source).mark_area().encode(
    x='a',
    y='b',
    color = 'c'
)

# Collapsable side bar with different view options
with st.sidebar:
    st.title('Customize Dashboard View')
    with st.expander('Charts'):
        chart_type = [st.checkbox('Chart 1'), st.checkbox('Chart 2'), st.checkbox('Chart 3'), st.checkbox('Chart 4'), st.checkbox('Chart 5')]

    with st.expander('Hotel Type'):
        hotel_type = [st.checkbox('City Hotel'), st.checkbox('Resort Hotel')]

    with st.expander('Hotel Location'):
        location = [st.checkbox('PRT'), st.checkbox('GBR'), st.checkbox('Other')]

    with st.expander('Guest Attributes'):
        numAdult = st.slider(
            'Number of Adults',
            min_value=0,
            max_value=10,
            value = 10
        )
        numChild = st.slider(
            'Number of Chidren',
            min_value=0,
            max_value=10,
            value = 10
        )
        numBaby = st.slider(
            'Number of Babies',
            min_value=0,
            max_value=10,
            value = 10
        )
    with st.expander('Reservation Attributes'):
        st.slider(
            'Select Number of Special Requests',
            min_value = date(2015, 1, 1), 
            max_value = date(2017, 12, 31),
            value = (date(2015, 1, 1), date(2017, 12, 31))
        )

        st.slider(
            'Select Booking Date:',
            min_value = date(2015, 1, 1), 
            max_value = date(2017, 12, 31),
            value = (date(2015, 1, 1), date(2017, 12, 31))
        )

        st.slider(
            'Select Arrival Date:',
            min_value = date(2015, 1, 1), 
            max_value = date(2017, 12, 31),
            value = (date(2015, 1, 1), date(2017, 12, 31))
        )

        st.slider(
            'Select Reservation Status Date:',
            min_value = date(2015, 1, 1), 
            max_value = date(2017, 12, 31),
            value = (date(2015, 1, 1), date(2017, 12, 31))
        )

# Dashboard view
if chart_type[0]:
    st.write(sample_bar)
if chart_type[1]:
    st.write(sample_heatmap)
if chart_type[2]:
    st.write(sample_line)
if chart_type[3]:
    st.write(sample_scatter)
if chart_type[4]:
    st.write(sample_stream)