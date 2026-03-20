from . import gestion_datos

def registrar_cliente(nombre, email):
    """
    Registra un nuevo cliente.
    Args:
        nombre (str): El nombre del cliente.
        email (str): El email del cliente.
    Returns:
        tuple: Una tupla que contiene el ID del nuevo cliente y sus datos.
    """
    clientes = gestion_datos.cargar_clientes()
    
    # Generar un nuevo ID de cliente
    nuevo_id_cliente = f"C{len(clientes) + 1:03d}"
    
    # Agregar el nuevo cliente
    clientes[nuevo_id_cliente] = {'nombre': nombre, 'email': email}
    
    # Guardar los datos actualizados de los clientes
    gestion_datos.guardar_clientes(clientes)
    
    return nuevo_id_cliente, clientes[nuevo_id_cliente]

def obtener_todos_los_clientes():
    """
    Recupera todos los clientes registrados.
    Returns:
        dict: Un diccionario de todos los clientes.
    """
    return gestion_datos.cargar_clientes()
