# Creamos una Barricada para verificar si las rutas necesarias y archivos estan creadas


def verificarArchivo(archivo):
    try:
        # Abre el archivo generado   
        archivoAVerificar = open(archivo, "r")

    except FileNotFoundError:    
        print("El archivo "+ archivo +" no se creo!")    
        SystemExit()

    else: 
        archivoAVerificar.close



# Funcion que verifica los archivo necesarios
def verificarArchivoNecesario():
    
    # Crear archivos HTML
    verificarArchivo("..\monbike\docs\index.html")
    verificarArchivo("..\monbike\docs\general.html")
    verificarArchivo("..\monbike\docs\contacto.html")

    # Crea archivos HTML de las Ubicaciones
    verificarArchivo("..\monbike\docs\Alcúdia.html")
    verificarArchivo("..\monbike\docs\Artá.html")
    verificarArchivo("..\monbike\docs\Felanix.html")
    verificarArchivo("..\monbike\docs\Inca.html")
    verificarArchivo("..\monbike\docs\Manacor.html")
    verificarArchivo("..\monbike\docs\Marratxi.html")
    verificarArchivo("..\monbike\docs\Palma.html")
    verificarArchivo("..\monbike\docs\Pollensa.html")
    verificarArchivo("..\monbike\docs\Soller.html")

    # Crea archivos HTML de las marcas
    verificarArchivo("..\monbike\docs\Deporvillage.html")
    verificarArchivo("..\monbike\docs\Elops.html")
    verificarArchivo("..\monbike\docs\Focus.html")
    verificarArchivo("..\monbike\docs\Motion.html")
    verificarArchivo('../monbike/docs/NCM.html')
    verificarArchivo("..\monbike\docs\Riverside.html")
    verificarArchivo("..\monbike\docs\Rockrider.html")
    verificarArchivo("..\monbike\docs\SHIMANO.html")
    verificarArchivo("..\monbike\docs\TRIBAN.html")
    verificarArchivo("..\monbike\docs\VAN RYSEL.html")
    verificarArchivo("..\monbike\docs\Windee.html")

    # Crea archivos HTML de los tipos
    verificarArchivo("..\monbike\docs\carretera.html")
    verificarArchivo("..\monbike\docs\city.html")
    verificarArchivo("..\monbike\docs\eléctrica.html")
    verificarArchivo("..\monbike\docs\MTB.html")
    
    # Verifica archivos CSS
    verificarArchivo("..\monbike\docs\style.css")