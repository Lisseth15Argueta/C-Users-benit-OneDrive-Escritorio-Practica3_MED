lista = []

while True:
    print("Menú:")
    print("a. Añadir número a la lista")
    print("b. Añadir número de la lista en una posición")
    print("c. Longitud de la lista")
    print("d. Eliminar el último número")
    print("e. Eliminar un número")
    print("f. Contar números")
    print("g. Posiciones de un número")
    print("h. Mostrar números")
    print("i. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "a":
        numero = int(input("Ingrese un número: "))
        lista.append(numero)
        print("Número añadido a la lista.")

    elif opcion == "b":
        numero = int(input("Ingrese un número: "))
        posicion = int(input("Ingrese una posición: "))
        if posicion >= 1 and posicion <= len(lista) + 1:
            lista.insert(posicion - 1, numero)
            print("Número añadido a la lista en la posición", posicion)
        else:
            print("Posición inválida.")

    elif opcion == "c":
        print("Longitud de la lista:", len(lista))

    elif opcion == "d":
        if len(lista) > 0:
            ultimo_numero = lista.pop()
            print("Último número de la lista:", ultimo_numero)
        else:
            print("La lista está vacía.")

    elif opcion == "e":
        posicion = int(input("Ingrese una posición: "))
        if posicion >= 1 and posicion <= len(lista):
            numero_eliminado = lista.pop(posicion - 1)
            print("Número", numero_eliminado, "eliminado de la lista.")
        else:
            print("Posición inválida.")

    elif opcion == "f":
        numero = int(input("Ingrese un número: "))
        cantidad = lista.count(numero)
        print("Cantidad de apariciones del número", numero, "en la lista:", cantidad)

    elif opcion == "g":
        numero = int(input("Ingrese un número: "))
        posiciones = [i + 1 for i, x in enumerate(lista) if x == numero]
        print("Posiciones del número", numero, "en la lista:", posiciones)

    elif opcion == "h":
        print("Números en la lista:", lista)

    elif opcion == "i":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")