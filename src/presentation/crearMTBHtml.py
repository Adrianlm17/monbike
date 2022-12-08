# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()


# Creo una funcion que crea las paginas para cada tipo de bici

def MtbBicis():
    mtb_html = open("../monbike/docs/mtb.html", "w", encoding="utf-8")
    
    # HEAD del HTML
    mtb_html.write(head)
    
    # BODY del HTMl
    mtb_html.write(body)
    
    # HEADER del HTML
    mtb_html.write(header)

    mtb_html.write('    <h1 class="titulo_general"> Estas son todas las bicis MTB que tenemos actualmente:</h1>\n')
    mtb_html.write(div_global)
    

    # Creo un bucle el cual nos escribe todas las bicis MTB con el precio y un boton de alquiler
    i = 0

    for bici in bicis:
        if bici['tipo de bici'] == "MTB":
            mtb_html.write(general_unica_bici)
            mtb_html.write("        <img src='"+ bicis[i]["img"] +"' class='img_varias_bicis'>\n")
            mtb_html.write("        <h2>"+ bicis[i]["nombre"] +"</h2>\n")

            # Agregamos 2 variables seun descuento segun los dias de alquiler
            descuentoGrande = int(bicis[i]["precio"]) - 2
            descuentoPequeño = int(bicis[i]["precio"]) - 1

            # Escribe el precio con su respectivo descuento en HTML
            mtb_html.write('        <p>\n          1 Día   - ' + bicis[i]["precio"] + '€ <br>\n          5 Días  - ' + str(descuentoGrande) + '€ <br>\n          10 Días  - ' + str(descuentoPequeño) + '€ <br>\n          15 Días - ' + str(descuentoPequeño) + '€ <br>\n          30 Días - ' + str(descuentoGrande) + '€\n        </p>\n')
            
            mtb_html.write(br_global)
            mtb_html.write("        <a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")
            mtb_html.write(fin_div)

            i += 1

    mtb_html.write(fin_div_general)
    mtb_html.write(footer)
    mtb_html.write(fin_body)
    mtb_html.write(fin_html)