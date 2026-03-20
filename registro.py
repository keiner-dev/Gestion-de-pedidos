#crea un diccioanrio vacio
cliente = {}
#define funcion, encapsula todo el proceso de registro
def registrar_cliente():
    #definimos la variable "id_cliente" para que guarde en la tupla el ide "k{len(cliente) + 1:03d}" que lo mostraria de esta forma "K001"
    id_cliente = f"K{len(cliente) + 1:03d}"
    while True:   
        nombre = input("Registrar cliente: \n")
        #verifica solo letras
        if not nombre.isalpha():
            print("Ingrese un nombre válido.")
            continue
        email = input("Ingrese el email del cliente: \n")
        #comprueba que tenga '@' '.' Si no repite el bucle        
        if '@' not in email or '.com' not in email:
            print("Ingrese un email válido.")
            continue
        #agrega registro al dicionario cliente y un diccionario con nombre y email como valor. 
        cliente[id_cliente] = {'nombre': nombre, 'email': email}
        print("======= CLIENTE REGISTRADO =======\n")
        #Confirma el registro exitoso y muestra el ID
        print(f"¡cliente '{nombre}' registrado con exito con el ID: {id_cliente}!")
        break
#Llama la funcion para ejecutar el proceso de registro