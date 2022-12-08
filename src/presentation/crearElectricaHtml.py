# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()


def ElectricasBicis():
    electrica_html = open("../monbike/docs/electrica.html", "w", encoding="utf-8")
    
    # HEAD del HTML
    electrica_html.write(head)
    
    # BODY del HTMl
    electrica_html.write(body)
    
    # HEADER del HTML
    electrica_html.write(header)

    electrica_html.write('    <h1 class="titulo_general"> Estas son todas las bicis Eléctricas que tenemos actualmente:</h1>\n')
    electrica_html.write(div_global)
    

    # Creo un bucle el cual nos escribe todas las bicis eléctrica con el precio y un boton de alquiler
    i = 0

    for bici in bicis:
        if bici['tipo de bici'] == "eléctrica":
            electrica_html.write(general_unica_bici)
            electrica_html.write("        <img src='"+ bicis[i]["img"] +"' class='img_varias_bicis'>\n")
            electrica_html.write("        <h2>"+ bicis[i]["nombre"] +"</h2>\n")

            # Agregamos 2 variables seun descuento segun los dias de alquiler
            descuentoGrande = int(bicis[i]["precio"]) - 2
            descuentoPequeño = int(bicis[i]["precio"]) - 1

            # Escribe el precio con su respectivo descuento en HTML
            electrica_html.write('        <p>\n          1 Día   - ' + bicis[i]["precio"] + '€ <br>\n          5 Días  - ' + str(descuentoGrande) + '€ <br>\n          10 Días  - ' + str(descuentoPequeño) + '€ <br>\n          15 Días - ' + str(descuentoPequeño) + '€ <br>\n          30 Días - ' + str(descuentoGrande) + '€\n        </p>\n')
            
            electrica_html.write(br_global)
            electrica_html.write("        <a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")
            electrica_html.write(fin_div)

        i += 1

    electrica_html.write(fin_div_general)
    electrica_html.write(footer)
    electrica_html.write(fin_body)
    electrica_html.write(fin_html)