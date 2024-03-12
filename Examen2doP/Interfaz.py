import tkinter as tk
from tkinter import messagebox
from Persona import Persona

def generar_matricula():
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    año_nacimiento = int(entry_año_nacimiento.get())
    carrera = entry_carrera.get()

    persona = Persona(nombre, apellido_paterno, apellido_materno, año_nacimiento, carrera)
    matricula = persona.matricula()

    messagebox.showinfo("Matrícula Generada", f"La matrícula generada es: {matricula}")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Generador de Matrícula")

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido_paterno = tk.Label(root, text="Apellido Paterno:")
label_apellido_paterno.pack()
entry_apellido_paterno = tk.Entry(root)
entry_apellido_paterno.pack()

label_apellido_materno = tk.Label(root, text="Apellido Materno:")
label_apellido_materno.pack()
entry_apellido_materno = tk.Entry(root)
entry_apellido_materno.pack()

label_año_nacimiento = tk.Label(root, text="Año de Nacimiento:")
label_año_nacimiento.pack()
entry_año_nacimiento = tk.Entry(root)
entry_año_nacimiento.pack()

label_carrera = tk.Label(root, text="Carrera:")
label_carrera.pack()
entry_carrera = tk.Entry(root)
entry_carrera.pack()

btn_generar = tk.Button(root, text="Generar Matrícula", command=generar_matricula)
btn_generar.pack()

root.mainloop()
