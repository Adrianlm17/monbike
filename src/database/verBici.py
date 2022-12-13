# Importamos las librerias necesarias para la API de MongoDB
import requests
import json
import os



def visualizarTodasBicis():

    # Llamamos desde la variable de entorno la URL de la API

    MONGO_URL = os.environ['MONGO_URL']
    API_KEY = os.environ['API_KEY']

    # Modificamos la URL de la API y añadimos "insertOne"
    url = MONGO_URL+"/find"


    # Le indicamos las caracteristicas que vamos a utilizar
    payload = json.dumps({
        "collection": "bicicletas",
        "database": "monbike",
        "dataSource": "MonBike",
        "filter" : {

        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY, 
    }

    response = requests.request("POST", url, headers=headers, data=payload,)
    print(response.text)


def visualizarUnaBici():

    # Preguntamos la información necesaria
    idBici = input("Escribe el ID de la bici que quieres visualizar: ")

    # Llamamos desde la variable de entorno la URL de la API

    MONGO_URL = os.environ['MONGO_URL']
    API_KEY = os.environ['API_KEY']

    # Modificamos la URL de la API y añadimos "insertOne"
    url = MONGO_URL+"/findOne"


    # Le indicamos las caracteristicas que vamos a utilizar
    payload = json.dumps({
        "collection": "bicicletas",
        "database": "monbike",
        "dataSource": "MonBike",
        "projection" : {
            "_id": idBici,
            "nombre": 1,
            "precio": 1,
            "ubicación": 1,
            "stock": 1,
            "material": 1,
            "marca de bici": 1,
            "peso": 1,
            "img": 1,
            "tipo de bici": 1,
            "seguro": 1,
            "talla": 1,
            "tipo de frenos": 1,
            "empresa": 1
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY, 
    }

    response = requests.request("POST", url, headers=headers, data=payload,)
    print(response.text)
        
        
def verBicis():
    opcion = input(f"""Indica que quieres ver:
    - Opción (1): visualizar todas las bicis
    - Opción (2): ver una sola bici
    """)
    if opcion == "1":
        visualizarTodasBicis()
    else:
        visualizarUnaBici()

verBicis()
