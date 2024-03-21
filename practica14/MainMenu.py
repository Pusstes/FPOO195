import tkinter as tk
from tkinter import messagebox
from Crud import Crud
from ConsultaSaldo import ConsultaSaldo
from CrearUsuario import CrearUsuario
from Deposito import Deposito
from Retiro import Retiro
from Transferencia import Transferencia

class MainMenu:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title('Menú Principal.')
        self.ventana.geometry('800x500')

        self.crud = Crud()
        # diseño de las cosas de La ventana
        # diseño de las letras que se ocuparán en la ventana
        fontStyleTitlle = ('Arial', 20, 'bold')


        # Estilo del botón
        buttonStyle = {'font': ('Arial', 12, 'bold'), 'bg': 'green', 'fg': 'white'}

        # mensaje que se mostrara en la ventana
        info = 'Menú Principal. \nBanco nacional de Gerardo Mx'
        self.labelInfo = tk.Label(ventana, text = info, font=fontStyleTitlle)
        self.labelInfo.pack()

       # boton para crear un usuario
        self.botonCrearUsuario = tk.Button(ventana, text = 'Crear Usuario', command=self.crearUsuario, **buttonStyle)
        self.botonCrearUsuario.pack(pady=10)

        # boton para consultar el saldo
        self.botonConsultar = tk.Button(ventana, text = 'Consultar Saldo', command=self.consultarSaldo, **buttonStyle)
        self.botonConsultar.pack(pady=10)

        # boton para depositar
        self.botonDepositar = tk.Button(ventana, text = 'Depositar', command=self.depositar, **buttonStyle)
        self.botonDepositar.pack(pady=10)

        # boton para retirar
        self.botonRetirar = tk.Button(ventana, text = 'Retirar', command=self.retirar, **buttonStyle)
        self.botonRetirar.pack(pady=10)

        #boton para transferir
        self.botonTransferir = tk.Button(ventana, text = 'Transferir', command=self.transferir, **buttonStyle)
        self.botonTransferir.pack(pady=10)

        # boton para visualizar cuentas
        self.botonVisualizarCuentas = tk.Button(ventana, text = 'Visualizar Cuentas', command=self.visualizarCuentas, **buttonStyle)
        self.botonVisualizarCuentas.pack(pady=10)

    def consultarSaldo(self):
        ventana = tk.Toplevel(self.ventana)
        app = ConsultaSaldo(ventana,self.crud)

    def crearUsuario(self):
        ventana = tk.Toplevel(self.ventana)
        app = CrearUsuario(ventana,self.crud)

    def depositar(self):
        ventana = tk.Toplevel(self.ventana)
        app = Deposito(ventana,self.crud)

    def retirar(self):
        ventana = tk.Toplevel(self.ventana)
        app = Retiro(ventana,self.crud)

    def transferir(self):
        ventana = tk.Toplevel(self.ventana)
        app = Transferencia(ventana,self.crud)

    def visualizarCuentas(self):
        cuentas = self.crud.consultarCuentas()
        cuentasStr = "\n".join(cuentas)
        messagebox.showinfo('Cuentas registradas:', f"Cuenats registras:\n{cuentasStr}")
        
if __name__ == '__main__':
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()