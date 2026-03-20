import funciones.gestion_clientes as gestion_clientes, funciones.gestion_pedidos as gestion_pedidos, funciones.gestion_productos as gestion_productos, funciones.interfaz as interfaz, funciones.reportes as reportes

from funciones.Iniciando import Limpiar_pantalla
from funciones.Iniciando import cargar

"""
Función principal para ejecutar la aplicación.
"""
while True:
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()

    opcion = interfaz.mostrar_menu()

    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()

    if opcion == '1':
            # Registrar Cliente
            nombre, email = interfaz.obtener_detalles_cliente()
            if not nombre or not email:
                print("El nombre y el email no pueden estar vacíos.")
                continue
            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
            nuevo_id, nuevo_cliente = gestion_clientes.registrar_cliente(nombre, email)
            print(f"Cliente '{nuevo_cliente['nombre']}' registrado con ID: {nuevo_id}")
            input("Precione Enter para continuar\n")
            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()

    elif opcion == '2':
            # Registrar Producto
            nombre, precio = interfaz.obtener_detalles_producto()
            if not nombre or precio <= 0:
                print("El nombre del producto no puede estar vacío y el precio debe ser positivo.")
                input("Precione ENTER para continuar")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                continue

            nuevo_id, nuevo_producto = gestion_productos.registrar_producto(nombre, precio)
            print(f"Producto '{nuevo_producto[0]}' registrado con ID: {nuevo_id}")
            input("Precione ENTER para continuar")
            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()

    elif opcion == '3':
            # Crear Pedido
            clientes = gestion_clientes.obtener_todos_los_clientes()
            productos = gestion_productos.obtener_todos_los_productos()
            if not clientes or not productos:
                print("Por favor, registre clientes y productos antes de crear un pedido.")
                input("Precione ENTER para continuar")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                continue
            
            
            id_cliente, id_producto, cantidad = interfaz.obtener_detalles_pedido(clientes, productos)
            
            if id_cliente not in clientes:
                print("ID de cliente inválido.")
                input("Precione ENTER para continuar")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                continue
            if id_producto not in productos:
                print("ID de producto inválido.")
                input("Precione ENTER para continuar")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                continue
            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
                input("Precione ENTER para continuar")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                continue

            nuevo_id, nuevo_pedido = gestion_pedidos.crear_pedido(id_cliente, id_producto, cantidad)
            if nuevo_id:
                print(f"Pedido {nuevo_id} creado con éxito por un total de ${nuevo_pedido['total']:.2f}")
                input("Precione ENTER para continuar")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
            else:
                print("No se pudo crear el pedido.")
                input("Precione ENTER para continuar")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()

    elif opcion == '4':
            # Ver Pedidos Registrados
            pedidos = gestion_pedidos.obtener_todos_los_pedidos()
            clientes = gestion_clientes.obtener_todos_los_clientes()
            productos = gestion_productos.obtener_todos_los_productos()
            input("Precione ENTER para continuar")
            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
            interfaz.mostrar_pedidos(pedidos, clientes, productos)

    elif opcion == '5':
            # Generar Reporte Final
            reporte = reportes.generar_reporte_final()
            input("Precione ENTER para continuar")
            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
            interfaz.mostrar_reporte(reporte)

    elif opcion == '6':
            print("Gracias por usar nuestro programa, bonito día.")
            break

    else:
            print("Opción no válida, por favor intente de nuevo.")

