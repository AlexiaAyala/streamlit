import streamlit as st
import pandas as pd 
import numpy as np

map_data=pd.DataFrame(
    np.random.randn(1000,2)/[50,50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.title('San Francisco Map')
st.header('Using Streamlit and Mapbox')

st.map(map_data)
st.markdown('_____')

st.title('Uber pickups in NYC')

DATE_COLUMN='date/time'
DATA_URL=('C:/Users/alexia/Downloads/uber_dataset.csv')

@st.cache_data
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase=lambda x:str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state=st.text('Loading data...')
data=load_data(1000)
data_load_state.text('Done! (using st.cache_data)')

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data=data[data[DATE_COLUMN].dt.hour==hour_to_filter]
st.map(filtered_data)