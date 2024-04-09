import tkinter as tk
from tkinter import messagebox
from Persona import Persona

class InterfazLogin:
    def __init__(self, ventana, persona):
        self.ventana = ventana
        self.persona = persona
        self.ventana.title("Login")

        self.label_correo = tk.Label(ventana, text="Correo:")
        self.label_correo.pack()
        self.entry_correo = tk.Entry(ventana)
        self.entry_correo.pack()

        self.label_contraseña = tk.Label(ventana, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(ventana, show="*")
        self.entry_contraseña.pack()

        self.boton_login = tk.Button(ventana, text="Iniciar Sesión", command=self.validar_login)
        self.boton_login.pack()

    def validar_login(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()
        if self.persona.validar_usuario(correo, contraseña):
            messagebox.showinfo("¡Bienvenido!", "Inicio de sesión exitoso")
        else:
            messagebox.showerror("Error", "Usuario no encontrado o contraseña incorrecta")