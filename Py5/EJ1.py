""" Desarrolla un programa para gestionar clientes de una empresa. Utiliza un conjunto para
almacenar los correos electrónicos de los clientes registrados. Permite al usuario agregar
nuevos clientes, verificar si un cliente ya está registrado y eliminar clientes """


correos = {"pepe@gmail.com", "david@gmail.com", "daniel@gmail.com", "olga@gmail.com"}

while True:
    print("\nMenu")
    print("1. Agregar cliente")
    print("2. Verificar cliente")
    print("3. Eliminar cliente")
    print("4. Salir")
    opcion = input("Escoja una opcion: ")

    try:
        opcion = int(opcion)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        correo = input("Ingrese el correo del cliente: ").strip().lower()
        if correo in correos:
            print("El cliente ya está registrado.")
        else:
            correos.add(correo)
            print("Cliente agregado con éxito.")
    elif opcion == 2:
        correo = input("Ingrese el correo del cliente: ").strip().lower()
        if correo in correos:
            print("El cliente ya está registrado.")
        else:
            print("El cliente no está registrado.")
    elif opcion == 3:
        correo = input("Ingrese el correo del cliente: ").strip().lower()
        if correo in correos:
            correos.remove(correo)
            print("Cliente eliminado con éxito.")
        else:
            print("No se pudo eliminar: El cliente no está registrado.")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")
    print("Clientes registrados:", correos)
    

