# Agregamos unas variables que crean las rutas necesarias y archivos

# Importamos la libreria OS
import os


def creadorRutas(ruta):
    # Crear carpetas
    crear_carpetas = os.makedirs(ruta, exist_ok=True)


#creadorRutas()


def creadorArchivos(archivo):

    # Crear archivos
    crear_arhcivos = open(archivo, "w")




# Funcion que crea el entorno necesario
def creadorEntornoNecesario():

    # Crear carpetas
    creadorRutas("..\monbike\docs")


    # Crear archivos HTML
    creadorArchivos("..\monbike\docs\index.html")
    creadorArchivos("..\monbike\docs\general.html")
        
    # Crear archivos CSS
    creadorArchivos("..\monbike\docs\style.css")