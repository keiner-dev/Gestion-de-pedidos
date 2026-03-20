from . import gestion_datos

def crear_pedido(id_cliente, id_producto, cantidad):
    """
    Crea un nuevo pedido.

    Args:
        id_cliente (str): El ID del cliente que realiza el pedido.
        id_producto (str): El ID del producto que se está pidiendo.
        cantidad (int): La cantidad del producto que se está pidiendo.

    Returns:
        tuple: Una tupla que contiene el ID del nuevo pedido y sus datos, o (None, None) if the product is not found.
    """
    pedidos = gestion_datos.cargar_pedidos()
    productos = gestion_datos.cargar_productos()

    # Comprobar si el producto existe
    if id_producto not in productos:
        return None, None

    # Obtener el precio del producto de la tupla (nombre, precio)
    precio_producto = productos[id_producto][1]
    
    # Calcular el total
    total = precio_producto * cantidad
    
    # Generar un nuevo ID de pedido
    nuevo_id_pedido = f"O{len(pedidos) + 1:03d}"
    
    # Crear un nuevo pedido
    pedidos[nuevo_id_pedido] = {
        "id_cliente": id_cliente,
        "id_producto": id_producto,
        "cantidad": cantidad,
        "total": total
    }
    
    # Guardar pedidos
    gestion_datos.guardar_pedidos(pedidos)
    
    return nuevo_id_pedido, pedidos[nuevo_id_pedido]

def obtener_todos_los_pedidos():
    """
    Recupera todos los pedidos registrados.

    Returns:
        dict: Un diccionario de todos los pedidos.
    """
    return gestion_datos.cargar_pedidos()
