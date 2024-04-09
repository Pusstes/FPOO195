import tkinter as tk
from tkinter import messagebox
from Crud import Crud

class CrearUsuario:
    def __init__(self, ventana,crud):
        self.vetana = ventana
        self.crud = crud
        self.vetana.title('Crear Usuario')
        self.vetana.geometry('800x500')

        # diseño de las cosas de La ventana
        
        # diseño de las letras que se ocuparán en la ventana
        fontStyleTitlle = ('Arial', 20, 'bold')

        # Estilo de los labels
        fontStyleText = ('Arial', 12)
        labelStyle = {'font': fontStyleText, 'fg': 'blue'}

        # Estilo de los inputs
        entryStyle = {'font': fontStyleText, 'fg': 'black'}

        # Estilo del botón
        buttonStyle = {'font': ('Arial', 12, 'bold'), 'bg': 'green', 'fg': 'white'}

        # mensaje que se mostrara en la ventana
        info = 'Ingrese los datos del propietario de la cuenta a crear'
        self.labelInfo = tk.Label(ventana, text = info, font=fontStyleTitlle)
        self.labelInfo.pack()

        # label y iunput del nombre del propietario
        # '**' es para desempaquetar el diccionario y mandar los valores como argumentos
        self.labelNombre = tk.Label(ventana, text = 'Nombre Completo del propietario que se creara la cuenta : ', **labelStyle)
        self.labelNombre.pack()

        self.entryNombre = tk.Entry(ventana, **entryStyle)
        self.entryNombre.pack()

        # label y input de la edad del propietario
        self.labelEdad = tk.Label(ventana, text = 'Edad del propietario: ', **labelStyle)
        self.labelEdad.pack()

        self.entryEdad = tk.Entry(ventana, **entryStyle)
        self.entryEdad.pack()

        # boton para crear el usuario
        self.botonCrear = tk.Button(ventana, text = 'Crear Usuario', command=self.crearUsuario, **buttonStyle)
        self.botonCrear.pack()
        
    def crearUsuario(self):
        nombre = self.entryNombre.get()
        edad = self.entryEdad.get()
        if nombre == '' or edad == '':
            messagebox.showerror('Error', 'Faltan datos por ingresar')
            return
        
        # usamos el metodo crearUsuario y metemos los valores de retorno en cuenta, saldo que es lo que retorna
        cuenta,saldo = self.crud.crearUsuario(nombre, edad)
        mensajeRegistro = f'Se ha registrado el usuario con los siguientes datos:\n\n'
        mensajeRegistro += f'Nombre: {nombre}\n'
        mensajeRegistro += f'No. Cuenta: {cuenta}\n'
        mensajeRegistro += f'Edad: {edad} años\n'
        mensajeRegistro += f'Saldo: {saldo}\n'
        messagebox.showinfo('Exito', mensajeRegistro)
        
        # limpiamos los campos de texto
        self.entryNombre.delete(0, tk.END)
        self.entryEdad.delete(0, tk.END)
        self.entryNombre.focus_set()
       
# linea de codigo que evitara que se ejecute el codigo si se importa a otro archivo 
if __name__ == '__main__':
    ventana = tk.Tk()
    crud = Crud()
    app = CrearUsuario(ventana,crud)
    ventana.mainloop()