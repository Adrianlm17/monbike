# Creamos una Barricada para verificar si las rutas necesarias y archivos estan creadas


def verificarArchivo(archivo):
    try:
        # Abre el archivo generado   
        archivoAVerificar = open(archivo, "r")

    except FileNotFoundError:    
        print("El/Los archivo/s no se creo/crearon!")    
        SystemExit()

    else: 
        archivoAVerificar.close
        print("El/Los archivo/s ha/n sido verificado/s con exito!")



# Funcion que verifica los archivo necesarios
def verificarArchivoNecesario():
    
    # Verifica archivos HTML
    verificarArchivo("..\monbike\docs\index.html")
    verificarArchivo("..\monbike\docs\general.html")
    
    # Verifica archivos CSS
    verificarArchivo("..\monbike\docs\style.css")