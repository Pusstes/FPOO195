# for
palabra = str(input('Ingresa una palabra: '))
contador_vocales = 0
for letra in palabra:
    if letra.lower() in 'eiou':
        contador_vocales += 1
print(f"la palabra '{palabra}' tiene {contador_vocales} vocal(es).")
        