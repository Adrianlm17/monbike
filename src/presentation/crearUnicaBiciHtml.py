# Importamos la funcion que contiene todas las bicis
from presentation.importJson import importarDatos

# Importamos todas las variables HTML
from presentation.variablesHtml import *



# Agregamos a la variable bicis la funcion "importarDatos"
bicis = importarDatos()



def generarUnicaBiciHtml():
    # Creo un bucle el cual nos escribe todas las bicis individualmente con una descripción y un boton de alquiler
    i = 0
    for bici in bicis:

        biciUnica_Html = open("../monbike/docs/"+ bicis[i]["_id"] +".html", "w", encoding="utf-8")
        
        # HEAD del HTML
        biciUnica_Html.write(head)
        
        # BODY del HTMl
        biciUnica_Html.write(body)
        
        # HEADER del HTML
        biciUnica_Html.write(header)
    
        biciUnica_Html.write("    <h1 class='titulo_unica_bici'>"+ bicis[i]["nombre"] +"</h1>\n")

        biciUnica_Html.write(dev_unicaBici)
        biciUnica_Html.write("      <img src='"+ bicis[i]["img"] +"' class='img_unica_bici' alt='bici individual alquiler'></img>\n")
        
        biciUnica_Html.write(p_unicaBici)
        
        # Agregamos variables segun el descuento de los dias de alquiler
        descuento5dias = int(bicis[i]["precio"]) - 2
        descuento10dias = int(bicis[i]["precio"]) - 3
        descuento15dias = int(bicis[i]["precio"]) - 4
        descuento30dias = int(bicis[i]["precio"]) - 6

        biciUnica_Html.write(f'''        Esta bicicleta'''+ bicis[i]["tipo de bici"]+ f''', cumple con las siguientes características:<br>
        <br>
        Material: Fabricada con un material de '''+ bicis[i]["material"]+ f'''. <br>
        <br>
        Marca: esta bicicleta cuenta con '''+ bicis[i]["marca de bici"]+ f'''!<br>
        <br>
        Peso: actualmente tenemos disponibles las tallas "'''+ bicis[i]["talla"]+ f'''" con un peso total de "'''+ bicis[i]["peso"]+ f'''".<br>
        <br>
        Freno: esta bicicleta cuenta con un '''+ bicis[i]["tipo de frenos"]+ f'''. <br>
        <br>
        Seguro: actualmente esta bicicleta Si / No tiene seguro. <br>
        <br>
        Precio por día<br>
        1 Día - '''+ bicis[i]["precio"] + f'''€<br>
        5 Días - '''+ str(descuento10dias) + f'''€<br>
        10 Días - '''+ str(descuento15dias) + f'''€<br>
        15 Días - '''+ str(descuento30dias) + f'''€<br>
        30 Días - '''+ str(descuento5dias) + f'''€<br>

        <br><br><br>

        No esperes más y alquila la bicicleta, solo nos quedan '''+ bicis[i]["stock"]+ f''' en '''+ bicis[i]["ubicación"]+ f'''!!!<br>
        Casco, guantes, bici y MONBIKE!!!<br>\n''')

        biciUnica_Html.write(p_unicaBici_fin)
        biciUnica_Html.write(dev_unicaBici_fin)
        biciUnica_Html.write(a_unicaBici)  
        biciUnica_Html.write(br_unicaBici) 

        biciUnica_Html.write(footer)
        biciUnica_Html.write(fin_body)
        biciUnica_Html.write(fin_html)

        i += 1