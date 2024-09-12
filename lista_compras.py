
lista_compras = ["Manzanas", "Pan", "Leche", "Huevos", "Arroz", "Pasta", "Tomates", "Pollo", "Café", "Papel higiénico"]

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        articulo = input("Ingresa el nombre del artículo: ")
        lista_compras.append(articulo)
        print(f"{articulo} ha sido agregado a la lista.")
    
    elif opcion == '2':
        if lista_compras:
            print("Lista de compras:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i}. {articulo}")
            try:
                indice = int(input("Ingresa el número del artículo a eliminar: "))
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"{eliminado} ha sido eliminado de la lista.")
                else:
                    print("Índice no válido.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        else:
            print("La lista está vacía.")
    
    elif opcion == '3':
        if lista_compras:
            print("Lista de compras actual:")
            for articulo in lista_compras:
                print(f"- {articulo}")
        else:
            print("La lista está vacía.")
    
    elif opcion == '4':
        print("Gracias por usar la lista de compras. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")