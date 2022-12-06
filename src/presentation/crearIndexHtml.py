# Importamos la libreria JSON
import json
from importJson import importarDatos
from variablesHtml import *

bicis = importarDatos()

def generarIndexHtml():
    # Aqui ejecutamos el codigo que nos crea/sobre escribe "index.html" en el directorio "docs" y le ponemos la siguiente estructura HTML:
    index_html = open("../monbike/docs/index.html", "w", encoding="utf-8")

    index_html.write(head)
    index_html.write(body)

    index_html.write("<h1> MonBike </h1>\n")
    index_html.write("<a href='general.html'> TODAS LAS BICIS </a>\n")
    index_html.write(fin_body)
    index_html.write("</head>\n")

generarIndexHtml()

