# Importamos la libreria JSON
import json
from variablesCss import css

def generarArchivoCss():
    general_html = open("../monbike/docs/style.css", "w", encoding="utf-8")
    
    # Escribir CSS
    general_html.write(css)
    
    general_html.close

generarArchivoCss()