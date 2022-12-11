from presentation.variablesHtml import *


def generarIndexHtml():
    # Aqui ejecutamos el codigo que nos crea/sobre escribe "index.html" en el directorio "docs" y le ponemos la siguiente estructura HTML:
    index_html = open("../monbike/docs/index.html", "w", encoding="utf-8")

    # HEAD del HTML
    index_html.write(head)

    # BODY del HTMl
    index_html.write(body)
    
    # HEADER del HTML
    index_html.write(header)

    index_html.write(index)

    index_html.write(footer)
    index_html.write(fin_body)
    index_html.write(fin_html)


