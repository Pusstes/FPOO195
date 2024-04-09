import tkinter as tk
from tkinter import messagebox
from Crud import Crud

class ConsultaSaldo:
    def __init__(self,ventana,crud):
        self.ventana = ventana
        self.crud = crud
        self.ventana.title('Consulta de Saldo')
        self.ventana.geometry('800x500')
        
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
        info = 'Ingrese la cuenta de la que se quiere saber el saldo'
        self.labelInfo = tk.Label(ventana, text = info, font=fontStyleTitlle)
        self.labelInfo.pack()
        
        #label y input de la cuenta que se consultara el saldo
        self.labelCuenta = tk.Label(ventana, text = 'Cuenta a consultar el saldo: ', **labelStyle)
        self.labelCuenta.pack()
        
        self.entryCuenta = tk.Entry(ventana, **entryStyle)
        self.entryCuenta.pack()
        
        # boton para consultar el saldo
        self.botonConsultar = tk.Button(ventana, text = 'Consultar', command=self.consultarSaldo, **buttonStyle)
        self.botonConsultar.pack()
        
    def consultarSaldo(self):
        cuenta = self.entryCuenta.get()
        if cuenta == '':
            messagebox.showerror('Error', 'Falta ingresar la cuenta')
            return
        saldo = self.crud.getSaldo(cuenta)
        titular = self.crud.getNombreUsuario(cuenta)
        if saldo == None:
            messagebox.showerror('Error', 'No existe la cuenta')
            return
        messagebox.showinfo('Saldo', f'El saldo de la cuenta {cuenta}, que pertenece a: {titular}, es: {saldo}')
        
if __name__ == '__main__':
    ventana = tk.Tk()
    crud = Crud()
    cuenta = crud.crearUsuario('Juan', 20,100)
    app = ConsultaSaldo(ventana,crud)
    ventana.mainloop()