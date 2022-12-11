# Agregamos unas variables que crean las rutas necesarias y archivos

# Importamos la libreria OS
import os

# Importamos la función rmtree que nos permite eliminar carpetas con contenido
from shutil import rmtree


def eliminarEntorno(ruta):
    # Eliminamos el entorno por seguridad
    rmtree(ruta)

def creadorRutas(ruta):
    # Crear carpetas
    crear_carpetas = os.makedirs(ruta, exist_ok=True)


#creadorRutas()


def creadorArchivos(archivo):

    # Crear archivos
    crear_arhcivos = open(archivo, "w")




# Funcion que crea el entorno necesario
def creadorEntornoNecesario():

    # Eliminamos la carpeta docs por seguridad
    eliminarEntorno("..\monbike\docs")
    print("Entorno eliminado con exito!")

    # Crear carpetas
    creadorRutas("..\monbike\docs")


    # Crear archivos HTML
    creadorArchivos("..\monbike\docs\index.html")
    creadorArchivos("..\monbike\docs\general.html")
    creadorArchivos("..\monbike\docs\contacto.html")

    # Crea archivos HTML de las Ubicaciones
    creadorArchivos("..\monbike\docs\Alcúdia.html")
    creadorArchivos("..\monbike\docs\Artá.html")
    creadorArchivos("..\monbike\docs\Felanix.html")
    creadorArchivos("..\monbike\docs\Inca.html")
    creadorArchivos("..\monbike\docs\Manacor.html")
    creadorArchivos("..\monbike\docs\Marratxi.html")
    creadorArchivos("..\monbike\docs\Palma.html")
    creadorArchivos("..\monbike\docs\Pollensa.html")
    creadorArchivos("..\monbike\docs\Soller.html")

    # Crea archivos HTML de las marcas
    creadorArchivos("..\monbike\docs\Deporvillage.html")
    creadorArchivos("..\monbike\docs\Elops.html")
    creadorArchivos("..\monbike\docs\Focus.html")
    creadorArchivos("..\monbike\docs\Motion.html")
    creadorArchivos('../monbike/docs/NCM.html')
    creadorArchivos("..\monbike\docs\Riverside.html")
    creadorArchivos("..\monbike\docs\Rockrider.html")
    creadorArchivos("..\monbike\docs\SHIMANO.html")
    creadorArchivos("..\monbike\docs\TRIBAN.html")
    creadorArchivos("..\monbike\docs\VAN RYSEL.html")
    creadorArchivos("..\monbike\docs\Windee.html")

    # Crea archivos HTML de los tipos
    creadorArchivos("..\monbike\docs\carretera.html")
    creadorArchivos("..\monbike\docs\city.html")
    creadorArchivos("..\monbike\docs\eléctrica.html")
    creadorArchivos("..\monbike\docs\MTB.html")
        
    # Crear archivos CSS
    creadorArchivos("..\monbike\docs\style.css")