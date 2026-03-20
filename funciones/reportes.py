from . import gestion_datos

def calcular_ingresos_diarios(pedidos):
    """
    Calcula los ingresos totales de todos los pedidos.
    Args:
        pedidos (dict): Un diccionario de pedidos.
    Returns:
        float: Los ingresos totales.
    """
    ingresos_totales = 0.0
    for pedido in pedidos.values():
        ingresos_totales += pedido.get("total", 0)
    return ingresos_totales

def generar_reporte_final():
    """
    Genera un informe completo de todos los datos de ventas.
    Returns:
        dict: Un diccionario que contiene los datos del informe.
    """
    pedidos = gestion_datos.cargar_pedidos()
    clientes = gestion_datos.cargar_clientes()
    productos = gestion_datos.cargar_productos()

    total_pedidos = len(pedidos)
    ingresos_totales = calcular_ingresos_diarios(pedidos)

    # Agrupar pedidos por cliente
    pedidos_por_cliente = {}
    for id_pedido, datos_pedido in pedidos.items():
        id_cliente = datos_pedido["id_cliente"]
        if id_cliente not in pedidos_por_cliente:
            pedidos_por_cliente[id_cliente] = () # Usando tupla en lugar de lista
        pedidos_por_cliente[id_cliente] += (id_pedido,)

    # Consolidar productos vendidos
    productos_vendidos = {}
    for datos_pedido in pedidos.values():
        id_producto = datos_pedido["id_producto"]
        cantidad = datos_pedido["cantidad"]
        nombre_producto = productos.get(id_producto, ("Desconocido", 0))[0]
        
        if nombre_producto not in productos_vendidos:
            productos_vendidos[nombre_producto] = 0
        productos_vendidos[nombre_producto] += cantidad

    reporte = {
        "total_pedidos": total_pedidos,
        "ingresos_totales": ingresos_totales,
        "pedidos_por_cliente": pedidos_por_cliente,
        "productos_vendidos": productos_vendidos,
        "clientes_raw": clientes,
        "productos_raw": productos,
        "pedidos_raw": pedidos
    }
    
    return reporte
