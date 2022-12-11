# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()


# Creamos una funcion que escribe todas las marca de bici indicada
def MarcaBicis(tipo):
    marcaBici_Html = open("../monbike/docs/" + tipo +".html", "a", encoding="utf-8")
    
    # HEAD del HTML
    marcaBici_Html.write(head)
    
    # BODY del HTMl
    marcaBici_Html.write(body)
    
    # HEADER del HTML
    marcaBici_Html.write(header)

    marcaBici_Html.write('    <h1 class="titulo_general"> Estas son todas las bicis  de la marca '+ tipo +' que tenemos actualmente:</h1>\n')
    marcaBici_Html.write(div_global)
    

    # Creo un bucle el cual nos escribe todas las bicis del tipo indicado con el precio y un boton de alquiler
    i = 0

    for bici in bicis:
        if bici['marca de bici'] == tipo:
            marcaBici_Html.write(general_unica_bici)
            marcaBici_Html.write("        <img src='"+ bicis[i]["img"] +"' class='img_varias_bicis' alt='imagen bici por marca'>\n")
            marcaBici_Html.write("        <h2>"+ bicis[i]["nombre"] +"</h2>\n")

            # Agregamos variables segun el descuento de los dias de alquiler
            descuento5dias = int(bicis[i]["precio"]) - 2
            descuento10dias = int(bicis[i]["precio"]) - 3
            descuento15dias = int(bicis[i]["precio"]) - 4
            descuento30dias = int(bicis[i]["precio"]) - 6

            # Escribe el precio con su respectivo descuento en HTML
            marcaBici_Html.write('        <p>\n          1 Día   - ' + bicis[i]["precio"] + '€ <br>\n          5 Días  - ' + str(descuento5dias) + '€ <br>\n          10 Días  - ' + str(descuento10dias) + '€ <br>\n          15 Días - ' + str(descuento15dias) + '€ <br>\n          30 Días - ' + str(descuento30dias) + '€\n        </p>\n')
            
            marcaBici_Html.write(br_global)
            marcaBici_Html.write("        <a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")
            marcaBici_Html.write(fin_div)

        i += 1

    marcaBici_Html.write(fin_div_general)
    marcaBici_Html.write(footer)
    marcaBici_Html.write(fin_body)
    marcaBici_Html.write(fin_html)





def generarMarcaBici():

    # Generamos la pagina para las bicis de marca VAN RYSEL:
    MarcaBicis("VAN RYSEL")

    # Generamos la pagina para las bicis de marca TRIBAN:
    MarcaBicis("TRIBAN")

    # Generamos la pagina para las bicis de marca Deporvillage:
    MarcaBicis("Deporvillage")
    
    # Generamos la pagina para las bicis de marca Focus:
    MarcaBicis("Focus")

    # Generamos la pagina para las bicis de marca Motion:
    MarcaBicis("Motion")

    # Generamos la pagina para las bicis de marca :
    MarcaBicis("NCM")

    # Generamos la pagina para las bicis de marca Riverside:
    MarcaBicis("Riverside")

    # Generamos la pagina para las bicis de marca Rockrider:
    MarcaBicis("Rockrider")

    # Generamos la pagina para las bicis de marca Windee:
    MarcaBicis("Windee")

    # Generamos la pagina para las bicis de marca Elops:
    MarcaBicis("Elops")

    # Generamos la pagina para las bicis de marca SHIMANO:
    MarcaBicis("SHIMANO")