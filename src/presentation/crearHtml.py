# Importamos la libreria JSON
import json
from importJson import importarDatos

bicis = importarDatos()


# Aqui ejecutamos el codigo que nos crea/sobre escribe "index.html" en el directorio "docs" y le ponemos la siguiente estructura HTML:
index_html = open("../monbike/docs/index.html", "w")

index_html.write("<!DOCTYPE html>\n")
index_html.write("<html lang=es>\n")

index_html.write("<head>\n")  
index_html.write("<meta charset='UTF-8'>\n")
index_html.write("<title>MonBike</title>\n")
index_html.write("</head>\n")

index_html.write("<body>\n")

# Creo una pequeña prueba para que escriba todos los nombres con sus respectivas imagenes y futuros enlaces
i = 0
for bici in bicis:
    index_html.write("<h1>"+ bicis[i]["nombre"] +"</h1>\n")
    index_html.write("<img src='"+ bicis[i]["img"] +"'>\n")
    index_html.write("<a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")

    i += 1

index_html.write("</body>\n")
index_html.write("</head>\n")

