class Persona:
    def __init__(self):
        self.__registros = []

    # Getter para obtener los registros
    def get_registros(self):
        return self.__registros

    # Método para agregar un nuevo usuario
    def crear_usuario(self,nombre, correo,contraseña):
        usuario = {
            "nombre": nombre,
            "correo": correo,
            "contraseña": contraseña,
        }
        self.__registros.append(usuario)
        print("Usuario creado exitosamente.")


    # Método para consultar todos los usuarios
    def consultar_usuarios(self):
        print("Lista de Usuarios:")
        for usuario in self.__registros:
            print(" Nombre: {}, Correo: {}, Contraseña: {}".format(
                usuario["nombre"], usuario["correo"], usuario["contraseña"]))

    #Metodo para validar si el usuario esta registrado
    def validar_usuario(self, correo, contraseña):
            for usuario in self.__registros:
                if usuario["correo"] == correo and usuario["contraseña"] == contraseña:
                    print("Usuario validado exitosamente.")
                    return True
            print("Usuario no encontrado o contraseña incorrecta.")
            return False
