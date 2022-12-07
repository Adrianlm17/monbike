# Al ejecutar este archivo se creara todo automaticamente


# Importamos todas las funciones necesarias
from database.importApi import importarInfoAPI
from database.crearJson import crearJson
from crearEntorno import creadorEntornoNecesario
from verificarEntorno import verificarArchivoNecesario
from presentation.importJson import importarDatos
from presentation.crearIndexHtml import generarIndexHtml
from presentation.crearGeneralHtml import generarPaginaTodasBicis
from presentation.crearStyleCss import generarArchivoCss




def ejecutarTrabajo():

    # Importamos la API
    datosMongo = importarInfoAPI()
    
    # Creamos el archivo JSON a partir de la API
    crearJson(datosMongo)

    # Creamos el entorno necesario
    creadorEntornoNecesario()

    # Agregamos la Barricada
    verificarArchivoNecesario()

    # Importamos el contenido JSON
    importarDatos()

    # Generamos los archivos HTML y CSS
    generarIndexHtml()
    generarPaginaTodasBicis()
    generarArchivoCss()
    
    print("Todo se genero con exito!")



ejecutarTrabajo()