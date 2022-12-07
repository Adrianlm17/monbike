# Variables globales HTML en Python


head = f'''<!Doctype html>
<html LANG="es">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Web de alquiler de bicis MonBike">
    <meta name="author" content="Adrián López">
    <meta name="copyright" content="Adrián López">
    <meta name="generator" content="Monbike">
    <meta name="date" content="27/11/2020">
    <meta name="last-modified" content="04 de Diciembre de 2022">
    <meta name="keyword" content="Bicis, Alquilar bicis, Monbike, Mallorca bicis">
    <link rel="StyleSheet" href="style.css">
    
    <!-- LOGO MonBike-->
    <link rel="shortcut icon" href="https://i.ibb.co/LPH7YSV/icono-monbike.png">
    <!-- Titulo MonBike -->
    <title>MonBike</title>
  </head>\n''' 

header = f'''    <header class="menu-header">
      <img src="https://i.ibb.co/LPH7YSV/icono-monbike.png" class="logo" alt="Logo MonBike">

      <label for="menu" class="boton_navegador">
        <img src="https://i.ibb.co/6Wzb0yY/boton-navegador.png" class="boton_navegador_img" alt="Menu navegación para móvil">
      </label>

      <input type="checkbox" id="menu" class="menu_input">

      <!-- Creo un navegador con diferentes apartados y sub-apartados -->
      <ul class="menu-principal">
                
        <li><a href="index.html">Inicio</a></li>
        <li><a>Tipos</a>
          <ul class="sub_menu">
            <li><a href="mtb.html">MTB</a></li>
            <li><a href="electrica.html">Eléctrica</a></li>
            <li><a href="carretera.html">Carretera</a></li>
            <li><a href="paseo.html">Paseo</a></li>
          </ul>
        </li>
        <li><a>Marcas</a>
          <ul>
            <li><a href="vanrysel.html">VAN RYSEL</a></li>
            <li><a href="triban.html">TRIBAN</a></li>
            <li><a href="deporvillage.html">Deporvillage</a></li>
            <li><a href="focus.html">Focus</a></li>
            <li><a href="motion.html">Motion</a></li>
            <li><a href="ncm.html">NCM</a></li>
            <li><a href="riverside.html">Riverside</a></li>
            <li><a href="rockrider.html">Rockrider</a></li>
            <li><a href="windee.html">Windee</a></li>
            <li><a href="elops.html">Elops</a></li>
            <li><a href="shimano.html">SHIMANO</a></li>
          </ul>
        </li>
        <li><a>Ubicación</a>
          <ul>
            <li><a href="palma.html">Palma</a></li>
            <li><a href="inca.html">Inca</a></li>
            <li><a href="alcudia.html">Alcúdia</a></li>
            <li><a href="manacor.html">Manacor</a></li>
            <li><a href="arta.html">Artá</a></li>
            <li><a href="pollensa.html">Pollensa</a></li>
            <li><a href="felanix.html">Felanix</a></li>
            <li><a href="soller.html">Soller</a></li>
            <li><a href="marratxi.html">Marratxi</a></li>
          </ul>
        </li>
        <li><a href="contacto.html">Contacto</a></li>
      </ul>
    </header>

    <img src="https://i.ibb.co/Mpq0Y94/img-index-1.jpg" class="img_index_1" alt="Imagen Bicis con logo">\n
'''
footer = f'''    <footer id="main-footer">
      <p>&copy; 2022 por Adrián López</p>
    </footer>\n'''

body = "  <body>\n"
fin_body = "  </body>\n"


# Variables para la pagina donde aparece todas las bicis

div_global = '    <div class="general_bicis">\n'
general_unica_bici = '      <div class="general_una_bici">\n'
fin_div = '      </div>\n'
fin_div_general = '    </div>\n'
br_global = "        <br>\n"
fin_html = "</html>"