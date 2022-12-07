# Al ejecutar este archivo se creara todo automaticamente


def ejecutarTrabajo():

    # Importamos la API
    from database.importApi import importarInfoAPI
    datosMongo = importarInfoAPI()
    
    # Creamos el archivo JSON a partir de la API
    from database.crearJson import crearJson
    crearJson(datosMongo)

    # Creamos el entorno necesario
    from crearEntorno import creadorEntornoNecesario
    creadorEntornoNecesario()

    # Agregamos la Barricada
    from verificarEntorno import verificarArchivoNecesario
    verificarArchivoNecesario()

    # Importamos el contenido JSON
    from presentation.importJson import importarDatos
    importarDatos()

    # Generamos los archivos HTML y CSS
    from presentation.crearIndexHtml import generarIndexHtml
    from presentation.crearGeneralHtml import generarPaginaTodasBicis
    from presentation.crearStyleCss import generarArchivoCss
    generarIndexHtml()
    generarPaginaTodasBicis()
    generarArchivoCss()
    
    print("Todo se genero con exito!")



ejecutarTrabajo()