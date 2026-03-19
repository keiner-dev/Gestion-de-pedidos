from gestion_datos import cargar_pedidos

def Consultar_P():
    """Carga y muestra todos los pedidos registrados."""
    pedidos = cargar_pedidos()

    if not pedidos:
        print("No hay pedidos registrados.")
        return

    print("\n--- Lista de Pedidos Registrados ---")
    for id_pedido, detalles in pedidos.items():
        print(
            f"ID: {id_pedido} | "
            f"Cliente: {detalles.get('cliente', 'N/A')} | "
            f"Producto: {detalles.get('producto', 'N/A')} | "
            f"Cantidad: {detalles.get('cantidad', 0)} | "
            f"Total: ${detalles.get('total', 0):.2f}"
        )
    print("--------------------------------------\n")

main ()