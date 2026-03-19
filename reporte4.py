def reporte_productos_vendidos():  # Define la función del reporte de productos
    print("\n--- PRODUCTOS MÁS VENDIDOS ---")  # Título del reporte
    
    conteo = {}  # Diccionario para guardar la cantidad vendida por producto
    
    for datos in pedidos.values():  # Recorre todos los pedidos
        id_producto = datos['producto_id']  # Obtiene el ID del producto
        cantidad = datos['cantidad']  # Obtiene la cantidad vendida
        
        if id_producto not in conteo:  # Verifica si el producto aún no está en el conteo
            conteo[id_producto] = 0  # Inicializa el contador en 0
        
        conteo[id_producto] += cantidad  # Suma la cantidad vendida al producto
    
    for id_producto, total in conteo.items():  # Recorre los productos ya contados
        nombre = productos[id_producto][0]  # Obtiene el nombre del producto
        print(f"{nombre}: {total} unidades vendidas")  # Muestra cuántas unidades se vendieron