import json
import pandas as pd
from datetime import UTC, datetime
from drug_safety_pipeline.extract import extraer_eventos

DIRECTORIO = "data/bronze" #acá pongo el archivo Parquet
COLUMNAS = ["reportduplicate", "primarysource", "sender", "receiver", "patient"] #son las columnas de la API que están anidadas.

def build_bronze(datos, ingestion_ts):
    """Función que recibe los datos de la API y convierte cada columna anidada en un string JSON para poder guardarla en Parquet"""
    df=pd.DataFrame(datos["results"]) #acá nace el dataframe con las columnas que devuelve la API, incluyendo las 5 anidadas.
    for columna in COLUMNAS: #son columnas que ya existen. Las recorre y cambia el contenido a texto.
        df[columna]=df[columna].apply(json.dumps)
    df["ingestion_ts"]=ingestion_ts #agregamos una columna con la fecha de ingestión, es decir, el momento en el que se bajó un dato.
    return df

def guardar_bronze(df, fecha):
    """Función que guarda el DataFrame en un archivo Parquet"""
    df.to_parquet(f"{DIRECTORIO}/bronze_{fecha}.parquet") #guardar el archivo con la fecha procesada hace que correrlo dos veces no duplique
    
def main(fecha):
    """Función principal que extrae los datos de la API, construye el DataFrame y lo guarda en un archivo Parquet. Procesa un día de punta a punta"""
    datos= extraer_eventos(fecha,fecha)
    df=build_bronze(datos, datetime.now(UTC))
    guardar_bronze(df, fecha) #la fecha es el día que se procesa, en formato AAAAMMDD y se usa para pedirle los reportes a la API y para nombrar el archivo.
