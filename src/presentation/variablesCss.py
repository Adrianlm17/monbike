# CSS metida en una variable Python 
css = """
/**** CSS para Ordenadores  de ANCHO 1366 Minimo y Altura 768 Minimo *****/

/************************* MENU de arriba ********************************/


* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font: oblique bold 15px cursive;
	
}

/* Oculto el boton de navegador de móvil para ordenadores */
.boton_navegador_img, .menu_input {
	display: none;
}

.menu-header { 
	background-color: rgb(165, 247, 175);
	height: 75px;
	width: 100%;
	display: flex;
	justify-content: space-between;
	align-items: center;
	border-bottom: 1px solid white;
	box-shadow: 10px 0 25px black;
	position: fixed;
	
}

.menu-principal {
	list-style: none;
	display: flex;
}


.menu-principal > li > a {
	display: block;
	padding: 25px 25px;
	color: rgb(0, 0, 0);
	text-decoration: none;
	font: oblique bold 20px cursive;
}

.menu-principal > li:hover {
	background-color: rgb(15, 92, 8);
	border-radius: 10px;
}

.menu-principal li ul {
	position: absolute;
	display: none;
	background-color: rgb(165, 247, 175);
	list-style: none;
	border-bottom: 2px solid white;
	box-shadow: 8 px 8px 10px black;
	border-radius: 10px;
}

.menu-principal li ul li a{
	text-decoration: none;
	padding: 10px 15px;
	color: rgb(0, 0, 0);
	display: block;
	font: oblique bold 15px cursive;
}

.menu-principal li:hover > ul {
	display: block;
}

.menu-principal li ul > li:hover {
	background-color: rgb(15, 92, 8);
	border-radius: 10px;
}

/* Logo MonBike */
.logo {
	display: flex;
	height: 100%;
}

/**********************************  BODY  ***************************************/

body {
	margin: 0px;
	background-color: beige;
}

.img_index_1 {
	width:100%;
}

/* Damos color y estilo de letra al subtitulo y lo centramos */ 
.sub-titulo-monbike {
	text-align: center;
	font: oblique bold 25px cursive;
	color: rgb(20, 151, 53);
}

.tabla_general_bicis {
	margin: 0 auto;
	text-align: left;
	background-image: url("img/general_bicis.png");
	width: 50%;
	font-family: sans-serif;
	border-radius: 15px;
}

.tabla_general_bicis_1 {
	background-color: rgb(130, 130, 239);
	width: 50%;
	padding: 3% 5% 3%;
	color: rgb(255, 254, 254);
	border-radius: 15px;
}

.button_general_bicis {
	background-color:#76a2fb;
	border-radius:1em;
	color:rgb(0, 0, 0);
	text-transform:uppercase;
	padding:3% 5%;
	margin-left: 35%;
}

.elige_monbike {
	text-align: center;
	font: oblique bold 40px cursive;
	color: rgb(20, 151, 53);
}

.porque_monbike {
	margin: 0 auto;
	text-align: center;
	color: rgb(53, 158, 53);
	font: oblique bold 19px cursive;
}

.porque_monbike h4 {
	font: oblique bold 20px cursive;
	color: rgb(48, 121, 48);
	text-align: center;
}

.titulo_general {
	font: oblique bold 40px cursive;
	color: rgb(48, 121, 48);
	text-align: center;
}

.general_bicis {
	display: grid;
	grid-template-columns: repeat(5, 1fr);
	
}

.general_una_bici{
	padding-left: 5%;
	padding-top: 10%;
	text-align: center;
	color: rgb(48, 121, 48);
}

.general_una_bici p {
	font: oblique bold 13px cursive;
	color: rgb(79, 172, 79);
}

.general_una_bici a{
	text-decoration: none;
	background-color:#76a2fb;
	border-radius:1em;
	color:rgb(0, 0, 0);
	text-transform:uppercase;
	padding:3% 5%;
}

.img_varias_bicis {
	width: 85%;
	height: 50%;
	border-radius: 10%;
}

/******************************** FOOTER **********************************/

#main-footer {
	background: rgb(165, 247, 175);
	color: rgb(6, 53, 13);
	text-align: center;
	padding: 15px;
	
}


/* RESPONSIVE PARA MOVILES DE: ANCHO 415 Maximo y Altura 753 Maximo */
@media screen and ((max-device-width: 415px) and (max-device-height: 753px)){

	/************************ NAVEGADOR PARA MÓVIL **********************/
	
	/* NAVEGADOR */
	
	.menu-header { 
		background-color: rgb(165, 247, 175);
		height: 8%;
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
		border-bottom: 3px solid white;
		box-shadow: 10px 0 25px black;
		position: fixed;
		
	}
	
	.logo {
		display: flex;
		height: 90%;
	}

	.boton_navegador_img {
		display: block;
		cursor: pointer;
		width: 120px;
		height: 98px;
	}

	.menu-principal {
		display: none;
	}
	
	.menu_input:checked + .menu-principal{
		position: fixed;
		top: 125px;
		display: flex;
		justify-content: space-evenly;
		align-items: center;
		right: 2%;
		border-radius: 15px;
		background-color: rgb(124, 202, 157);
	}
	
	.menu-principal > li > a {
		display: block;
		padding: 25px 25px;
		color: rgb(0, 0, 0);
		text-decoration: none;
		font: oblique bold 25px cursive;
		text-align: center;
	}
	
	.menu-principal > li:hover {
		background-color: rgb(65, 116, 86);
		border-radius: 10px;
	}
	
	.menu-principal li ul {
		position: absolute;
		display: none;
		background-color: rgb(124, 202, 157);
		list-style: none;
		border-bottom: 2px solid white;
		box-shadow: 8 px 8px 10px black;
		border-radius: 10px;
	}
	
	.menu-principal li ul li a{
		text-decoration: none;
		padding: 10px 15px;
		color: rgb(0, 0, 0);
		display: block;
		font: oblique bold 25px cursive;
	}
	
	.menu-principal li:hover > ul {
		display: block;
	}
	
	.menu-principal li ul > li:hover {
		background-color: rgb(65, 116, 86);
		border-radius: 10px;
	}

	/*************************  BODY  MÓVIL *****************************/

    body {
        background-color: rgb(240, 232, 212);
    }

	/* IMAGEN MONBIKE */
	.img_index_1 {
		width:100%;
		padding-top: 10%;
	}

	/* TABLA PARA LA GENERAL BICIS*/
    .tabla_general_bicis {
        margin: 0 auto;
        background-image: url("img/general_bicis.png");
        width: 90%;
        border-radius: 15px;
    }
    
    .tabla_general_bicis_1 {
        background-color: rgb(130, 130, 239);
        width: 50%;
        padding: 5% 3% 6%;
        color: rgb(255, 254, 254);
        border-radius: 15px;
    }

    .tabla_general_bicis_1 h2 {
        font-size: 200%
    }

    .tabla_general_bicis_1 p {
        font-size: 200%
    }
    
    .button_general_bicis {
    
        background-color:#76a2fb;
        border-radius:1em;
        color:rgb(0, 0, 0);
        text-transform:uppercase;
        padding:6% 8%;
        margin-left: 24%;
        font-size: 160%
    }

	.titulo_general {
		font: oblique bold 25px cursive;
		color: rgb(48, 121, 48);
		text-align: center;
	}
	
	.general_bicis {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		
	}
	
	.general_una_bici{
		padding-left: 3%;
		padding-top: 10%;
		text-align: center;
		color: rgb(48, 121, 48);
	}
	
	.general_una_bici p {
		font: oblique bold 10px cursive;
		color: rgb(79, 172, 79);
	}

	.general_una_bici a{
		text-decoration: none;
		background-color:#76a2fb;
		border-radius:25%;
		color:rgb(0, 0, 0);
		text-transform:uppercase;
		padding:3% 5%;
	}
	
	.img_varias_bicis {
		width: 85%;
		height: 50%;
		border-radius: 10%;
	}
}

"""
