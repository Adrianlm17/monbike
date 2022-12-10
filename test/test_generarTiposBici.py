# Importamos las funciones necesarias para este caso TEST
from src.presentation.crearTiposBiciHtml import TiposBicis

# Importamos las librerias necesarias para PYTEST
import pytest



tipo = "carretera"

# Cuando se vaya a realizar este caso test ves al archivo "crearTiposBiciHtml.py" y agregar src. despues de los 2 from, dado que el main.py esta dentro de la carpeta "SRC"

@pytest.mark.test_generarCarretera
def test_generarCarretera():

    # Escribimos en la pagina los tipos de bici que son de carretera para hacer una prueba    
    TiposBicis(tipo)
        
    # Le indico a esta función que me busque el nombre de la bici carretera en su archivo, si esta sera diferente a -1 
    assert open("../monbike/docs/"+tipo+".html", "r").read().find('<h1 class="titulo_general"> Estas son todas las bicis  del tipo '+tipo+' que tenemos actualmente:</h1>') != -1
