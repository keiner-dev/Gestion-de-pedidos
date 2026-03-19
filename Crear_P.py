from gestion_datos import cargar_pedidos, guardar_pedidos

def main():
    """Crea un nuevo pedido y lo guarda."""
    pedidos = cargar_pedidos()
    nuevo_id = f"P{len(pedidos) + 1:03d}"
    print(f"--- Crear Pedido Nuevo (ID: {nuevo_id}) ---")

    try:
        cliente = input("Nombre del cliente: ")
        producto = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("\nError: Precio y cantidad deben ser números. El pedido no fue guardado.")
        return

    pedidos[nuevo_id] = {
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad,
        "total": precio * cantidad
    }
    
    guardar_pedidos(pedidos)
    print(f"\n¡Pedido {nuevo_id} guardado con éxito!")
