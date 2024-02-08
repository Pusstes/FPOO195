# Funciones que permitan hacer la convercion de temperaturas

def centigrados_a_fahrenheit(centigrados):
    return centigrados * 9 / 5 + 32

def fahrenheit_a_centigrados(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def centigrados_a_kelvin(centigrados):
    return centigrados + 273.15

opc = int(input('Elege la opcion que desees: \n1. Centigrados a fahrenheit.\n2.Fahrenheit a centigrados.\n3.Centigrados a kelvin.\nOpcion: '))

if opc == 1:
    temperatura = float(input('Ingrese la temperatura en centigrados: '))
    print(f'La temperatura en fahrenheit es: {centigrados_a_fahrenheit(temperatura)}')
    
elif opc == 2:
    temperatura = float(input('Ingrese la temperatura en fahrenheit: '))
    print(f'La temperatura en centigrados es: {fahrenheit_a_centigrados(temperatura)}')
    
elif opc == 3:
    temperatura = float(input('Ingrese la temperatura en centigrados: '))
    print(f'La temperatura en kelvin es:{centigrados_a_kelvin(temperatura)}')
