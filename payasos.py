payasos = int(input("Ingrese el número de payasos vendidos: "))
munecas = int(input("Ingrese el número de muñecas vendidas: "))

pesopa = 112
pesomu = 75

total = (payasos * pesopa) + (munecas * pesomu)
print("El peso total del paquete que será enviado es:",total, "gramos")