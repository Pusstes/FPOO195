frase = str(input('Ingresa una frase: '))
letra = str(input('Ingresa una letra: '))
contador = 0
for char in frase:
    if char == letra:
        contador += 1
        
print(f"la letra: '{letra}' aparece {contador} veces en la frase que diste.")