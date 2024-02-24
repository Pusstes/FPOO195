# esta forma es para importar todo lo que tiene el archivo
# en este caso el archivo se llama 'Personaje', tambien la clase

from Personaje import *
from Armas import *

spartan = Personaje()
Arma = Armas()

print(spartan.altura)
print(spartan.especie) 
print(spartan.nombre)         
spartan.correr(False)
spartan.lanzarGranada()
Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(10)
