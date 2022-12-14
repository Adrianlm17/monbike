# Al ejecutar este archivo se creara todo automaticamente

# Importamos webbrowser
import webbrowser






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
    print("Entorno creado y verificado con exito!")

    # Importamos el contenido JSON
    from presentation.importJson import importarDatos
    importarDatos()

    # Generamos los archivos HTML y CSS
    from presentation.crearIndexHtml import generarIndexHtml
    from presentation.crearGeneralHtml import generarPaginaTodasBicis
    from presentation.crearTiposBiciHtml import generarTipoBici
    from presentation.crearMarcasBiciHtml import generarMarcaBici
    from presentation.crearUbicacionBiciHtml import generarUbicacionesBici
    from presentation.crearContacto import ContactoBicis
    from presentation.crearUnicaBiciHtml import generarUnicaBiciHtml
    from presentation.crearStyleCss import generarArchivoCss
    generarIndexHtml()
    generarPaginaTodasBicis()
    generarTipoBici()
    generarMarcaBici()
    generarUbicacionesBici()
    generarUnicaBiciHtml()
    ContactoBicis()
    generarArchivoCss()
    
    print("Todo se genero con exito!")


ejecutarTrabajo()
