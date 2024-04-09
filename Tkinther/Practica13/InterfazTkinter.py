import tkinter as tk
from random import sample
from Password import Password

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de Contraseñas")
        
        self.label_length = tk.Label(master, text="Longitud:")
        self.label_length.grid(row=0, column=0, padx=10, pady=10)

        self.entry_length = tk.Entry(master)
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)
        self.entry_length.insert(0, "8")  # Valor predeterminado
        
        self.label_option = tk.Label(master, text="Opción (1, 2, 3 o 4):")
        self.label_option.grid(row=1, column=0, padx=10, pady=10)
        
        self.entry_option = tk.Entry(master)
        self.entry_option.grid(row=1, column=1, padx=10, pady=10)

        self.label_option_info = tk.Label(master, text="(1) Letras + Números, (2) Letras + Números + Mayúsculas, (3) Letras + Números + Caracteres especiales, (4) Letras + Mayúsculas + Números + Caracteres especiales")
        self.label_option_info.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Generar Contraseña", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_frame = tk.Frame(master)
        self.result_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.result_entry = tk.Entry(self.result_frame, state='readonly')
        self.result_entry.pack(side=tk.LEFT)

        self.strength_label = tk.Label(self.result_frame, text="Fortaleza:")
        self.strength_label.pack(side=tk.LEFT, padx=(10, 0))

        self.strength_entry = tk.Entry(self.result_frame, state='readonly')
        self.strength_entry.pack(side=tk.LEFT)

    def generate_password(self):
        longitud_input = self.entry_length.get()
        if longitud_input.strip() == "":
            longitud = 8
        else:
            longitud = int(longitud_input)
        
        caracteres = int(self.entry_option.get())
        contase = Password(longitud)
        nueva_contrasena = contase.generadorPassword(caracteres)
        fortaleza = contase.comprobarFortaleza(nueva_contrasena)
        
        self.result_entry.config(state='normal')
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, nueva_contrasena)
        self.result_entry.config(state='readonly')

        self.strength_entry.config(state='normal')
        self.strength_entry.delete(0, tk.END)
        self.strength_entry.insert(0, fortaleza)
        self.strength_entry.config(state='readonly')
        

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
