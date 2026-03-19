#✨Colores para imprimir mensajes cute✨

Reset = "\033[0m"
Pink = "\033[95m"
Green = "\033[92m"
Yellow = "\033[93m"
Blue = "\033[94m"

# Ejecutamos el bloque de código
while True:
    try:
    # Definimos variables
        Product_ID = input(Pink + "💖 Introdue el ID del producto 💖\n⭐ " + Reset)

    # Definimos variable
        Produt_Name = (input(Pink + "💖 Escribe el nombre del producto 💖\n⭐ " + Reset))
    # Validamos entrada de datos
        if Produt_Name.isalpha():
            None
        else:
            print(Yellow + "El valor nombre no es válido, intenta de nuevo" + Reset)
    
    # Definimos variable
        Unit_Price = float(input(Pink + "💖 Ingresa el precio del producto 💖\n⭐" + Reset))
    # Validamos entrada de datos
        if Unit_Price <= 0: 
            print(Yellow + "Ingresa un precio válido" + Reset)
            break
        # Salimos del ciclo
            
# Creamos tupla
        Registro_P = (Product_ID, Produt_Name, Unit_Price)
    
    # Datos de salida
        print(Green + "✨ Has registrado con éxito tu producto ✨" + Reset)
        print(Pink + "Historia de tu registro:" + Reset)
        print("ID de tu producto:" , Product_ID)
        print("Nombre de tu producto:" , Produt_Name)
        print("Precio de tu producto:" , Unit_Price)
  
  
    except ValueError:
        print("Ingrese un valor válido")
    print(Green + " ✨ Tu producto ha sido registrado con éxito ✨ " + Reset)
