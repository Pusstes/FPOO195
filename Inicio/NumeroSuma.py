X = int(input("Ingrese un entero: "))

suma = 0
for i in range(1, X + 1):
    suma += i

print("La suma de todos los enteros desde 1 hasta", X, "es:", suma)