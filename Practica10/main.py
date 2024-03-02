from crud import *

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Crear Usuario")
    print("2. Borrar Usuario")
    print("3. Consultar Usuarios")
    print("4. Actualizar Usuario")
    print("5. Salir")

def main():
    crud = Crud()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            sexo = input("Sexo: ")
            edad = input("Edad: ")
            crud.crear_usuario(id, nombre, correo, telefono, sexo, edad)
        elif opcion == "2":
            id = input("ID del usuario a borrar: ")
            crud.borrar_usuario(id)
        elif opcion == "3":
            crud.consultar_usuarios()
        elif opcion == "4":
            id = input("ID del usuario a actualizar: ")
            crud.actualizar_usuario(id)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
            
if __name__ == "__main__":
    main()