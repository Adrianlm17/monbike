# Importamos la libreria JSON
import json
from importJson import importarDatos
from variablesHtml import *

bicis = importarDatos()

def generarPaginaTodasBicis():
    general_html = open("../monbike/docs/general.html", "w", encoding="utf-8")
    
    # HEAD del HTML
    general_html.write(head)
    
    # BODY del HTMl
    general_html.write(body)
    
    # HEADER del HTML
    general_html.write(header)

    general_html.write('    <h1 class="titulo_general"> Estas son todas las bicis que tenemos actualmente:</h1>\n')
    general_html.write(div_global)
    

    # Creo un bucle el cual nos escribe todas las bicis con una pequeña descripción y un boton de alquiler
    i = 0
    for bici in bicis:
        general_html.write(general_unica_bici)
        general_html.write("        <img src='"+ bicis[i]["img"] +"' class='img_varias_bicis'>\n")
        general_html.write("        <h2>"+ bicis[i]["nombre"] +"</h2>\n")
        general_html.write('        <p>\n          1 Día   - ' + bicis[i]["precio"] + '€ <br>\n          5 Días  - ' + bicis[i]["precio"] + '€ <br>\n          10 Días  - ' + bicis[i]["precio"] + '€ <br>\n          15 Días - ' + bicis[i]["precio"] + '€ <br>\n          30 Días - ' + bicis[i]["precio"] + '€\n        </p>\n')
        general_html.write(br_global)
        general_html.write("        <a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")
        general_html.write(fin_div)

        i += 1

    general_html.write(fin_div_general)
    general_html.write(footer)
    general_html.write(fin_body)
    general_html.write(fin_html)

generarPaginaTodasBicis()