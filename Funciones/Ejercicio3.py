# Escribir una función que convierta un número decimal en binario y
# otra que convierta un número binario en decimal.

def dec_a_binario(numero):
    binario = ""
    
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero //= 2
    
    return binario

def bin_a_dec(dig_binarios):
    decimal = 0
    for i in range(len(dig_binarios)):
        if dig_binarios[i] == '1':
            decimal += 2 ** (len(dig_binarios) - 1 - i)
    return decimal



opc = int(input('Ingresa que es lo que quieres hacer: \n 1:Decimal a binario. \n 2:Binario a decimal.\n Respuesta: '))

if opc == 1:
   numero = int(input('Ingresa el numero decimal que convertiremos a binario: '))
   numero_binario = dec_a_binario(numero)
   print(f"El numero decimal: '{numero}', equivale a: '{numero_binario}' en el sistema binario.")
   
elif opc == 2:
    numero = input('Ingresa el numero binario que deseas convertir a decimal: ')
    dig_binarios = list(numero)
    numero_decimal = bin_a_dec(dig_binarios)
    print(f"El numero binario: '{numero}', equivale a: '{numero_decimal}' en el sistema decimal.")

else:
    print('Esa no es una opcion valida.')
            
            