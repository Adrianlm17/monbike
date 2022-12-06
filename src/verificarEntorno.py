# Creamos una Barricada para verificar si las rutas necesarias y archivos estan creadas

# Importamos la libreria OS
import os




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
