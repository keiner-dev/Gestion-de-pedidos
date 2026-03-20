import json
import os

ARCHIVO_CLIENTES = 'clientes.json'
ARCHIVO_PRODUCTOS = 'productos.json'
ARCHIVO_PEDIDOS = 'pedidos.json'

def cargar_datos(ruta_archivo):
    """
    Carga datos desde un archivo JSON.
    Args:
        ruta_archivo (str): La ruta al archivo JSON.
    Returns:
        dict: Los datos cargados desde el archivo JSON, o un diccionario vacío si el archivo no existe o está vacío.
    """
    if not os.path.exists(ruta_archivo):
        return {}
    try:
        with open(ruta_archivo, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def guardar_datos(ruta_archivo, datos):
    """
    Guarda datos en un archivo JSON.
    Args:
        ruta_archivo (str): La ruta al archivo JSON.
        datos (dict): Los datos a guardar.
    """
    with open(ruta_archivo, 'w') as f:
        json.dump(datos, f, indent=4)

def cargar_clientes():
    """Carga los datos de los clientes."""
    return cargar_datos(ARCHIVO_CLIENTES)

def guardar_clientes(clientes):
    """Guarda los datos de los clientes."""
    guardar_datos(ARCHIVO_CLIENTES, clientes)

def cargar_productos():
    """Carga los datos de los productos."""
    # Los productos se guardan como tuplas, pero JSON los guarda como listas.
    # Necesitamos convertirlos de nuevo a tuplas después de cargarlos.
    datos_productos = cargar_datos(ARCHIVO_PRODUCTOS)
    return {id_producto: tuple(info_producto) for id_producto, info_producto in datos_productos.items()}

def guardar_productos(productos):
    """Guarda los datos de los productos."""
    guardar_datos(ARCHIVO_PRODUCTOS, productos)

def cargar_pedidos():
    """Carga los datos de los pedidos."""
    return cargar_datos(ARCHIVO_PEDIDOS)

def guardar_pedidos(pedidos):
    """Guarda los datos de los pedidos."""
    guardar_datos(ARCHIVO_PEDIDOS, pedidos)
