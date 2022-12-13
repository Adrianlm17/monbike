# MONBIKE




## **Índice de contenido**

- [**MonBike**](#monbike)
- [**Introducción**](#introducción)
- [**Manual**](#manual)
    - [**Pre-requisitos**](#pre-requisitos)
    - [**Instalación**](#instalación)
    - [**Uso**](#uso)
- [**Descripción Técnica**](#descripción-técnica)
    - [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
    - [**Tecnologías y Herramientas Usadas**](#tecnologías-y-herramientas-usadas)
    - [**Diagrama uso MonBike**](#diagrama-uso-monbike)
    - [**Diagrama de componentes**](#diagrama-de-componentes)
    - [**Diagrama base de datos**](#diagrama-base-de-datos)
- [**Metodología**](#metodología)
- [**Pruebas**](#pruebas)
    - [**Coverage**](#coverage)
- [**Clockfiy**](#clockfiy)
    - [**Diagrama Tiempo**](#diagrama-tiempo)
    - [**Justificación Tiempo**](#justificación-tiempo)
- [**Conclusiones**](#conclusiones)
    - [**Mejoras**](#mejoras)
    - [**Dificultades**](#dificultades)







## MonBike

![MonBike](https://i.ibb.co/0YQqkTH/MonBike.png)

**MonBike** surge de la idea de crear una plataforma de alquiler de bicis. A raíz de ello crece con el fin de generar una web fácil y sencilla al usuario con un único fin que ambas partes queden satisfechas!

Para poder llevar a cabo este trabajo he usado Mongo Atlas (un servicio que nos ofrece [**MongoDB**](https://www.mongodb.com)).
Después he utilizado para el lenguaje de programación [**Python**](https://www.python.org) con una version "3.11".
Y por último, pero no menos importante, he usado [**GitHub Pages**](https://pages.github.com/) el cual me permite producir mi sitio web estático.


![img_resumen](https://i.ibb.co/cbq2hkX/general-Monbike.png)



## Introducción

Es el mes de abril y acabas de aterrizar en el departamento de desarrollo de tu flamante nueva empresa de Dual.
Ahora toca trabajar y en tu empresa han decidido que bas a **desarrollar un mínimo producto viable**, una idea de negocio a la que llevan dando vueltas tiempo y procrastinando, aplicando estos conocimientos, y así que les enseñes lo que tienes sin romper nada (además de ganarte tu primer salario). 

El excesivo número de coches en las carreteras de Baleares se ha convertido en un problema, el Gobierno de las Islas Baleares está barajando diversas medidas.
La idea es crear una plataforma donde la gente local y los/as turistas puedan chequear la disponibilidad de bicicletas de alquiler en un área. Se trata de construir un agregador donde las compañías volcasen su flota de bicicletas. 

Tu empresa quiere poner en marcha un site que muestre información sobre un modelo concreto de bicicleta, dónde se encuentra disponible en alquiler y realizar comparativas entre las características de diferentes modelos. Cada bicicleta se encuentra en stock en una empresa de alquiler distinta. La idea es vender este producto como un agregador de las bicicletas disponibles en los negocios de alquiler de les Illes Balears.



**REQUISITOS**


Tu tutor/a de empresa quiere:
- Desarrolla una aplicación **Python** para extraer los datos de **MongoAtlas**. Se hace necesario diseñar una especificación del esquema de los documentos **JSON**.
- Esos documentos **JSON** tendrás que transformarlos, también con una aplicación **Python**, en ficheros **HTML** (los estilos **CSS** corren también por tu cuenta). 
- Luego, has de situar estos ficheros en una estructura de directorios que establece el generador de sitios estáticos de **GitHub Pages**, también mediante una aplicación **Python** que construyas.
- Cuando subas este código a tu repo en github, **GitHub Pages** servirá las páginas **HTML** a modo de sitio web estático.
- Tendrás que customizar los estilos **CSS** para dar la presentación adecuada a los datos.
- Desarrolla una **API** de **MongoAtlas** que permita hacer un **CRUD**.



## Manual


### Pre-requisitos

```
- Git
- Python3
- pip3
- Requests
- Coverage
- API-KEY
```



### Instalación

Para poder usar el programa, se recomienda usar [**venv**](https://docs.python.org/es/3.8/library/venv.html) para tener instaladas todas las dependencias usadas en el programa.



### Uso

MonBike está pensado para facilitar el trabajo tanto al usuario como al programador/trabajador, así que con solo ejecutar el comando **python3 .\typer\MonBike.py --help** nos mostrara todas las opciones que nos permite realiar MonBike.

```
python3 .\typer\MonBike.py --help
```

![Typer MonBike](https://i.ibb.co/BZWmBtP/typer-Mon-Bike.png)


## Descripción Técnica


### Arquitectura de la aplicación

![arquitecturaMonBike](https://i.ibb.co/LCRGfF2/arquitectura-Mon-Bike.png)

- **Presentación**

    - **monbike.py** programa principal.

- **Servicios**

    - **ejecutarTrabajo** encargado de generar todo el entorno con las páginas webs.
    - **verMonBike** encargado de visualizar en *Google Chrome* la página web.

- **Base de datos**

    - **insertNuevaBici** encargado de insertar una nueva bici.
    - **eliminarBici** encargado de eliminar una bici.
    - **modificarBici** encargado de modificar el contenido de una bici.
    - **verbici** encargado de mostrar las bicics que le indiques.

- **Parte Externa**

    - **GitHub Pages** programa externo que nos permite alojar nuestra web estática



### Tecnologías y Herramientas Usadas

- **[Python](https://docs.python.org/3/)**
    - **[OS](https://docs.python.org/es/3.10/library/os.html)** es una librería de Python que nos permite acceder a funcionalidades dependientes del Sistema Operativo.
    - **[REQUESTS](https://requests.readthedocs.io/en/latest/)** es una librería Python que facilita enormemente el trabajo con peticiones HTTP.
    - **[SHUTIL](https://docs.python.org/es/3/library/shutil.html)** es un módulo que ofrece varias operaciones de alto nivel en archivos y colecciones de archivos.
    - **[webbrowser](https://docs.python.org/es/3/library/webbrowser.html)** es un módulo que nos permite mostrar documentos basados en web a los usuarios.
    - **[Pytest](https://docs.pytest.org/en/7.2.x/)** es un marco de trabajo que permite realizar pruebas unitarias para un software en Python.
    - **[Coverage](https://coverage.readthedocs.io/en/6.5.0/)** es una herramienta que tiene la capacidad de realizar la generación de los informes por línea de comando, o bien, la generación de los informes en formato html.
    - **[JSON](https://docs.python.org/3/library/json.html)** es una librería la cual nos permite principalmente parsear archivos o strings JSON en un diccionario o en una lista en Python y viceversa.

- **[MongoDB](https://www.mongodb.com/docs/)**
    - **[MongoAtlas](https://www.mongodb.com/es/cloud/atlas/efficiency)** es un servicio de "Cloud Database", que permite crear y administrar tu BBDD Mongo desde cualquier lugar del mundo, a través de su plataforma.
    - **[MongoDB API](https://www.mongodb.com/docs/atlas/api/)** es una herramienta la cual nos permite interactuar con MongoAtlas usando una API.

- **[HTML5](https://www.w3schools.com/html/html_intro.asp)** y **[CSS3](https://www.w3schools.com/css/css_intro.asp)** permite crear y dar formato a las páginas webs.

- **[Git](https://git-scm.com/docs)** sistema de control de versiones distribuido.

- **[Markdown](https://markdown.es/)** es un lenguaje de marcado ligero.

- **[GitHub Pages](https://pages.github.com/)** es un servicio de alojamiento de sitios estáticos que toma archivos HTML, CSS y JavaScript directamente de un repositorio en GitHub

- **[Typer](https://typer.tiangolo.com/)** es una librería para crear aplicaciones CLI basada en sugerencias de tipo de Python 3.6+.




### Diagrama uso MonBike

![Diagrama uso MonBike](https://i.ibb.co/5TDJrm8/diagrama-Uso-Mon-Bike.png)




### Diagrama de componentes

![Diagrama de Componentes](https://i.ibb.co/Ky77L2J/diagrama-Componentes.png)

Este diagrama de componentes se divide en 5 módulos:

- **Base de datos**
    - **Crear** añade nuevas bicis.
    - **Modificar** modifica bicis.
    - **Eliminar** elimina bicis.
    - **Conexión** sube las modificaciones realizadas o importa los datos de la base de datos.
    - **Importar datos** guarda los datos importados.

- **JSON**
    crea un archivo JSON con todo el contenido de la base de datos.

- **ENTORNO**
    elimina todo el contenido que ya exista en la carpeta docs y crea las carpetas y archivos necesarios.

- **HTML | CSS**
    - **INDEX** crea una página HTML de inicio.
    - **GLOBAL** genera diferentes páginas HTML como tipos de bici, ubicación...
    - **BICI** genera varias páginas HTML, una para cada bici.
    - **CONTACTO** genera una página HTML de contacto.

- **VER WEB**
    Nos permite visualizar la página web desde GitHub Pages




### Diagrama base de datos

![Diagrama Base de Datos](https://i.ibb.co/hsVHnSh/diagrama-Base-Datos.png)

Para hacerlo lo más simple posible, cree una única colección donde almacenaba los siguientes datos:

- **ID** de la bici (te lo otorga automáticamente)
- **Nombre** de la bici
- **Tipo de bici**
- **Empresa** que dispone de dicha bici
- **Precio** de alquiler de la bici
- **Ubicación** de la bici
- **Stock** que dispone de esa bici
- **Material** de la bici
- **Marca de bici**
- **Talla** de esa bici en concreto
- **Peso** de esa bici en concreto
- **Tipo de freno** que dispone
- **IMG** de la bici
- Si dispone de **Seguro**

Para que nos hagamos una idea, esto quedaría de la siguiente forma:

```
{
    "_id": "6384ff576b1b912573be835d",
    "nombre": "Bicicleta MTB Deporvillage GR900 29",
    "tipo de bici": "MTB",
    "precio": "20",
    "ubicación": "Palma, Inca, Manacor, Artá y Pollensa",
    "stock": "836",
    "material": "aluminio ",
    "marca de bici": "Deporvillage",
    "talla": "S",
    "peso": "13,15 kg",
    "tipo de frenos": "freno de disco",
    "img": "https://cdn.deporvillage.com/cdn-cgi/image/h=576,w=576,dpr=1,f=auto,q=75,fit=contain,background=white/product/dpv-c353202103-01_1001.jpg",
    "seguro": "No"
}
```




## Metodología

Para realizar este trabajo he utilizado una **metodología Espiral**, primero de todo cree un prototipo donde iba visualizando diferentes aspectos, después cuando ya comprendí el funcionamiento del producto y tenía ya generado unas cuantas ideas, pase a dividir el trabajo (tanto la parte de diseño como la lógica) en diferentes etapas.

En mi caso al no disponer de compañero, no pude implementar la **metodología Scrum** internamente, pero si la pude aplicar con el resto de compañeros donde iba obteniendo algún feedback.



## Pruebas

Para este trabajo se han implementado varias pruebas de tal forma que dependiendo el tipo de función hubiese un número o otro de test:
    
    * Un test que verificaba que en el archivo JSON había contenido
    * Dos test que verificaban si se había creado un archivo o no
    * Dos test que verificaban si se había creado una carpeta o no
    * Cuatro test que verificaban la estructura que tenía el archivo JSON
    * Dos test que verifican si la función verifica o no los archivos creados

Principalmente, se crearon alguno de estos casos test, aunque también se fueron implementando otros a medida que se iba realizando los códigos.

En caso de dudas o querer indagar, revise [pytest.ini](https://github.com/Adrianlm17/monbike/blob/main/pytest.ini) o la carpeta donde se encuentran los casos [test](https://github.com/Adrianlm17/monbike/blob/main/test/).



### Coverage

![Coverage MonBike](https://i.ibb.co/w4VxdGs/coverage-Mon-Bike.png)

Como bien podemos observar en la imagen, cuento con una cobertura del 61% dado que en los archivos que uso como barricada apenas tiene casos test.



## [Clockfiy](https://asana.com/es/apps/clockify)

### Diagrama Tiempo

Para poder saber el tiempo dedicado a este trabajo y un control del tiempo invertido en cada función, módulo,... Utilice la herramienta **Clockfiy**.
Asigne a cada trabajo unas etiquetas las cuales me permitían diferenciar el tiempo que dedicaba a cada módulo, función... Y de qué herramienta estaba haciendo uso principalmente:

- **Clockfy** para cuando realizaba ajustes o consultas.
- **CSS** para cuando dedicaba tiempo al lenguaje *CSS*.
- **DATABASE** para el tiempo dedicado a todo lo relacionado con la base de datos como MongoDB, Mongo Atlas o la API.
- **DOCUMENTACIÓN** para el tiempo dedicado a revisar, crear o buscar algún tipo de consulta o archivo.
- **GitHub** para el tiempo invertido en todo lo relacionado con Git, GitHub y GitHub Pages.
- **HTML** para cuando dedicaba tiempo en el lenguaje *HTML*.
- **MARKDOWN** para el tiempo invertido en el lenguaje *MARKDOWN*
- **PYTHON** para cuando dedicaba tiempo al lenguaje *PYTHON*

![Clockfiy MonBike](https://i.ibb.co/KFyh0K9/Clockfiy-Mon-Bike.png)

Para más información puedes entrar en el Clockify de *[MonBike](https://app.clockify.me/shared/6396539761b5bd72764ee867)* y comprobarlo!


![Tiempo invertido](https://i.ibb.co/f9Kg1RV/tiempo-invertido-Mon-Bike.png)

La predicción era de un total de **58 horas**, pero en mi caso al no contar con un compañero y no contar con algunos aspectos como configurar algunas herramientas, falta de documentación me quedo con un total de **73 h y 9 min**.



### Justificación Tiempo

Ahora que ya hemos visualizado el tiempo en un gráfico, podemos comprobar en que hemos invertido más tiempo o menos tiempo, pero principalmente donde más tiempo he dedicado, a este trabajo ha sido en HTML, CSS y Python dado que he requerido de mucho tiempo para crear plantillas para cada cosa o crear funciones o casos test.



## Conclusiones

En general, haber realizado este trabajo he podido aprender muchas cosas, desde herramientas que desconocía como GitHub Pages o Clockify, hasta implementar códigos o librerías que me han permitido ir más haya de donde nos pedian. También he podido aprender a base de errores, muchas otras cosas que me ayudaran a tener en cuenta para ahorrar tiempo hasta incluso dinero.

A pesar de haber empezado tarde y haber realizado un trabajo de parejas totalmente individual, estoy bastante satisfecho con los resultados obtenidos.



### Mejoras

* Implementar un sistema de notificación al Usuario cuando mande un formulario de contacto o alquile una bici.



### Dificultades

Como comente anteriormente, una de las principales dificultades que me encontré en algunos aspectos era realizar un trabajo de dos personas siendo una única persona, otra dificultad también fue el tiempo. Y referente a la parte más interna donde más encontré algunas dificultades fueron a la hora de realizar algunos casos test o situar cada objeto que quería en el lugar exacto de la página web dado que el CSS o el HTML no me lo permitían.
