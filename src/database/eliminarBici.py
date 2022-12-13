# Importamos las librerias necesarias para la API de MongoDB
import requests
import json
import os



def eliminarBici():

    # Preguntamos la información necesaria
    idBici = input("Indica el ID de la bici que quieres eliminar: ")

    # Llamamos desde la variable de entorno la URL de la API

    MONGO_URL = os.environ['MONGO_URL']
    API_KEY = os.environ['API_KEY']

    # Modificamos la URL de la API y añadimos "deleteOne"
    url = MONGO_URL+"/deleteOne"


    # Le indicamos las caracteristicas que vamos a utilizar
    payload = json.dumps({
        "collection": "bicicletas",
        "database": "monbike",
        "dataSource": "MonBike",
        "filter":{ "_id": { "$oid": idBici } }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY, 
    }

    response = requests.request("POST", url, headers=headers, data=payload,)

eliminarBici()
