# Casos test para verificar si las rutas estan creadas o no
from src.crearEntorno import *

# Importamos las librerias necesarias para PYTEST
import os
import pytest

# Creamos un archivo de prueba
rutaDocs = ".\docs\index.html"
rutaDocs = os.path.relpath(rutaDocs)




@pytest.mark.test_creadorArchivos
def test_creadorArchivos():

    # Creamos el archivo de la variable "rutaDocs"
    creadorArchivos(rutaDocs) 

    # Verificamos si existe
    assert os.path.exists(rutaDocs) != False



@pytest.mark.test_verificarArchivo
def test_verificarArchivo():


    # Creamos el archivo de la variable "rutaDocs"
    creadorArchivos(rutaDocs) 

    # Verifica si es un archivo
    assert os.path.isfile(rutaDocs) == True 

