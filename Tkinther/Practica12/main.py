from Persona import Persona

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Crear Usuario")
    print("2. Consultar Usuarios")
    print("3. Mostrar Interfaz de Login")
    print("4. Salir")

def main():
    crud = Persona()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contraseña = input("Contraseña:")
            crud.crear_usuario(nombre, correo, contraseña)  
        elif opcion == "2":
            crud.consultar_usuarios()  
        elif opcion == "3":
            import tkinter as tk
            from InterfazLogin import InterfazLogin
            ventana = tk.Tk()
            interfaz = InterfazLogin(ventana, crud)
            ventana.mainloop()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()