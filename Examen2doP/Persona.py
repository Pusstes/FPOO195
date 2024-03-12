# Programa con interfaz y clase en archivos propios que solicite Nombre, apellido paterno,
# apellido materno, año de nacimiento y carrera.
#Con los datos generados se generara una amtricula con las caracteristicas: 2 digitos del año en curso
#2 digitos del año de nacimiento, primera letra del nombre, 3 letras de cada apellido, 3 digitos aleatorios y 3 letras de la carrera
#Mostrar la matricula en un message box

import random

class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera):
        self.__nom = nombre
        self.__apeP = apellido_paterno
        self.__apeM = apellido_materno
        self.__aN = str(anio_nacimiento)  # Convertir a cadena de texto
        self.__carr = carrera

    def getNombre(self):
        return self.__nom

    def getApePa(self):
        return self.__apeP

    def getApeMa(self):
        return self.__apeM

    def getAnN(self):
        return self.__aN

    def getCarrera(self):
        return self.__carr

    def matricula(self):
        carre3 = self.__carr[:3]
        digAc = '24'
        anN2 = self.__aN[-2:]
        letnom = self.__nom[0]
        letapeP = self.__apeP[:3]
        letapeM = self.__apeM[:3]
        dig = str(random.randrange(100, 998, 10))
        matricula = carre3 + digAc + anN2 + letnom + letapeP + letapeM + dig
        return matricula
    
    
# nombre = input('nombre')
# apellido_paterno = input('apep')
# apellido_materno = input('ape materno')
# anio_nacimiento = input('anio')
# carrera = input('carrera')
    
# obj = Persona(nombre,apellido_paterno,apellido_materno,anio_nacimiento,carrera)
# obj.matricula()
