import tkinter as tk
from random import sample

class Password:
    def __init__(self, longitud=8):
        self.longitud = longitud

    def generadorPassword(self, opc):
        letras = 'abcdefghijklmnñopqrstuvwxyz'
        letUp = letras.upper()
        numeros = '0123456789'
        simbolos = '''[]()+*-/;.,_%$#!¿?<>'''
        if opc == '1':
            todo = letras + numeros
            contra = sample(todo, self.longitud)
            contraresul = ''.join(contra)
            return contraresul
        elif opc == '2':
            todo = letras + letUp + numeros + simbolos
            contra = sample(todo, self.longitud)
            contraresul = ''.join(contra)
            return contraresul

    def comprobarFortaleza(self, contrasena, caracteres_permitidos, complejidad_caracteres):
        longitud = len(contrasena)
        contiene_minusculas = any(c.islower() for c in contrasena)
        contiene_mayusculas = any(c.isupper() for c in contrasena)
        contiene_numeros = any(c.isdigit() for c in contrasena)
        contiene_especiales = any(c in caracteres_permitidos for c in contrasena)
        if longitud < 8 or complejidad_caracteres < 3:
            return "Débil"
        elif (longitud >= 8 and longitud < 12) or (complejidad_caracteres >= 3 and (contiene_minusculas or contiene_mayusculas or contiene_numeros)):
            return "Media"
        elif (longitud >= 12 and longitud < 16) or (complejidad_caracteres >= 3 and (contiene_minusculas and contiene_mayusculas and contiene_numeros and contiene_especiales)):
            return "Fuerte"
        else:
            return "Muy Fuerte"