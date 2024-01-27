edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    print("El cliente puede entrar gratis.")
else:
    if 4 <= edad <= 18:
        print("El precio de la entrada es: $110.")
    else:
        print("El precio de la entrada es: $190.")