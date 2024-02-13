# Crea un programa usando funciones y lo que necesites para que el usuario inserte
# N números en una Tupla, después de la captura debe desplegar el siguiente menú
# funcional
# 1. Sumatoria de los elementos de la lista
# 2. Numero mayor de la lista
# 3. Numero menor de la lista
# 4. Promedio
# 5. Moda: es el valor que más se repite de un conjunto de datos
# 6. Rango: es la diferencia entre el valor máximo y el valor mínimo de un
# conjunto de datos

# funcion para pedir la tupla

import statistics

def pedirTupla():
    numeros = tuple(map(int, input("Ingrese los números separados por espacios: ").split()))
    return numeros

def sumarTupla(tupla):
    suma = sum(tupla)
    return suma

def numeroMayor(tupla):
    mayor = max(tupla)
    return mayor

def numeroMenor(tupla):
    menor = min(tupla)
    return menor

def promedio(tupla):
    promedio = sum(tupla) / len(tupla)
    return promedio

def moda(tupla):
    moda = statistics.mode(tupla)
    return moda


def rango(tupla):
    rango = max(tupla) - min(tupla)
    return rango

def menu():
    print("Operaciones con tupla:\n1. Sumatoria de los elementos de la lista.\n2. Número mayor de la lista\n3. Número menor de la lista\n4. Promedio\n5. Moda\n6. Rango\n7. Salir")

def main():
    numeros = pedirTupla()
    while True:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
          print("La sumatoria de la tupla es:", sumarTupla(numeros))
          print("\n")
        elif opcion == 2:
          print("El número mayor de la tupla es:", numeroMayor(numeros))
          print("\n")
        elif opcion == 3:
          print("El número menor de la tupla es:", numeroMenor(numeros))
          print("\n")
        elif opcion == 4:
          print("El promedio de los elementos de la tupla es:", promedio(numeros))
          print("\n")
        elif opcion == 5:
          print("La moda de la tupla es: ", moda(numeros))
          print("\n")
        elif opcion == 6:
          print("El rango de la tupla es:", rango(numeros))
          print("\n")
        elif opcion == 7:
          print("Bye")
          print("\n")
          break
        else:
          print("Opción no válida. ingrese una opción válida.")
          print("\n")

main()
    