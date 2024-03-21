from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x500")

# Crear el panel de pestañas
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

# Crear el panel de pestañas
pestana1 = ttk.Frame(ventana)
pestana2 = ttk.Frame(ventana)
pestana3 = ttk.Frame(ventana)
pestana4 = ttk.Frame(ventana)
pestana5 = ttk.Frame(ventana)

# Añadir el panel de pestañas
panel.add(pestana1, text='Crear Usuario')
panel.add(pestana2, text='Buscar Usuario')
panel.add(pestana3, text='ConsultarUsuarios')
panel.add(pestana4, text='Actualizar Usuario')
panel.add(pestana5, text='Eliminar Usuario')


#pestaña 1: Formulario para crear un usuario
Label(pestana1, text="Registro de usuarios",fg="blue", font=("modern",18)).pack()

var1 = tk.StringVar()
Label(pestana1, text="Nombre:").pack()
Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(pestana1, text="Email:").pack()   
Entry(pestana1, textvariable=var2).pack()  

var3 = tk.StringVar()
Label(pestana1, text="Contraseña:").pack()  
Entry(pestana1, textvariable=var3).pack()

    


ventana.mainloop()




