import json
import os

# Creamos una funcion que nos genere el archivo JSON
def crearJson(result):
    
    # Le ponemos una precondición, para verificar que tiene texto!
    assert len(result) != 0, "La API importada a texto no tiene contenido!"
    
    
    # Metemos todo en un documento JSON 
    api_mongodb = open("../monbike/JSON/bicis.json", "w", encoding="utf-8")
    General = json.dump(result["documents"],api_mongodb, indent=4, ensure_ascii=False)    
    api_mongodb.close
    print("Archivo JSON creado con exito!")
