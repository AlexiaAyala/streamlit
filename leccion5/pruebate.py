import streamlit as st
import pandas as pd
from google.cloud import firestore

db= firestore.Client.from_service_account_json('C:/Users/alexia/Downloads/products-project-firebase.json')
dbNames= db.collection('products')

prod_dataframeg=pd.DataFrame(None)

st.title('CRUD Products')
st.markdown('_____')
def carga_dataset():
    prod_ref= list(db.collection(u'products').stream())
    prod_dict= list(map(lambda x: x.to_dict(), prod_ref))
    prod_dataframe= pd.DataFrame(prod_dict)
    global prod_dataframeg
    prod_dataframeg=prod_dataframe

carga_dataset()
dt_products= st.dataframe(prod_dataframeg)


st.markdown('_____')
st.header('Nuevo registro')

cod = st.text_input('Código:')
nombre = st.text_input('Nombre:')
precio = st.text_input('Precio:')
existencias = st.text_input('Existencias:')
stock_min = st.text_input('Stock Mínimo:')
stock_max = st.text_input('Stock Máximo:')

submit= st.button('Crear nuevo registro')

#Once the name has submitted, upload it to the database
if cod and nombre and precio and existencias and stock_min and stock_max and submit:
    doc_ref = db.collection('products').document(cod)
    doc_ref.set({
        'codigo':int(cod),
        'existencias':int(existencias),
        'nombre':nombre,
        'precio':float(precio),
        'stock_maximo':int(stock_max),
        'stock_minimo':int(stock_min)
    })
    st.sidebar.write('Registro insertado correctamente')
    carga_dataset()

def loadByName(name):
    names_ref=dbNames.where(u'nombre', u'==', name)
    currentName= None
    for myName in names_ref.stream():
        currentName=myName
    return currentName

btnFiltrar= st.button('Buscar')
if btnFiltrar:
    doc= loadByName(nombre)
    if doc is None:
        st.sidebar.write('Nombre no existe :(')
    else:
        st.sidebar.write(doc.to_dict())

btnActualizar= st.button('Actualizar')
if btnActualizar:
    updatename=loadByName(nombre)
    if updatename is None:
        st.sidebar.write(f'{nombre} no existe')
    else:
        myupdatename= dbNames.document(updatename.id)
        myupdatename.update(
            {
                'existencias':int(existencias),
                'nombre':nombre,
                'precio':float(precio),
                'stock_maximo':int(stock_max),
                'stock_minimo':int(stock_min)
            }
        )

btnEliminar= st.button('Eliminar')
if btnEliminar:
    deletename= loadByName(nombre)
    if deletename is None:
        st.sidebar.write(f'{nombre} no existe')
    else:
        dbNames.document(deletename.id).delete()
        st.sidebar.write(f'{nombre} eliminado')