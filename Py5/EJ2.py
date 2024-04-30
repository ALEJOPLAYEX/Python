
""" Crea un sistema para controlar el inventario de productos de una tienda. Utiliza un conjunto para
almacenar los códigos de barras de los productos disponibles. Permite al usuario agregar
nuevos productos al inventario, verificar la disponibilidad de un producto y eliminar productos
obsoletos. """


productos_disp = {"pepe@gmail.com", "david@gmail.com", "daniel@gmail.com", "olga@gmail.com"}

while True:
    print("\nMenu")
    print("1. Agregar Producto")
    print("2. Verificar Producto")
    print("3. Eliminar Producto")
    print("4. Salir")
    opcion = input("Escoja una opcion: ")

    try:
        opcion = int(opcion)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        producto = input("Ingrese el producto del cliente: ").strip().lower()
        if producto in productos_disp:
            print("El cliente ya está registrado.")
        else:
            productos_disp.add(producto)
            print("Cliente agregado con éxito.")
    elif opcion == 2:
        producto = input("Ingrese el producto del cliente: ").strip().lower()
        if producto in productos_disp:
            print("El cliente ya está registrado.")
        else:
            print("El cliente no está registrado.")
    elif opcion == 3:
        producto = input("Ingrese el producto del cliente: ").strip().lower()
        if producto in productos_disp:
            productos_disp.remove(producto)
            print("Cliente eliminado con éxito.")
        else:
            print("No se pudo eliminar: El cliente no está registrado.")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")
    print("Clientes registrados:", productos_disp)
    
