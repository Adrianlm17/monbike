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












# ------------------------------------ MENU MONBIKE -------------------------------------

def menuMonBike():
    
    opcionMonBike = input(f'''--------------- MONBIKE ---------------
|                                     |
|                                     |
|    Bienvenid@, Este es el Menú      |
|               MONBIKE!              |
|                                     |
|                                     |
|    Indica que deseas hacer de las   |
|   siguientes opciones disponibles:  |
|                                     |
|   1. Insertar una nueva Bici        |
|   2. Eliminar una Bici              |
|   3. Modificar una Bici             |
|   4. Ejecutar la pagina web         |
|   5. Ver la pagina web              |
|   6. Salir del Menú                 |
|                                     |
--------------------------------------- 
''')

    if opcionMonBike == "1":
        
        # Funcion crear nueva bici
        from database.insertNuevaBici import insertNuevaBici
        insertNuevaBici()
        
        # Preguntamos al usuario si quiere seguir en el menu o no
        MenuMonBike = input("Deseas volver al Menú MonBike (S)/(N): ")

        if MenuMonBike == "S" or MenuMonBike == "Si" or MenuMonBike == "SI" or MenuMonBike == "s" or MenuMonBike == "si":
            menuMonBike()
        else:
            print("Hasta pronto!")
            exit

    elif opcionMonBike == "2":

        # Funcion eliminar una bici
        from database.eliminarBici import eliminarBici
        eliminarBici()

        # Preguntamos al usuario si quiere seguir en el menu o no
        MenuMonBike = input("Deseas volver al Menú MonBike (S)/(N): ")

        if MenuMonBike == "S" or MenuMonBike == "Si" or MenuMonBike == "SI" or MenuMonBike == "s" or MenuMonBike == "si":
            menuMonBike()
        else:
            print("Hasta pronto!")
            exit

    elif opcionMonBike == "3":

        # Funcion modificar una bici
        from database.modificarBici import modificarBici
        modificarBici()
    
        # Preguntamos al usuario si quiere seguir en el menu o no
        MenuMonBike = input("Deseas volver al Menú MonBike (S)/(N): ")

        if MenuMonBike == "S" or MenuMonBike == "Si" or MenuMonBike == "SI" or MenuMonBike == "s" or MenuMonBike == "si":
            menuMonBike()
        else:
            print("Hasta pronto!")
            exit

    elif opcionMonBike == "4":
        ejecutarTrabajo()

        # Preguntamos al usuario si quiere seguir en el menu o no
        MenuMonBike = input("Deseas volver al Menú MonBike (S)/(N): ")

        if MenuMonBike == "S" or MenuMonBike == "Si" or MenuMonBike == "SI" or MenuMonBike == "s" or MenuMonBike == "si":
            menuMonBike()
        else:
            print("Disfruta de la web y hasta pronto!")
            exit

    elif opcionMonBike == "5":
        webbrowser.open_new_tab('https://adrianlm17.github.io/monbike/')

        # Preguntamos al usuario si quiere seguir en el menu o no
        MenuMonBike = input("Deseas volver al Menú MonBike (S)/(N): ")

        if MenuMonBike == "S" or MenuMonBike == "Si" or MenuMonBike == "SI" or MenuMonBike == "s" or MenuMonBike == "si":
            menuMonBike()
        else:
            print("Disfruta de la web y hasta pronto!")
            exit

    elif opcionMonBike == "6":
        print("Hasta pronto!")
        exit

    else:
        print("Selecciona un numero valido!")
        menuMonBike()


menuMonBike()