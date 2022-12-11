# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()


# Creamos una funcion que escribe todas las bicis del tipo de bici indicada
def TiposBicis(tipo):
    tipoBici_Html = open("../monbike/docs/" + tipo +".html", "a", encoding="utf-8")
    
    # HEAD del HTML
    tipoBici_Html.write(head)
    
    # BODY del HTMl
    tipoBici_Html.write(body)
    
    # HEADER del HTML
    tipoBici_Html.write(header)

    tipoBici_Html.write('    <h1 class="titulo_general"> Estas son todas las bicis  del tipo '+ tipo +' que tenemos actualmente:</h1>\n')
    tipoBici_Html.write(div_global)
    

    # Creo un bucle el cual nos escribe todas las bicis del tipo indicado con el precio y un boton de alquiler
    i = 0

    for bici in bicis:
        if bici['tipo de bici'] == tipo:
            tipoBici_Html.write(general_unica_bici)
            tipoBici_Html.write("        <img src='"+ bicis[i]["img"] +"' class='img_varias_bicis' alt='imagen bici por tipo'>\n")
            tipoBici_Html.write("        <h2>"+ bicis[i]["nombre"] +"</h2>\n")

            # Agregamos variables segun el descuento de los dias de alquiler
            descuento5dias = int(bicis[i]["precio"]) - 2
            descuento10dias = int(bicis[i]["precio"]) - 3
            descuento15dias = int(bicis[i]["precio"]) - 4
            descuento30dias = int(bicis[i]["precio"]) - 6

            # Escribe el precio con su respectivo descuento en HTML
            tipoBici_Html.write('        <p>\n          1 Día   - ' + bicis[i]["precio"] + '€ <br>\n          5 Días  - ' + str(descuento5dias) + '€ <br>\n          10 Días  - ' + str(descuento10dias) + '€ <br>\n          15 Días - ' + str(descuento15dias) + '€ <br>\n          30 Días - ' + str(descuento30dias) + '€\n        </p>\n')
            
            tipoBici_Html.write(br_global)
            tipoBici_Html.write("        <a href='"+ bicis[i]["_id"] +".html'>ALQUILAR</a>\n")
            tipoBici_Html.write(fin_div)

        i += 1

    tipoBici_Html.write(fin_div_general)
    tipoBici_Html.write(footer)
    tipoBici_Html.write(fin_body)
    tipoBici_Html.write(fin_html)





def generarTipoBici():

    # Generamos la pagina para las bicis de carretera:
    TiposBicis("carretera")

    # Generamos la pagina para las bicis de MTB:
    TiposBicis("MTB")

    # Generamos la pagina para las bicis de eléctrica:
    TiposBicis("eléctrica")
    
    # Generamos la pagina para las bicis de city:
    TiposBicis("city")