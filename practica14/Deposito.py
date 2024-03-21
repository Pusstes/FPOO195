import tkinter as tk
from tkinter import messagebox
from Crud import Crud

class Deposito:
    def __init__(self,ventana,crud):
        self.ventana = ventana
        self.crud = crud
        self.ventana.title('Deposito')
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
        info = 'Ingrese la cuenta a la que depositara y el monto a depositar'
        self.labelInfo = tk.Label(ventana, text = info, font=fontStyleTitlle)
        self.labelInfo.pack()
        
        # label y iunput de la cuenta a la que se hara el deposito
        self.labelCuenta = tk.Label(ventana, text = 'Cuenta a la que se hara el deposito: ', **labelStyle)
        self.labelCuenta.pack()
        
        self.entryCuenta = tk.Entry(ventana, **entryStyle)
        self.entryCuenta.pack()
        
        #label y input del monto a depositar
        self.labelMonto = tk.Label(ventana, text = 'Monto a depositar: ', **labelStyle)
        self.labelMonto.pack()
        
        self.entryMonto = tk.Entry(ventana, **entryStyle)
        self.entryMonto.pack()
        
        # boton para depositar
        self.botonDepositar = tk.Button(ventana, text = 'Depositar', command=self.depositar, **buttonStyle)
        self.botonDepositar.pack()
        
    def depositar(self):
        cuenta = self.entryCuenta.get()
        monto_text = self.entryMonto.get()
        
        if cuenta == '' or monto_text == '':
            messagebox.showerror('Error', 'Faltan datos por ingresar')
            return

        try:
            monto = float(monto_text)
        except ValueError:
            messagebox.showerror('Error', 'El monto debe ser un número válido')
            return
        if monto <= 0:
            messagebox.showerror('Error', 'El monto a depositar debe ser mayor a 0')
            return
        
        existenciaCuenta = self.crud.buscarUsuarioPorCuenta(cuenta)
        if existenciaCuenta is None:
            messagebox.showerror('Error', 'La cuenta no existe')
            return

        self.crud.ingresarEfectivo(cuenta, monto)
        saldoActual = self.crud.getSaldo(cuenta)
        titular = self.crud.getNombreUsuario(cuenta)
        mensajeDeposito = f'Se ha depositado el monto de {monto} a la cuenta {cuenta}. El nuevo saldo es: {saldoActual}\n\n'
        mensajeDeposito += f'El propietario de la cuenta es: {titular}'
        messagebox.showinfo('Depósito', mensajeDeposito)

        # Limpiamos los campos
        self.entryCuenta.delete(0, tk.END)
        self.entryMonto.delete(0, tk.END)
        self.entryCuenta.focus_set()

if __name__ == '__main__':
    ventana = tk.Tk()
    crud = Crud()
    cuenta = crud.crearUsuario('Juan', 25, 1000.26)
    app = Deposito(ventana,crud)
    ventana.mainloop()