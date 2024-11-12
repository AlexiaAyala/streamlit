import streamlit as st
import pandas as pd 

st.title('Streamlit -  Search by sex')

DATA_URL=('C:/Users/alexia/Downloads/dataset.csv')

data=pd.read_csv(DATA_URL)

@st.cache
def load_data_bysex(sex):
    filtered_data_bysex= data[data['sex'].str.contains(sex)]
    return filtered_data_bysex

selected_sex = st.selectbox("Select Sex", data['sex'].unique())
btnRange= st.button('Search by sex')

if(btnRange):
    filterbyrange = load_data_bysex(selected_sex)
    count_row=filterbyrange.shape[0]
    st.write(f"Total items : {count_row}")

st.dataframe(filterbyrange)