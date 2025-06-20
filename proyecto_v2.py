# importar librerias
import pandas as pd
import plotly.express as px
from Dash import Dash, html, dcc, Input, Output

# definir funciones
def load_data(file_path):
    try:
        data = pd.read_excel(file_path, header = 3)
        return data
    except Exception as e:
        print(f"Error al cargar la data de {file_path}: {e}")
        return None

# copiar ruta de los archivos
siniestros_path = 'C:/Users/User_001/Documents/PACD/proyecto/BBDD ONSV - SINIESTROS 2021-2023.xlsx' # modificar según sea necesario
vehiculos_path = 'C:/Users/User_001/Documents/PACD/proyecto/BBDD ONSV - VEHICULOS 2021-2023.xlsx' # modificar según sea necesario

# cargar datos
siniestros = load_data(siniestros_path)
vehiculos = load_data(vehiculos_path)

# limpiar siniestros 'CÓDIGO SINIESTRO'
siniestros = siniestros.drop_duplicates(subset = 'CÓDIGO SINIESTRO', keep = 'first') # eliminar duplicados de la base de datos de siniestros

# seleccionar columnas de interés
siniestros = siniestros[['CÓDIGO SINIESTRO', 'FECHA SINIESTRO', 'HORA SINIESTRO', 'CLASE SINIESTRO', 'DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'TIPO DE VÍA', 'COORDENADAS LATITUD', 'COORDENADAS  LONGITUD', 'CONDICIÓN CLIMÁTICA', 'SUPERFICIE DE CALZADA', 'CAUSA FACTOR PRINCIPAL']]
vehiculos = vehiculos[['CÓDIGO SINIESTRO', 'VEHÍCULO', 'MES', 'DÍA', 'HORA', 'AÑO']]

# realizar merge entre siniestros y vehículos
vehiculos_siniestros = pd.merge(siniestros, vehiculos, on = 'CÓDIGO SINIESTRO', how = 'inner')
print(vehiculos_siniestros.shape)

# mostrar las primeras filas del dataframe resultante
print(vehiculos_siniestros.head(10))

# crear la aplicación Dash
app = Dash()

app.layout = html.Div([
    html.H1('Siniestros de tránsito en Perú 2021-2023')
])