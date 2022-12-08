# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()


def PaseoBicis():
    paseo_html = open("../monbike/docs/paseo.html", "w", encoding="utf-8")
    
    # HEAD del HTML
    paseo_html.write(head)
    
    # BODY del HTMl
    paseo_html.write(body)
    
    # HEADER del HTML
    paseo_html.write(header)

    paseo_html.write('    <h1 class="titulo_general"> Estas son todas las bicis Paseo que tenemos actualmente:</h1>\n')
    paseo_html.write(div_global)
    

    # Creo un bucle el cual nos escribe todas las bicis paseo con el precio y un boton de alquiler
    i = 0

    for bici in bicis:
        if bici['tipo de bici'] == "city":
            paseo_html.write(general_unica_bici)
            paseo_html.write("        <img src='"+ bicis[i]["img"] +"' class='img_varias_bicis'>\n")
            paseo_html.write("        <h2>"+ bicis[i]["nombre"] +"</h2>\n")

            # Agregamos 2 variables seun descuento segun los dias de alquiler
            descuentoGrande = int(bicis[i]["precio"]) - 2
            descuentoPequeño = int(bicis[i]["precio"]) - 1

            # Escribe el precio con su respectivo descuento en HTML
            paseo_html.write('        <p>\n          1 Día   - ' + bicis[i]["precio"] + '€ <br>\n          5 Días  - ' + str(descuentoGrande) + '€ <br>\n          10 Días  - ' + str(descuentoPequeño) + '€ <br>\n          15 Días - ' + str(descuentoPequeño) + '€ <br>\n          30 Días - ' + str(descuentoGrande) + '€\n        </p>\n')
            
            paseo_html.write(br_global)
            paseo_html.write("        <a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")
            paseo_html.write(fin_div)

        i += 1

    paseo_html.write(fin_div_general)
    paseo_html.write(footer)
    paseo_html.write(fin_body)
    paseo_html.write(fin_html)