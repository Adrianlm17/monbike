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
            <li><a href="eléctrica.html">Eléctrica</a></li>
            <li><a href="carretera.html">Carretera</a></li>
            <li><a href="city.html">City</a></li>
          </ul>
        </li>
        <li><a>Marcas</a>
          <ul>
            <li><a href="VAN RYSEL.html">VAN RYSEL</a></li>
            <li><a href="TRIBAN.html">TRIBAN</a></li>
            <li><a href="Deporvillage.html">Deporvillage</a></li>
            <li><a href="Focus.html">Focus</a></li>
            <li><a href="Motion.html">Motion</a></li>
            <li><a href="NCM.html">NCM</a></li>
            <li><a href="Riverside.html">Riverside</a></li>
            <li><a href="Rockrider.html">Rockrider</a></li>
            <li><a href="Windee.html">Windee</a></li>
            <li><a href="Elops.html">Elops</a></li>
            <li><a href="SHIMANO.html">SHIMANO</a></li>
          </ul>
        </li>
        <li><a>Ubicación</a>
          <ul>
            <li><a href="Palma.html">Palma</a></li>
            <li><a href="Inca.html">Inca</a></li>
            <li><a href="Alcúdia.html">Alcúdia</a></li>
            <li><a href="Manacor.html">Manacor</a></li>
            <li><a href="Artá.html">Artá</a></li>
            <li><a href="Pollensa.html">Pollensa</a></li>
            <li><a href="Felanix.html">Felanix</a></li>
            <li><a href="Soller.html">Soller</a></li>
            <li><a href="Marratxi.html">Marratxi</a></li>
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

# Variables para la pagina index.html

index = f'''    <h2 class="sub-titulo-monbike">
      Alquiler de Bicicletas Eléctricas, de Paseo, de Montaña y de Carretera al mejor precio!!
    </h2>

    <br><br><br>

    <table class="tabla_general_bicis">
      <tr>
        <td class="tabla_general_bicis_1">
          <h2>BICICLETAS</h2>
          <br>
          <p>
            Ahora también puedes ver las bicis que tenemos disponibles para ti!!!
          </p>
        </td>
        <td class="img_tabla_general">
          <a href="general.html" alt="Todas las bicis" class="button_general_bicis">Ver bicis</a>
        </td>
      </tr>
    </table>

    <br>

    <h3 class="elige_monbike"> ¿Por qué MonBike?</h3>

    <br>
        
    <div class="porque_monbike">
        <h4>Gran variedad</h4>

        <p>
            ¡Te garantizamos una gran variedad de <b>alquiler de bicicletas en Mallorca!!</b><br>
            Disponemos de bicicletas de bicis de paseo, eléctricas, de montaña y bicicletas de carretera.
        </p>

        <br>

        <h4>Atención al cliente</h4>

        <p>
            Te ofrecemos asistencia en cualquier punto de Mallorca los 365 días al año.<br>
            Tus vacaciones ciclistas deben ser para descansar y disfrutar del cicloturismo,<br>
            solo elige la bici y nosotros nos encargamos del resto
        </p>

        <br>

        <h4>Nos gusta el ciclismo</h4>

        <p>
            Además de disponer de las mejores bicicletas para su experiencia, contamos con un gran equipo de expertos en el sector, <br>
            los cuales podrás llamar en cualquier momento y ellos te resolverán el problema, a demás, <br>
            también te podrán recomendar rutas que nunca olvidaras!!
        </p>

    </div>

    <br><br>

    <!-- Agreo un pequeño video referente al ciclismo -->
    <div style="text-align:center;">
        <iframe src="https://www.youtube.com/embed/3W3X8vfssYo" width="650" height="350"></iframe>
    </div>
'''

# Variables para la pagina donde aparece todas las bicis

div_global = '    <div class="general_bicis">\n'
general_unica_bici = '      <div class="general_una_bici">\n'
fin_div = '      </div>\n'
fin_div_general = '    </div>\n'
br_global = "        <br>\n"
fin_html = "</html>"

# Variables para la pagina contacto.html

contacto = f'''    <div class="formulario_bici">
            
    <br>
    
    <h2 class="contactanos">Contáctanos</h2>
    
    <br>
    
    <form method="get" action="index.html">
        
      <br>
      <label>Nombre: </label><input type="text" name="usuario" class="formulario_dentro" required> <br>
      <br>
      <label>Apellidos: </label><input type="text" name="apellidos" class="formulario_dentro" required> <br>
      <br>
      <label>EMAIL: </label><input type="email" name="email" class="formulario_dentro" required> <br>
      <br>
      <label>Telefono: </label><input type="tel" name="telf" class="formulario_dentro" required> <br>
      <br>
      <label>Dirección: </label><input type="text" name="dirreción" placeholder="Calle , numero" class="formulario_dentro" required> <br>
      <br>
      <label>Fecha: </label><input type="date" name="trip-start" value="2022-12-13" class="formulario_dentro" required> <br>
      <br><br>
      <label>Comentario</label><br>
      <br>
      <textarea class="formulario_dentro" name="comentario" rows="5" cols="30" required>Escribe tu comentario </textarea><br>
      
      <br><br><br>

      <input type="submit" value="Enviar" class="boton"> <br>
      
      <br>

      <input type="reset" value="Restablecer formulario" class="boton"> <br>
      <br>
    </form>
    
</div>


'''