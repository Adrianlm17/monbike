# Importamos webbrowser
import webbrowser

# Importamos OS
import os

# Importamos TYPER
import typer

from rich.progress import Progress, SpinnerColumn, TextColumn
from colorama import Cursor, Fore



app = typer.Typer(help="Bienvenid@ a MONBIKE!!")



@app.command()
def generarmonbike():
    '''
    Ejecuta el archivo main del SRC que genera el entorno MonBike
    '''
    with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    transient=True,
    )as progress:
        progress.add_task(description='[green]Creando WEB', total=100)
        os.environ["PYTHONPATH"]
        import main
    print(Fore.GREEN + "WEB CREADA")
    print(Fore.WHITE)
    



@app.command()
def insertbici():
    '''
    Insertar una nueva bicicleta
    '''
    os.environ["PYTHONPATH"]
    import database.insertNuevaBici
    print(Fore.GREEN + "BICI CREADA!")
    print(Fore.WHITE)



@app.command()
def eliminarbici():
    '''
    Eliminar una bicicleta de la base de datos
    '''
    os.environ["PYTHONPATH"]
    import database.eliminarBici
    print(Fore.GREEN + "BICI ELIMINADA!")
    print(Fore.WHITE)



@app.command()
def modificarbici():
    '''
    Modificar una bicicleta de la base de datos
    '''
    os.environ["PYTHONPATH"]
    import database.modificarBici
    print(Fore.GREEN + "BICI MODIFICADA!")
    print(Fore.WHITE)



@app.command()
def verbicicletas():
    '''
    Visualizar todas o una bicicleta/s
    '''
    os.environ["PYTHONPATH"]
    import database.verBici



@app.command()
def verweb():
    '''
    Visualizar la pagina web de MonBike desde GitHub Pages
    '''
    webbrowser.open_new_tab('https://adrianlm17.github.io/monbike/')


if __name__ == "__main__":
    app()
