# Importamos las funciones necesarias para este caso TEST
from src.database.crearJson import crearJson


# Importamos las librerias necesarias para PYTEST
import pytest
import os



dato = {"documents" : [{"_id": "X","nombre": "X","precio": "X","ubicación": "X","stock": "X","material": "X","marca de bici": "X","garantia": "X","tallas": "X","peso": "X","img": "X", "tipo de freno": "X", "tipo de bici": "X"}]}



@pytest.mark.test_contieneTexto
def test_contieneTexto():
    
    crearJson(dato)

    # Verificamos si tiene el archivo "bicis.js" contenido
    assert os.stat("./JSON/bicis.json").st_size != 0
