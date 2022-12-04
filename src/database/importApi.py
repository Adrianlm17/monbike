# Importamos las librerias necesarias para la API de MongoDB
import requests
import json


def importarInfoAPI():

  # Importamos la URL de la API
  url = "https://data.mongodb-api.com/app/data-ltnil/endpoint/data/v1/action/find"


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
    'api-key': "nWyp9GCEj1fHBvPJOqpBmX8Kvf53JgMdxSsQOB2U0SkpfmivCUN55Yy5OPzEi2Q9", 
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
    # Metemos todo en un documento JSON 
    api_mongodb = open("../monbike/JSON/bicis.json", "w", encoding="utf-8")
    General = json.dump(result["documents"],api_mongodb, indent=4, ensure_ascii=False)    
    api_mongodb.close




importarInfoAPI()