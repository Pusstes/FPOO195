from typing import Any


class Personaje:
    
    # atributos
    def __init__(self,esp,nom,alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
    # metodos   
    
    # Getter y Setter de nombre:
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    # Getter y seter de especie:    
    def get_especie(self):
        return self.__especie
    
    def set_especie(self, nueva_especie):
        self.__especie = nueva_especie
        
    # Getter y Setter altura:
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura_nueva):
        self.__altura = altura_nueva
        
    def correr(self, estado):
        if(estado):
            print("El personaje " + self.get_nombre() + " esta corriendo")
        else:
            print("El personaje " + self.get_nombre() + " esta muerto :´(" )
            
    def lanzarGranada(self):
        print(self.get_nombre() + " lanzo una granada.")
        
    def __pensar(self):
        print(self.__nombre + "Esta pensado")
