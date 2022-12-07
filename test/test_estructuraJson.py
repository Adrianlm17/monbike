# Importamos las funciones necesarias para este caso TEST
from src.database.crearJson import crearJson


# Importamos las librerias necesarias para PYTEST
import pytest




dato = {"documents" : [{"_id": "X","nombre": "X","precio": "X","ubicación": "X","stock": "X","material": "X","marca de bici": "X","garantia": "X","tallas": "X","peso": "X","img": "X", "tipo de freno": "X", "tipo de bici": "X"}]}

contieneID = "_id"

noContieneID = "ID"

contienePrecio = "precio"

noContienePrecio = "errorPrecio"


@pytest.mark.test_contieneID
def test_contieneID():
    
    crearJson(dato)


    # Nos indica que la variable "contieneID" existe en el archivo "bicis.json"
    assert open("../monbike/JSON/bicis.json", "r").read().find(contieneID) != -1


@pytest.mark.test_noContieneID
def test_noContieneID():
    
    crearJson(dato)


    # Nos indica que la variable "noContieneID" NO existe en el archivo "bicis.json"
    assert open("../monbike/JSON/bicis.json", "r").read().find(noContieneID) == -1


@pytest.mark.test_contienePrecio
def test_contienePrecio():
    
    crearJson(dato)


    # Nos indica que la variable "contienePrecio" existe en el archivo "bicis.json"
    assert open("../monbike/JSON/bicis.json", "r").read().find(contienePrecio) != -1


@pytest.mark.test_noContienePrecio
def test_noContienePrecio():
    
    crearJson(dato)


    # Nos indica que la variable "noContienePrecio" NO existe en el archivo "bicis.json"
    assert open("../monbike/JSON/bicis.json", "r").read().find(noContienePrecio) == -1

