# esta forma es para importar todo lo que tiene el archivo
# en este caso el archivo se llama 'Personaje', tambien la clase

from Personaje import *
from Armas import *

#solicitar datos del spartan:
nombreS = input('Escribe el nombre de tu Spartan:\n ')
especieS = input('Escribe la Especie de tu Spartan:\n')
alturaS = float(input('Ingresa la altura de tu Spartan:\n '))

# Solicitar datos del nemesis
print("")
nombreN = input('Escribe el nombre de tu Nemesis:\n ')
especieN = input('Escribe la Especie de tu Nemesis:\n')
alturaN = float(input('Ingresa la altura de tu Nemesis:\n '))

spartan = Personaje(especieS,nombreS,alturaS)
nemesis = Personaje(especieN,nombreN,alturaN)
Arma = Armas()

# atributos Spartan
print("")
print('===== Datos del Spartan ======')
print(spartan.get_nombre())
print(spartan.get_especie())
print(spartan.get_altura())
print("")

# atributos nemesis 
print('===== Datos del villano ======')
print(nemesis.get_nombre())
print(nemesis.get_especie())
print(nemesis.get_altura())
print("")

# Metodos del spartan
print('===== Metodos del Objeto Spartan =====')
spartan.correr(False)
spartan.lanzarGranada()
print("")

# Metodos del Nemesis
print('===== Metodos del Objeto Nemesis =====')
nemesis.correr(True)
nemesis.lanzarGranada()
print("")

# Metodos del arma
Arma.seleccionarArma(spartan.get_nombre())
Arma.recargarArma(65)




