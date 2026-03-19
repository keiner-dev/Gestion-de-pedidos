def reporte_detallado():  # Define la función del reporte detallado
    print("\n--- REPORTE DETALLADO ---")  # Título del reporte
    
    for id_pedido, datos in pedidos.items():  # Recorre todos los pedidos
        cliente = clientes[datos['cliente_id']]['nombre']  # Busca el nombre del cliente usando su ID
        producto = productos[datos['producto_id']][0]  # Obtiene el nombre del producto (posición 0 de la tupla)
        
        print(f"Pedido: {id_pedido}")  # Muestra el ID del pedido
        print(f"  Cliente: {cliente}")  # Muestra el nombre del cliente
        print(f"  Producto: {producto}")  # Muestra el producto
        print(f"  Cantidad: {datos['cantidad']}")  # Muestra la cantidad pedida
        print(f"  Total: ${datos['total']:.2f}")  # Muestra el total con formato de dinero
        print("-" * 20)  # Imprime una línea separadora