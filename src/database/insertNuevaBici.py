# Importamos las librerias necesarias para la API de MongoDB
import requests
import json
import os



def insertNuevaBici():

    # Preguntamos la información necesaria
    nombreBici = input("Escribe el nombre de la bici: ")
    tipoBici = input("Que tipo de bici es: ")
    precioBici = input("Que precio por día quieres ponerle? ")
    ubicacionBici = input("En que ubicaciónes se encuentra esta bici? ")
    stockBici = input("Cantidad de stock: ")
    materialBici = input("Material de la bici: ")
    marcaBici = input("Que marca es? ")
    tallaBici = input("Indica la talla de la bici: ")
    pesoBici = input("Indica el peso de la bici: ")
    frenoBici = input("Que tipo de frenos tiene? ")
    imgBici = input("Escriba la URL de la imagen: ")
    seguroBici = input("Tiene seguro? ")
    empresaBici = input("Que empresa la alquila?")

    # Llamamos desde la variable de entorno la URL de la API

    MONGO_URL = os.environ['MONGO_URL']
    API_KEY = os.environ['API_KEY']

    # Modificamos la URL de la API y añadimos "insertOne"
    url = MONGO_URL+"/insertOne"


    # Le indicamos las caracteristicas que vamos a utilizar
    payload = json.dumps({
        "collection": "bicicletas",
        "database": "monbike",
        "dataSource": "MonBike",
        "document":{
        "nombre": nombreBici,
        "precio": precioBici,
        "ubicación": ubicacionBici,
        "stock": stockBici,
        "material": materialBici,
        "marca de bici": marcaBici,
        "peso": pesoBici,
        "img": imgBici,
        "tipo de bici": tipoBici,
        "seguro": seguroBici,
        "talla": tallaBici,
        "tipo de frenos": frenoBici,
        "empresa": empresaBici
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY, 
    }

    response = requests.request("POST", url, headers=headers, data=payload,)
    print("Bicicleta creada con existo! Aqui tienes su ID:" + response.text)
        
insertNuevaBici()