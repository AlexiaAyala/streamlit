import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

path='C:/Users/alexia/Downloads/'
cred= credentials.Certificate(path+'names-firebase.json') 
firebase_admin.initialize_app(cred)

db=firestore.client()
doc_ref = db.collection(u'names') #Set the name of Collection
#Import data
df=pd.read_csv(path+'demo_names_dataset.csv')
tmp=df.to_dict(orient='records')
list(map(lambda x: doc_ref.add(x), tmp))
