# import streamlit as st
# st.title("hello world")
# st.write("Hola, ¿cómo estás?")
import streamlit as st
import pandas as pd 
names_link='C:/Users/alexia/Downloads/dataset.csv'
names_data=pd.read_csv(names_link)

#Creando el título
st.title("Streamlit and pandas")
st.dataframe(names_data)