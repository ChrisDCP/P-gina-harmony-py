import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate('./firebase-credentials.json')
firebase_admin.initialize_app(cred,{'databaseURL': 'https://harmony-space-59144-default-rtdb.firebaseio.com/'})

