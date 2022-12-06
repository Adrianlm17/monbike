import json
from importApi import importarInfoAPI

# Creamos una funcion que nos genere el archivo JSON
def crearJson(result):
    
    # Metemos todo en un documento JSON 
    api_mongodb = open("../monbike/JSON/bicis.json", "w", encoding="utf-8")
    General = json.dump(result["documents"],api_mongodb, indent=4, ensure_ascii=False)    
    api_mongodb.close
