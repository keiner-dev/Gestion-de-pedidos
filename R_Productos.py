Reset = "\033[0m"
Pink = "\033[95m"
Green = "\033[92m"
Yellow = "\033[93m"

while True:
    try:
        N_Producto = input(Pink + "💖 Escribe el nombre del producto 💖\n⭐ " + Reset)
        
        if N_Producto.isalpha():
            None

        else:
            print("Error, ingrese solo letras")
            continue

        P_Producto = float(input(Pink + "💖 Escribe el precio del producto 💖\n⭐ " + Reset))

        if P_Producto <= 0:
            print(Yellow + "El valor del producto no es válido, intenta de nuevo" + Reset)

        C_Producto = int(input(Pink + "💖 Escribe la cantidad del producto 💖\n⭐   " + Reset))
        if C_Producto <= 0: 
            print(Yellow + "Ingresa una cantidad válida" + Reset)
            continue
        break
    except ValueError:
        print("Ingrese un valor valido")
print(Green + " ✨ Tu producto ha sido registrado con éxito ✨ " + Reset)