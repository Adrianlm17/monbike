# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()


# Creamos una funcion que escribe todas las bicis del tipo de bici indicada
def UbicacionBicis(tipo):
    ubicacionBici_Html = open("../monbike/docs/" + tipo +".html", "a", encoding="utf-8")
    
    # HEAD del HTML
    ubicacionBici_Html.write(head)
    
    # BODY del HTMl
    ubicacionBici_Html.write(body)
    
    # HEADER del HTML
    ubicacionBici_Html.write(header)

    ubicacionBici_Html.write('    <h1 class="titulo_general"> Estas son todas las bicis que se encuentran en '+ tipo +' actualmente:</h1>\n')
    ubicacionBici_Html.write(div_global)
    

    # Creo un bucle el cual nos escribe todas las bicis que se encuentran en la ubicación indicada con el precio y un boton de alquiler
    i = 0

    for bici in bicis:
        if tipo in bici['ubicación']:
            ubicacionBici_Html.write(general_unica_bici)
            ubicacionBici_Html.write("        <img src='"+ bicis[i]["img"] +"' class='img_varias_bicis'>\n")
            ubicacionBici_Html.write("        <h2>"+ bicis[i]["nombre"] +"</h2>\n")

            # Agregamos 2 variables seun descuento segun los dias de alquiler
            descuentoGrande = int(bicis[i]["precio"]) - 2
            descuentoPequeño = int(bicis[i]["precio"]) - 1

            # Escribe el precio con su respectivo descuento en HTML
            ubicacionBici_Html.write('        <p>\n          1 Día   - ' + bicis[i]["precio"] + '€ <br>\n          5 Días  - ' + str(descuentoGrande) + '€ <br>\n          10 Días  - ' + str(descuentoPequeño) + '€ <br>\n          15 Días - ' + str(descuentoPequeño) + '€ <br>\n          30 Días - ' + str(descuentoGrande) + '€\n        </p>\n')
            
            ubicacionBici_Html.write(br_global)
            ubicacionBici_Html.write("        <a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")
            ubicacionBici_Html.write(fin_div)

        i += 1

    ubicacionBici_Html.write(fin_div_general)
    ubicacionBici_Html.write(footer)
    ubicacionBici_Html.write(fin_body)
    ubicacionBici_Html.write(fin_html)





def generarUbicacionesBici():

    # Generamos la pagina para las bicis con ubicacion Palma:
    UbicacionBicis("Palma")

    # Generamos la pagina para las bicis con ubicacion Inca:
    UbicacionBicis("Inca")

    # Generamos la pagina para las bicis con ubicacion Alcúdia:
    UbicacionBicis("Alcúdia")
    
    # Generamos la pagina para las bicis con ubicacion Manacor:
    UbicacionBicis("Manacor")

    # Generamos la pagina para las bicis con ubicacion Artá:
    UbicacionBicis("Artá")

    # Generamos la pagina para las bicis con ubicacion Pollensa:
    UbicacionBicis("Pollensa")

    # Generamos la pagina para las bicis con ubicacion Felanix:
    UbicacionBicis("Felanix")

    # Generamos la pagina para las bicis con ubicacion Soller:
    UbicacionBicis("Soller")

    # Generamos la pagina para las bicis con ubicacion Marratxi:
    UbicacionBicis("Marratxi")