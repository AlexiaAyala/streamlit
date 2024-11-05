# import streamlit as st
# st.title("hello world")
# st.write("Hola, ¿cómo estás?")
import streamlit as st
import pandas as pd 
import datetime

titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)

# Create the title for the web app
st.title("Titanic App")
# Creamos sidebar
sidebar = st.sidebar
# Agregamos title y texto en sidebar
sidebar.title("This is the sidebar.")
sidebar.write("You can add any elements to the sidebar.")

# ask user the current date
today = datetime.date.today()
today_date = sidebar.date_input('Cual es tu cumple : ', today)
#st.success('tu cumple es : `%s` felicidades ...' % (today_date))
st.success(f'tu cumple es: {today_date} felicidades...') 

# Display the content of the dataset if checkbox is true
st.header("Titanic Dataset")

agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:
  st.dataframe(titanic_data)
