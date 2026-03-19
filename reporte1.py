def reporte_simple():  # Define la función del reporte simple
    print("\n--- REPORTE SIMPLE ---")  # Muestra el título del reporte
    
    for id_pedido, datos in pedidos.items():  # Recorre cada pedido (ID y datos)
        print(f"{id_pedido} | Cliente: {datos['cliente_id']} | Total: ${datos['total']:.2f}")  # Imprime info básica
    
    print("----------------------")  # Línea final del reporte