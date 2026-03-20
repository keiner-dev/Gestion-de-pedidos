from .colores import GRIS, ROJO, VERDE, AMARILLO, ROSA, RESET, AZUL, CYAN

def mostrar_menu():
    """Muestra el menú principal y obtiene la elección del usuario."""
    print(AMARILLO + "🌸 Bienvenido al Sistema de Gestión de Pedidos 🌸\n" + RESET)
    print(CYAN + "✨ Por favor, elija una opción ✨" + RESET)
    print(ROSA + " 👤 1. Registrar Cliente 👤 " + RESET )
    print(ROSA + " 📦 2. Registrar Producto 📦 " + RESET)
    print(ROSA + " 🧾 3. Crear Pedido 🧾 " + RESET)
    print(ROSA + " 📋 4. Ver Pedidos Registrados 📋 " + RESET)
    print(ROSA + " 📊 5. Generar Reporte Final 📊 " + RESET)
    print(ROSA + " ❌ 6. Salir ❌ " + RESET)
    
    opcion = input(GRIS + "> " + RESET)
    return opcion

def obtener_detalles_cliente():
    """Obtiene los detalles de un nuevo cliente del usuario."""
    nombre = input( VERDE + " 👤 Ingrese el nombre del cliente: 👤  \n " + RESET)
    email = input( ROSA + " 📧 Ingrese el email del cliente: 📧 \n " + RESET)
    return nombre, email

def obtener_detalles_producto():
    """Obtiene los detalles de un nuevo producto del usuario."""
    nombre = input(VERDE  + "Ingrese el nombre del producto: \n " + RESET)
    while True:
        try:
            precio = float(input(ROSA + "💰 Ingrese el precio del producto: 💰 \n " + RESET))
            break
        except ValueError:
            print(AMARILLO + "⚠️ Precio inválido. Por favor, ingrese un número. ⚠️" + RESET)
    return nombre, precio

def obtener_detalles_pedido(clientes, productos):
    """Obtiene los detalles de un nuevo pedido del usuario."""
    print(ROSA + "--- Clientes Disponibles ---" + RESET)
    for id_c, datos_c in clientes.items():
        print(f"ID: {id_c}, Nombre: {datos_c['nombre']}")
    id_cliente = input(VERDE + "Ingrese el ID del cliente para el pedido:  \n " + RESET) 

    print("--- Productos Disponibles ---")
    for id_p, datos_p in productos.items():
        print(f"ID: {id_p}, Nombre: {datos_p[0]}, Precio: ${datos_p[1]:.2f}")
    id_producto = input(ROSA + "Ingrese el ID del producto para el pedido: \n " +  RESET)
    
    while True:
        try:
            cantidad = int(input(VERDE + "Ingrese la cantidad: \n " + RESET ))
            break
        except ValueError:
            print(AMARILLO + "⚠️ Cantidad inválida. Por favor, ingrese un número entero. ⚠️ " + RESET)
            
    return id_cliente, id_producto, cantidad

def mostrar_pedidos(pedidos, clientes, productos):
    """Muestra una lista de todos los pedidos."""
    print(VERDE + "--- Pedidos Registrados ---" + RESET)
    if not pedidos:
        print("⚠️ No se encontraron pedidos. ⚠️ ")
        return

    for id_pedido, datos_pedido in pedidos.items():
        nombre_cliente = clientes.get(datos_pedido['id_cliente'], {}).get('nombre', 'N/A')
        nombre_producto = productos.get(datos_pedido['id_producto'], ('N/A', 0))[0]
        
        print(
            f"ID: {id_pedido} | "
            f"Cliente: {nombre_cliente} | "
            f"Producto: {nombre_producto} | "
            f"Cantidad: {datos_pedido['cantidad']} | "
            f"Total: ${datos_pedido['total']:.2f}"
        )
    print("--------------------------")

def mostrar_reporte(reporte):
    """Muestra el reporte final."""
    print(VERDE + "--- Reporte Final ---" + RESET)
    print(f"Total de Pedidos: {reporte['total_pedidos']}")
    print(f"Ingresos Totales: ${reporte['ingresos_totales']:.2f}")

    print(VERDE + "--- Productos Vendidos ---" + RESET )
    if not reporte['productos_vendidos']:
        print(AMARILLO + " ⚠️ No se vendieron productos. ⚠️ " + RESET )
    else:
        for nombre_producto, cantidad in reporte['productos_vendidos'].items():
            print(f"- {nombre_producto}: {cantidad} unidades")

    print(ROSA + "--- Pedidos por Cliente ---" + RESET )
    if not reporte['pedidos_por_cliente']:
        print(" ⚠️ No se encontraron pedidos para ningún cliente. ⚠️")
    else:
        for id_cliente, ids_pedidos in reporte['pedidos_por_cliente'].items():
            nombre_cliente = reporte['clientes_raw'].get(id_cliente, {}).get('nombre', 'Desconocido')
            print(f"Cliente: {nombre_cliente} (ID: {id_cliente})")
            for id_pedido in ids_pedidos:
                datos_pedido = reporte['pedidos_raw'].get(id_pedido)
                if datos_pedido:
                    nombre_producto = reporte['productos_raw'].get(datos_pedido['id_producto'], ('N/A', 0))[0]
                    print(
                        f"  - ID Pedido: {id_pedido}, Producto: {nombre_producto}, "
                        f"Cantidad: {datos_pedido['cantidad']}, Total: ${datos_pedido['total']:.2f}"
                    )

    print("----------------------")
