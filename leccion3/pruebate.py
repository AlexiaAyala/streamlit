import streamlit as st
import pandas as pd 

DATA_URL=('C:/Users/alexia/Downloads/movies.csv')
data_movie=pd.read_csv(DATA_URL, encoding='latin1')


def load_data_bydirector(director):
    data= data_movie[data_movie['director'].str.contains(director)]
    return data

sidebar=st.sidebar

sidebar.title('Directores disponibles')
selected_director = sidebar.selectbox("", data_movie['director'].unique())

# name_title=st.text_input('Título: ')
btnSearch= sidebar.button('Buscar por director')
if btnSearch:
    st.dataframe(load_data_bydirector(selected_director))