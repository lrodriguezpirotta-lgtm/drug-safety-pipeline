import requests

URL = "https://api.fda.gov/drug/event.json"


def extraer_eventos(fecha_desde, fecha_hasta, limite=100):
    """Trae los reportes de eventos adversos recibidos entre dos fechas.
    
    Las fechas van en formato AAAAMMDD, por ejemplo "20260901".
    """
    filtros = {
        "search": f"receivedate:[{fecha_desde} TO {fecha_hasta}]",
        "limit": limite,
    }
    #El TO es la sintaxis que usa la API de la FDA para indicar un rango de fechas.
    respuesta = requests.get(URL, params=filtros, timeout=10)
    #Si en 10s no responde se corta la espera y lanza un error.
    respuesta.raise_for_status()
    return respuesta.json()