import json
import os

PEDIDOS_FILE = 'pedidos.json'

def cargar_pedidos():
    """Carga los pedidos desde el archivo JSON. Devuelve un diccionario vacío si no existe o está vacío."""
    if not os.path.exists(PEDIDOS_FILE):
        return {}
    try:
        with open(PEDIDOS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def guardar_pedidos(pedidos):
    """Guarda el diccionario de pedidos en el archivo JSON."""
    with open(PEDIDOS_FILE, 'w') as f:
        json.dump(pedidos, f, indent=4)
