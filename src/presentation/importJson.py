# Importamos la libreria de JSON
import json


# Creamos una funcion que nos sacara la información del archivo JSON y metera todo en la variable bicis
def importarDatos():
    
    # Abrimos el archivo JSON en modo de lectura y cargamos los datos en la variable "bicicletas"
    with open("../monbike/JSON/bicis.json", encoding="utf-8") as datos:
        bicicletas = datos.read()

        # Cargar los datos de la variable "bicicletas" en una variable llamada "bicis"
        bicis = json.loads(bicicletas)
        return bicis

