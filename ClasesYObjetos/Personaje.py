class Personaje:
    
    # atributos
    def __init__(self,esp,nom,alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt
    # metodos   
    def correr(self, estado):
        if(estado):
            print("El personaje " + self.nombre + " esta corriendo")
        else:
            print("El personaje " + self.nombre + " esta muerto :´(" )
            
    def lanzarGranada(self):
        print(self.nombre + " lanzo una granada.")
