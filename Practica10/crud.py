class Crud:
    def __init__(self):
        self.__registros = []

    # Getter para obtener los registros
    def get_registros(self):
        return self.__registros

    # Método para agregar un nuevo usuario
    def crear_usuario(self, id, nombre, correo, telefono, sexo, edad):
        usuario = {
            "id": id,
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
            "sexo": sexo,
            "edad": edad
        }
        self.__registros.append(usuario)
        print("Usuario creado exitosamente.")

    # Método para borrar un usuario por su id
    def borrar_usuario(self, id):
        for usuario in self.__registros:
            if usuario["id"] == id:
                self.__registros.remove(usuario)
                print("Usuario con ID {} ha sido borrado.".format(id))
                return
        print("Usuario con ID {} no encontrado.".format(id))

    # Método para consultar todos los usuarios
    def consultar_usuarios(self):
        print("Lista de Usuarios:")
        for usuario in self.__registros:
            print("ID: {}, Nombre: {}, Correo: {}, Teléfono: {}, Sexo: {}, Edad: {}".format(
                usuario["id"], usuario["nombre"], usuario["correo"], usuario["telefono"], usuario["sexo"], usuario["edad"]))

    # Método para actualizar un usuario por su id
    def actualizar_usuario(self, id):
        for usuario in self.__registros:
            if usuario["id"] == id:
                print("Selecciona qué dato del usuario con ID {} quieres actualizar:".format(id))
                print("1. Nombre")
                print("2. Correo")
                print("3. Teléfono")
                print("4. Sexo")
                print("5. Edad")
                opcion = input("Opción: ")
                if opcion == "1":
                    nuevo_nombre = input("Nuevo nombre: ")
                    usuario["nombre"] = nuevo_nombre
                elif opcion == "2":
                    nuevo_correo = input("Nuevo correo: ")
                    usuario["correo"] = nuevo_correo
                elif opcion == "3":
                    nuevo_telefono = input("Nuevo teléfono: ")
                    usuario["telefono"] = nuevo_telefono
                elif opcion == "4":
                    nuevo_sexo = input("Nuevo sexo: ")
                    usuario["sexo"] = nuevo_sexo
                elif opcion == "5":
                    nueva_edad = input("Nueva edad: ")
                    usuario["edad"] = nueva_edad
                else:
                    print("Opción no válida.")
                print("Usuario actualizado exitosamente.")
                return
        print("Usuario con ID {} no encontrado.".format(id))
