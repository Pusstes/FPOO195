# Programa que pide al usuario dos palabras, se indicara cual 
# es mas larga y por cuanto lo es.

print('Ingresaras dos palabras y te indicare cual es mas larga y por cuantas letras lo es.')
palabra1 = input('Ingresa la primer palabra: ')
palabra2 = input('Ingresa la segunda palabra: ')

len(palabra1)
len(palabra2)



if len(palabra1) > len(palabra2):
    resta = len(palabra1) - len(palabra2)
    print( 'La palabra: ' + palabra1 +' Tiene: ' + str(resta) + " letras mas que la palabra 2")
    
elif len(palabra2) > len(palabra1):
    resta = len(palabra2) - len(palabra1)
    print( 'La palabra: ' + palabra2 +' Tiene: ' + str(resta) + " letras mas que la palabra 1")

else:
    print("La palabra: " + palabra1 + " y la palabra: " + palabra2 + " Son iguales")
    
    
    