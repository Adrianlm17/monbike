# Casos TEST para la Barricada 
from src.verificarEntorno import *

# Importamos las librerias necesarias para PYTEST
import os
import pytest


# Verificamos un archivo de prueba
archivoCreado = "./docs/index.html"
archivoCreado= os.path.relpath(archivoCreado)

archivoNoCreado = "./docs/NoCreado.html"
archivoNoCreado= os.path.relpath(archivoNoCreado)





@pytest.mark.test_verificarArchivoCreado
def test_verificarArchivoCreado():

    # Realiza la funcion "verificarArchivo" si el archivo existe o no
    verificarArchivo(archivoCreado) 

    # Es igual a True dado que el archivo esta creado
    assert os.path.exists(archivoCreado) == True



@pytest.mark.test_verificarArchivoNoCreado
def test_verificarArchivoNoCreado():

    # Realiza la funcion "verificarArchivo" si el archivo existe o no
    verificarArchivo(archivoNoCreado) 

    # Es igual a False dado que el archivo "NO" esta creado
    assert os.path.exists(archivoNoCreado) == False