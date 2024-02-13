
import random

def llenar_lista():
    lista = [random.randint(10, 20) for _ in range(30)]
    return lista

def contar_repetidos(lista):
    repetidos = {}
    for num in lista:
        if num in repetidos:
            repetidos[num] += 1
        else:
            repetidos[num] = 1
    return repetidos
    

def eliminar_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

def remplazar_repetidos_con_cero(lista):
    repetidos = contar_repetidos(lista)
    for num, cantidad in repetidos.items():
        if cantidad > 1:
            for i in range(cantidad - 1):
                index = lista.index(num)
                lista[index] = 0
    return lista

def main():
    lista = llenar_lista()
    while True:
        print("Lista generada:", lista)
        opcion = input("Seleccione una opción:\n"
                       "a. Contar número repetidos\n"
                       "b. Eliminar número repetidos\n"
                       "c. Remplazar los repetidos con 0\n"
                       "d. Salir\n"
                       "Opción: ")
        if opcion == 'a':
            repetidos = contar_repetidos(lista)
            print("Número repetidos:", repetidos)
            print("\n")
        elif opcion == 'b':
            lista_sin_repetidos = eliminar_repetidos(lista)
            print("Lista sin repetidos:", lista_sin_repetidos)
            print("\n")
        elif opcion == 'c':
            lista_remplazada = remplazar_repetidos_con_cero(lista)
            print("Lista con repetidos remplazados por 0:", lista_remplazada)
        elif opcion == 'd':
            print("Adiós.")
            print("\n")
            break
        else:
            print("Opción no válida.")
            print("\n")

main()
