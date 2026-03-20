from . import gestion_datos

def registrar_producto(nombre, precio):
    """
    Registra un nuevo producto.
    Args:
        nombre (str): El nombre del producto.
        precio (float): El precio unitario del producto.
    Returns:
        tuple: Una tupla que contiene el ID del nuevo producto y sus datos como una tupla (nombre, precio).
    """
    productos = gestion_datos.cargar_productos()
    
    # Generar un nuevo ID de producto
    nuevo_id_producto = f"P{len(productos) + 1:03d}"
    
    # Agregar el nuevo producto como una tupla
    productos[nuevo_id_producto] = (nombre, precio)
    
    # Guardar los datos actualizados de los productos
    gestion_datos.guardar_productos(productos)
    
    return nuevo_id_producto, productos[nuevo_id_producto]

def obtener_todos_los_productos():
    """
    Recupera todos los productos registrados.
    Returns:
        dict: Un diccionario de todos los productos, donde el valor es una tupla (nombre, precio).
    """
    return gestion_datos.cargar_productos()
