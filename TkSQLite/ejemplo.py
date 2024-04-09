import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Actualizar Usuario")
        
        # Frame para el input del ID y el botón de buscar
        self.frame_buscar = tk.Frame(self.root)
        self.frame_buscar.pack(pady=20)
        
        self.label_id = tk.Label(self.frame_buscar, text="ID del Usuario:")
        self.label_id.pack(side=tk.LEFT, padx=10)
        
        self.entry_id = tk.Entry(self.frame_buscar, width=30)
        self.entry_id.pack(side=tk.LEFT, padx=10)
        
        self.btn_buscar = tk.Button(self.frame_buscar, text="Buscar", command=self.buscar_usuario)
        self.btn_buscar.pack(side=tk.LEFT, padx=10)
        
        # Variables para guardar la información del usuario encontrado
        self.nombre = tk.StringVar()
        self.correo = tk.StringVar()
        self.contraseña = tk.StringVar()
        
        # Frame para los Checkbuttons
        self.frame_check = tk.Frame(self.root)
        
        self.check_nombre = tk.Checkbutton(self.frame_check, text="Nombre", variable=self.nombre, onvalue="nombre", offvalue="")
        self.check_nombre.pack(side=tk.LEFT, padx=10)
        
        self.check_correo = tk.Checkbutton(self.frame_check, text="Correo", variable=self.correo, onvalue="correo", offvalue="")
        self.check_correo.pack(side=tk.LEFT, padx=10)
        
        self.check_contraseña = tk.Checkbutton(self.frame_check, text="Contraseña", variable=self.contraseña, onvalue="contraseña", offvalue="")
        self.check_contraseña.pack(side=tk.LEFT, padx=10)
        
        # Frame para los inputs adicionales
        self.frame_inputs = tk.Frame(self.root)
        
        self.entry_nuevo_nombre = tk.Entry(self.frame_inputs, width=30)
        self.entry_nuevo_correo = tk.Entry(self.frame_inputs, width=30)
        self.entry_nuevo_contraseña = tk.Entry(self.frame_inputs, width=30)
        
        # Botón para actualizar
        self.btn_actualizar = tk.Button(self.root, text="Actualizar", command=self.actualizar_usuario, state=tk.DISABLED)
        self.btn_actualizar.pack(pady=20)
        
    def buscar_usuario(self):
        # Aquí deberías implementar la lógica para buscar el usuario en tu base de datos
        # Por ahora, simplemente estableceré los valores de los inputs para mostrar el ejemplo
        id_usuario = self.entry_id.get()
        
        if id_usuario == "1":  # Suponiendo que el usuario con ID 1 existe
            self.frame_check.pack(pady=20)
            self.btn_actualizar.config(state=tk.NORMAL)
            
            # Aquí deberías obtener los datos del usuario y establecerlos en los inputs
            # Por ahora, simplemente estableceré valores de ejemplo
            self.entry_nuevo_nombre.insert(0, "Nuevo Nombre")
            self.entry_nuevo_correo.insert(0, "nuevo@correo.com")
            self.entry_nuevo_contraseña.insert(0, "nueva_contraseña")
            
        else:
            messagebox.showwarning("Alerta", "Usuario no encontrado.")
            
    def actualizar_usuario(self):
        # Aquí deberías implementar la lógica para actualizar el usuario en tu base de datos
        # Por ahora, simplemente mostraré un mensaje de éxito
        mensaje = "Actualización exitosa.\n"
        
        if self.nombre.get():
            mensaje += f"Nuevo nombre: {self.entry_nuevo_nombre.get()}\n"
        
        if self.correo.get():
            mensaje += f"Nuevo correo: {self.entry_nuevo_correo.get()}\n"
            
        if self.contraseña.get():
            mensaje += "Contraseña actualizada"
        
        messagebox.showinfo("Información", mensaje)

root = tk.Tk()
app = App(root)
root.mainloop()
