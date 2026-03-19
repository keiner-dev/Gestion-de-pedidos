# sistema_pedidos.py
# Solución completa para el "Desafío de Desarrollo en Python semana 2".

# --- ESTRUCTURAS DE DATOS PRINCIPALES ---
# Se usarán diccionarios para almacenar la información, cumpliendo con los requisitos.

# Almacenará los clientes. Ejemplo: {'C001': {'nombre': 'Juan Perez', 'email': 'juan@riwi.es'}}
clientes = {}

# Almacenará los productos. Ejemplo: {'P001': ('Laptop', 1200.00)}
productos = {}

# Almacenará los pedidos. Ejemplo: {'ORD001': {'cliente_id': 'C001', 'producto_id': 'P001', 'cantidad': 1, 'total': 1200.00}}
pedidos = {}


# --- FUNCIONES DE UTILIDAD ---

def mostrar_clientes():
    """Muestra una lista de todos los clientes registrados."""
    print("--- Clientes Registrados ---")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for id_cliente, datos in clientes.items():
            print(f"ID: {id_cliente} | Nombre: {datos['nombre']} | Email: {datos['email']}")
    print("----------------------------")

def mostrar_productos():
    """Muestra una lista de todos los productos disponibles."""
    print("--- Productos Disponibles ---")
    if not productos:
        print("No hay productos registrados.")
    else:
        for id_producto, datos in productos.items():
            nombre_prod, precio_prod = datos
            print(f"ID: {id_producto} | Producto: {nombre_prod} | Precio: ${precio_prod:.2f}")
    print("-----------------------------")


# --- 1. REGISTRO DE CLIENTES ---

def registrar_cliente():
    """Pide los datos de un nuevo cliente y lo añade al diccionario de clientes."""
    print("--- Registrar Nuevo Cliente ---")
    id_cliente = f"C{len(clientes) + 1:03d}"
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    
    clientes[id_cliente] = {'nombre': nombre, 'email': email}
    print(f"¡Cliente '{nombre}' registrado con éxito con el ID: {id_cliente}!")


# --- 2. REGISTRO DE PRODUCTOS ---

def registrar_producto():
    """Pide los datos de un nuevo producto y lo añade al diccionario de productos."""
    print("--- Registrar Nuevo Producto ---")
    id_producto = f"P{len(productos) + 1:03d}"
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Error: El precio debe ser un número.")
        return
        
    # Se guarda como una tupla para cumplir el requisito de usar tuplas para datos inmutables.
    productos[id_producto] = (nombre, precio)
    print(f"¡Producto '{nombre}' registrado con éxito con el ID: {id_producto}!")


# --- 3. CREACIÓN DE PEDIDOS ---

def crear_pedido():
    """Crea un nuevo pedido asociando un cliente, un producto y una cantidad."""
    print("--- Crear Nuevo Pedido ---")
    
    if not clientes or not productos:
        print("Error: Debe registrar clientes y productos antes de crear un pedido.")
        return

    mostrar_clientes()
    id_cliente = input("Ingrese el ID del cliente para el pedido: ")
    if id_cliente not in clientes:
        print("Error: ID de cliente no válido.")
        return

    mostrar_productos()
    id_producto = input("Ingrese el ID del producto para el pedido: ")
    if id_producto not in productos:
        print("Error: ID de producto no válido.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad deseada: "))
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        return

    # Calcular el total
    _, precio_unitario = productos[id_producto]
    total_pedido = precio_unitario * cantidad
    
    # Crear y guardar el pedido
    id_pedido = f"ORD{len(pedidos) + 1:03d}"
    pedidos[id_pedido] = {
        'cliente_id': id_cliente,
        'producto_id': id_producto,
        'cantidad': cantidad,
        'total': total_pedido
    }
    
    print(f"¡Pedido {id_pedido} creado con éxito por un total de ${total_pedido:.2f}!")


# --- 4. CONSULTA DE PEDIDOS REGISTRADOS ---

def consultar_pedidos():
    """Muestra una lista detallada de todos los pedidos realizados."""
    print("--- Pedidos Registrados ---")
    if not pedidos:
        print("No se ha realizado ningún pedido.")
        return

    for id_pedido, datos_pedido in pedidos.items():
        id_cliente = datos_pedido['cliente_id']
        id_producto = datos_pedido['producto_id']
        
        # Obtener nombres para mayor claridad
        nombre_cliente = clientes.get(id_cliente, {}).get('nombre', 'Cliente no encontrado')
        nombre_producto, _ = productos.get(id_producto, ('Producto no encontrado', 0))

        print(f"ID Pedido: {id_pedido}")
        print(f"  - Cliente: {nombre_cliente} (ID: {id_cliente})")
        print(f"  - Producto: {nombre_producto}")
        print(f"  - Cantidad: {datos_pedido['cantidad']}")
        print(f"  - Total del pedido: ${datos_pedido['total']:.2f}")
        print("-" * 25)


# --- 5. CÁLCULO DE INGRESOS DEL DÍA ---

def calcular_ingresos_totales():
    """Suma los totales de todos los pedidos para obtener el ingreso total."""
    print("--- Ingresos Totales del Día ---")
    if not pedidos:
        print("No hay pedidos para calcular ingresos.")
        return 0.0

    total_ingresos = 0.0
    # Se usa una tupla de totales para el cálculo, evitando listas.
    for total_pedido in tuple(p['total'] for p in pedidos.values()):
        total_ingresos += total_pedido
    
    print(f"El ingreso total del día es: ${total_ingresos:.2f}")
    return total_ingresos


# --- 6. GENERACIÓN DE REPORTE FINAL ---

def generar_reporte_final():
    """Genera y muestra un reporte consolidado del día."""
    print("" + "="*40)
    print("--- REPORTE FINAL DEL DÍA ---")
    print("="*40)

    if not pedidos:
        print("No se realizaron operaciones hoy.")
        print("="*40)
        return

    # 1. Total de pedidos registrados
    total_pedidos = len(pedidos)
    print(f"1. Total de pedidos registrados: {total_pedidos}")

    # 2. Total de ingresos generados
    print("2. Total de ingresos generados:")
    total_ingresos = calcular_ingresos_totales()

    # 3. Pedidos agrupados por cliente
    print("3. Pedidos por cliente:")
    pedidos_por_cliente = {}
    for id_pedido, datos_pedido in pedidos.items():
        id_cliente = datos_pedido['cliente_id']
        if id_cliente not in pedidos_por_cliente:
            pedidos_por_cliente[id_cliente] = () # Tupla vacía para agregar pedidos
        
        # Añadir info del pedido a la tupla del cliente
        info_pedido = (id_pedido, productos[datos_pedido['producto_id']][0], datos_pedido['total'])
        pedidos_por_cliente[id_cliente] += (info_pedido,)

    for id_cliente, tupla_pedidos in pedidos_por_cliente.items():
        print(f"  - Cliente: {clientes[id_cliente]['nombre']}")
        for p in tupla_pedidos:
            print(f"    - Pedido {p[0]}: {p[1]} por ${p[2]:.2f}")

    # 4. Productos vendidos durante el día
    print("4. Resumen de productos vendidos:")
    productos_vendidos = {}
    for datos_pedido in pedidos.values():
        id_producto = datos_pedido['producto_id']
        cantidad = datos_pedido['cantidad']
        if id_producto not in productos_vendidos:
            productos_vendidos[id_producto] = 0
        productos_vendidos[id_producto] += cantidad
    
    for id_producto, cantidad_total in productos_vendidos.items():
        nombre_prod, _ = productos[id_producto]
        print(f"  - {nombre_prod}: {cantidad_total} unidades")
        
    print("" + "="*40)
    print("--- FIN DEL REPORTE ---")
    print("="*40)


# --- MENÚ PRINCIPAL ---

def menu_principal():
    """Muestra el menú principal y maneja la selección del usuario."""
    while True:
        print("===== Sistema de Gestion de Pedidos =====")
        print("1. Registrar Cliente")
        print("2. Registrar Producto")
        print("3. Crear Pedido")
        print("4. Consultar Pedidos")
        print("5. Calcular Ingresos Totales")
        print("6. Generar Reporte Final y Salir")
        print("=========================================")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            registrar_producto()
        elif opcion == '3':
            crear_pedido()
        elif opcion == '4':
            consultar_pedidos()
        elif opcion == '5':
            calcular_ingresos_totales()
        elif opcion == '6':
            generar_reporte_final()
            print("Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# --- PUNTO DE ENTRADA DEL PROGRAMA ---

if __name__ == "__main__":
    menu_principal()
