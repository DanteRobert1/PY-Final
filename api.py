from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
import os
import pandas as pd
import plotly.express as px

app = FastAPI()

static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Plantillas
templates = Jinja2Templates(directory="templates")

# Página principal con el menú
@app.get("/")
async def menu(request: Request):
    return templates.TemplateResponse("Problema.html", {"request": request})

@app.get("/Info")
async def menu(request: Request):
    return templates.TemplateResponse("Informacion.html", {"request": request})

@app.get("/Dat")
async def menu(request: Request):
    return templates.TemplateResponse("Datos.html", {"request": request})

@app.get("/Men")
async def menu(request: Request):
    return templates.TemplateResponse("Menu.html", {"request": request})


# Ruta para la gráfica 1
@app.get("/grafica1")
async def grafica1(request: Request):
    return templates.TemplateResponse("grafica1.html", {"request": request})

# Ruta para la gráfica 2
@app.get("/grafica2")
async def grafica2(request: Request):
    return templates.TemplateResponse("grafica2.html", {"request": request})

# Ruta para la gráfica 3
@app.get("/grafica3", response_class=HTMLResponse)
async def grafica3(request: Request):
    # Leer los datos desde GitHub
    url = "https://raw.githubusercontent.com/DanteRobert1/Optativa_Liz_Uaa/main/vgsales.csv"
    df = pd.read_csv(url)

    # Crear una nueva columna para las ventas regionales
    df['Regional_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales']

    # Generar la gráfica
    fig = px.scatter(
        df,
        x='Regional_Sales',  # Ventas combinadas de las regiones
        y='Global_Sales',    # Ventas globales
        color='Genre',       # Colorear por género
        size='Regional_Sales',  # Tamaño según la suma de las ventas 
        hover_name='Name',      
        title='Dispersión de ventas de videojuegos con las Regiones Combinadas'
    )

    # Convertir la gráfica a HTML
    graph_html = fig.to_html(full_html=False)

    # Renderizar el template
    return templates.TemplateResponse("grafica3.html", {"request": request, "graph_html": graph_html})

# Ruta para la gráfica 4
@app.get("/grafica4", response_class=HTMLResponse)
async def grafica4(request: Request):
    # Leer los datos desde GitHub
    url = "https://raw.githubusercontent.com/DanteRobert1/Optativa_Liz_Uaa/main/vgsales.csv"
    df = pd.read_csv(url)

    # Generar la gráfica
    fig = px.pie(df, names='Genre',  #Grafico de Pastel sobre los Generos
             values='Global_Sales', #Mostrara la cantidad de salario global de cada genero
             title='Distribución de Ventas Globales por Género de Videojuegos') 

    # Convertir la gráfica a HTML
    graph_html = fig.to_html(full_html=False)

    # Renderizar el template
    return templates.TemplateResponse("grafica4.html", {"request": request, "graph_html": graph_html})
# Ruta para la gráfica 5
@app.get("/grafica5")
async def grafica5(request: Request):
    return templates.TemplateResponse("grafica5.html", {"request": request})

@app.get("/Recomendaciones")
async def grafica5(request: Request):
    return templates.TemplateResponse("Recomendaciones.html", {"request": request})

# Página principal con el menú
@app.get("/")
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request": request})