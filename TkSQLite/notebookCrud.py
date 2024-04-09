from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from Controlador import *
from GeneradorPDF import *
import os

objControlador = Controlador() #crear un objeto de la clase Controlador

def ejecutarInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get()) #llamar al método insertUsuario de la clase Controlador

def buscar():
    usuario = objControlador.buscarUsuario(varBus.get())
    if usuario is not None:
        resultadoBusqueda.delete('1.0', tk.END)  # Borra cualquier texto existente
        resultadoBusqueda.insert(tk.END, str(usuario))  # Inserta el resultado de la búsqueda
    else:
        messagebox.showinfo("Información", "No se encontró ningún usuario con ese ID")
        
def ejecutaPDF():
    if varRepo.get() == "":
        messagebox.showerror("Error", "El campo es obligatorio")
        return
    else:
        objPDF = GeneradorPDF()
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varRepo.get() + '.pdf')
        rutaPDF = 'C:/Users/ulqui/Desktop/UPQ/5to_cuatri/POO/FPOO195/TkSQLite'+ varRepo.get() + '.pdf'
        messagebox.showinfo("Éxito", "PDF generado en " + rutaPDF)
        os.system('start ' + rutaPDF)
        #os.startfile(varRepo.get() + '.pdf')
    
    
#creacion de la ventana
ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x500")

# Crear el panel de pestañas
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

# Crear las pestañas con el metodo frame
pestana1 = ttk.Frame(ventana)
pestana2 = ttk.Frame(ventana)
pestana3 = ttk.Frame(ventana)
pestana4 = ttk.Frame(ventana)
pestana5 = ttk.Frame(ventana)
pestana6 = ttk.Frame(ventana)

# Añadir las pestañas al panel con la propiedad add
panel.add(pestana1, text='Crear Usuario')
panel.add(pestana2, text='Buscar Usuario')
panel.add(pestana3, text='ConsultarUsuarios')
panel.add(pestana4, text='Actualizar Usuario')
panel.add(pestana5, text='Eliminar Usuario')
panel.add(pestana6, text='Reportes en PDF')   


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

boton = Button(pestana1, text="Guardar", bg="green", fg="white", command=ejecutarInsert)
boton.pack()

#pestaña2: Buscar usuario
Label(pestana2, text="Buscar usuario por ID",fg="blue", font=("modern",18)).pack() #etiqueta de título
varBus = tk.StringVar() #variable para almacenar el ID
Label(pestana2, text="Ingrese el ID").pack() #etiqueta para el campo de texto
Entry(pestana2, textvariable=varBus).pack() #campo de texto
Button(pestana2, text="Buscar", bg="green", fg="white",command=buscar).pack() #botón de búsqueda
Label(pestana2, text="Resultado de la búsqueda",fg="blue", font=("modern",18)).pack() #etiqueta de título
resultadoBusqueda = tk.Text(pestana2, height=5, width=70) #área de texto para mostrar el resultado
resultadoBusqueda.pack() #mostrar el área de texto

#pestaña 3: Consultar usuarios
Label(pestana3, text="Usuarios registrados",fg="blue", font=("modern",18)).pack()
from tkinter import ttk

# Crear el Treeview
tree = ttk.Treeview(pestana3, columns=('ID', 'Nombre', 'Correo'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Nombre', text='Nombre')
tree.heading('Correo', text='Correo')
tree.pack()

# Llenar el Treeview con datos
usuarios = objControlador.obtenerUsuarios()
for usuario in usuarios:
    tree.insert('', 'end', values=usuario)
    
#pestana 4: Actualizar usuario
Label(pestana4, text="Actualizar usuario",fg="blue", font=("modern",18)).pack() #etiqueta de título
varAct = tk.StringVar() #variable para almacenar el ID
Label(pestana4, text="Ingrese el ID").pack() #etiqueta para el campo de texto
Entry(pestana4, textvariable=varAct).pack() #campo de texto

#pestaña 6: Reportes en PDF
Label(pestana6, text="Reportes en PDF",fg="blue", font=("modern",18)).pack() #etiqueta de título
varRepo = tk.StringVar() #variable para almacenar el título del archivo
Label(pestana6, text="Escribe el titulo del archivo",fg="black", font=("modern",12)).pack() #etiqueta de título
Entry(pestana6, textvariable=varRepo).pack() #campo de texto
Button(pestana6, text="Generar PDF", bg="green", fg="white",command=ejecutaPDF).pack() #botón de búsqueda

ventana.mainloop()




