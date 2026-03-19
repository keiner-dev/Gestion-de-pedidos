cliente = {}

def registrar_cliente():
    id_cliente = f"k{len(cliente) + 1:03d}"
    while True:   
        nombre = input("Registrar cliente: \n")
        
        if not nombre.isalpha():
            print("Ingrese un nombre válido.")
            continue
        email = input("Ingrese el email del cliente: \n")
                
        if '@' not in email or '.com' not in email:
            print("Ingrese un email válido.")
            continue
        
        cliente[id_cliente] = {'nombre': nombre, 'email': email}
        print("======= CLIENTE REGISTRADO =======\n")
        print(f"¡cliente '{nombre}' registrado con exito con el ID: {id_cliente}!")
        break
registrar_cliente()

