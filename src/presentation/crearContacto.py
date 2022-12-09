# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()


def ContactoBicis():
    contacto_html = open("../monbike/docs/contacto.html", "w", encoding="utf-8")
    
    # HEAD del HTML
    contacto_html.write(head)
    
    # BODY del HTMl
    contacto_html.write(body)
    
    # HEADER del HTML
    contacto_html.write(header)

    # Contacto
    contacto_html.write(contacto)

    contacto_html.write(footer)
    contacto_html.write(fin_body)
    contacto_html.write(fin_html)