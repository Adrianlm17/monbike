# Casos test para verificar si las rutas estan creadas o no
from src.crearEntorno import *

# Importamos las librerias necesarias para PYTEST
import os
import pytest


# Le indicamos una ruta de prueba
rutaDocs = ".\docs"
rutaDocs = os.path.relpath(rutaDocs)




@pytest.mark.test_creadorRutas
def test_creadorRutas():

    # Creamos la carpeta "docs"
    creadorRutas(rutaDocs) 

    # La carpeta existe
    assert os.path.exists(rutaDocs) != False



@pytest.mark.test_verificarDirectorio
def test_verificarDirectorio():
    
    # Creamos la carpeta "docs"
    creadorRutas(rutaDocs) 

    # Verifica si en la carpeta existe un directorio
    assert os.path.isdir(rutaDocs) == True 

