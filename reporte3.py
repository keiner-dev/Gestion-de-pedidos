def reporte_por_cliente():  # Define la función del reporte por cliente
    print("\n--- REPORTE POR CLIENTE ---")  # Título del reporte
    
    for id_cliente, datos_cliente in clientes.items():  # Recorre todos los clientes
        print(f"\nCliente: {datos_cliente['nombre']}")  # Muestra el nombre del cliente
        
        total_cliente = 0  # Variable para acumular el total gastado por ese cliente
        
        for datos in pedidos.values():  # Recorre todos los pedidos
            if datos['cliente_id'] == id_cliente:  # Verifica si el pedido pertenece a ese cliente
                total_cliente += datos['total']  # Suma el total del pedido al acumulado
        
        print(f"Total gastado: ${total_cliente:.2f}")  # Muestra cuánto gastó ese cliente