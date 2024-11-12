import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import datetime

titanic_link='C:/Users/alexia/Downloads/titanic_data.csv'
titanic_data=pd.read_csv(titanic_link)

st.title('Mi primera App con Streamlit')

sidebar=st.sidebar

sidebar.title('Esta es la barra lateral.')
sidebar.write('Aquí van los elementos de entrada')

st.title('Información sobre el conjunto de datos')
st.header('Descripción de los datos')
st.markdown('_____')

today=datetime.date.today()
today_date=st.date_input('Current date', today)
st.success('Current date `%s`' %(today_date))
st.markdown('_____')

st.header('Dataset')
agree=st.checkbox('show Dataset overview?')
if agree:
    st.dataframe(titanic_data)
st.markdown('_____')

st.header('Data description')
selected_class=st.radio('Select class', titanic_data['class'].unique())
st.write('Selected Class:', selected_class)
st.markdown('_____')

optionals=st.expander('Optional Configurations', True)
fare_select=optionals.slider(
    'Select the Fare',
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare=titanic_data[(titanic_data['fare']>= fare_select)]
st.write(f'Number of records with this Fare {fare_select}: {subset_fare.shape[0]}')
st.markdown('_____')

fig, ax=plt.subplots()
ax.hist(titanic_data.fare)
st.header('Histograma del Titanic')
st.pyplot(fig)
st.markdown('_____')

fig2, ax2 =plt.subplots()
y_pos=titanic_data['class']
x_pos=titanic_data['fare']
ax2.barh(y_pos,x_pos)
ax2.set_ylabel('Class')
ax2.set_xlabel('Fare')
ax2.set_title=('¿Cuánto pagaron las clases del Titanic?')
st.header('Grafica de Barras del Titanic')
st.pyplot(fig2)
st.markdown('_____')

fig3, ax3=plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel('Edad')
ax3.set_ylabel('Tarifa')
st.header('Grafica de Dispersión del Titanic')
st.pyplot(fig3)