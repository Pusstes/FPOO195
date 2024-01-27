cadena = input("Ingrese una palabra: ")
cadena = cadena.replace(" ", "").lower()
if cadena == cadena[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")