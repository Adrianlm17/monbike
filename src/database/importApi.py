# Importamos las librerias necesarias para la API de MongoDB
import requests
import json
import os


def importarInfoAPI():

  # Llamamos desde la variable de entorno la URL de la API

  MONGO_URL = os.environ['MONGO_URL']
  API_KEY = os.environ['API_KEY']

  # Modificamos la URL de la API y añadimos "find"
  url = MONGO_URL+"/find"


  # Le indicamos las caracteristicas que vamos a utilizar
  payload = json.dumps({
      "collection": "bicicletas",
      "database": "monbike",
      "dataSource": "MonBike",
      "projection": {
      }
  })

  headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': API_KEY, 
  }

  try:    
    # Convertimos la API con su información en una variable de Python
    datosApi = requests.post(url, headers=headers, data=payload) 
    result = (datosApi.text)    
    result = json.loads(result)

  # Agrego una pequeña verificación de la API (en caso de error nos mandara un error o otro)
  except requests.exceptions.Timeout:    
    print("Error: Timeout")    
    SystemExit()

  except requests.exceptions.ConnectionError:    
    print("Ha ocurrido un error de Conexión")    
    SystemExit()  

  else: 
    print("API Importada con existo!")
    return result
    