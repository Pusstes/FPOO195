altura = int(input("Ingrese la cantidad de asteriscos de la base del árbol: "))
altura_actual = 0


while altura_actual <= altura:
    
    espacios = altura - altura_actual
    print(" " * espacios, end="")


    asteriscos = altura_actual * 2 - 1
    print("*" * asteriscos)

   
    altura_actual += 1
