from random import sample

class Password:
    def __init__(self, longitud=8):
        self.longitud = longitud
        self.simbolos = '''[]()+*-/;.,_%$#!¿?<>'''  

    def generadorPassword(self, opc):
        letras = 'abcdefghijklmnñopqrstuvwxyz'
        letUp = letras.upper()
        numeros = '0123456789'
        
        if opc == 1:  
            todo = letras + numeros
            contra = sample(todo, self.longitud)
            contraresul = ''.join(contra)
            return contraresul
        elif opc == 2:  
            todo = letras + letUp + numeros
            contra = sample(todo, self.longitud)
            contraresul = ''.join(contra)
            return contraresul
        elif opc == 3:  
            todo = letras + numeros + self.simbolos
            contra = sample(todo, self.longitud)
            contraresul = ''.join(contra)
            return contraresul
        elif opc == 4:  
            todo = letras + letUp + numeros + self.simbolos
            contra = sample(todo, self.longitud)
            contraresul = ''.join(contra)
            return contraresul
        else:
            return "Opción no válida"

    def comprobarFortaleza(self, contrasena):
        longitud = len(contrasena)
        contiene_minusculas = any(c.islower() for c in contrasena)
        contiene_mayusculas = any(c.isupper() for c in contrasena)
        contiene_numeros = any(c.isdigit() for c in contrasena)
        contiene_especiales = any(c in self.simbolos for c in contrasena)

        complejidad_caracteres = sum([contiene_minusculas, contiene_mayusculas, contiene_numeros, contiene_especiales])
        if longitud < 8 or complejidad_caracteres < 3:
            return "Débil"
        elif (longitud >= 8 and longitud < 12) or (complejidad_caracteres >= 3 and (contiene_minusculas or contiene_mayusculas or contiene_numeros)):
            return "Media"
        elif (longitud >= 12 and longitud < 16) or (complejidad_caracteres >= 3 and (contiene_minusculas and contiene_mayusculas and contiene_numeros and contiene_especiales)):
            return "Fuerte"
        else:
            return "Muy Fuerte"


# longitud = int(input('Longitud: '))
# contase = Password(longitud)
# caracteres = int(input('Opción (1, 2, 3 o 4): '))  # Convertir la entrada a un entero
# nueva_contrasena = contase.generadorPassword(caracteres)
# print("Nueva contraseña generada:", nueva_contrasena)
# fortaleza = contase.comprobarFortaleza(nueva_contrasena, longitud, caracteres)
# print("Fortaleza de la contraseña:", fortaleza)
