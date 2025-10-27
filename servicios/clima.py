import requests

def consultar_clima(ciudad):
    """
    Consulta el clima actual de una ciudad usando la API de wttr.in. Más info en https://wttr.in/:help
    Devuelve un diccionario con temperatura, sensación térmica y descripción.
    """
    # url = f"https://wttr.in/{ciudad}"
    url = f"https://wttr.in/{ciudad}?format=j1"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        clima_actual = datos["current_condition"][0]
        print( clima_actual)
        return {
            "temperatura": clima_actual["temp_C"],
            "sensacion": clima_actual["FeelsLikeC"],
            "descripcion": clima_actual["weatherDesc"][0]["value"]
        }
    except Exception as e:
        print("Error al consultar el clima:", e)
        return None