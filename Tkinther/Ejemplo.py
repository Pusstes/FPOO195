from tkinter import Tk, Frame

# crear la ventana

ventana = Tk() 
ventana.title('Ejemplo con 3 frames')
ventana.geometry('600x400')

# secciones
seccion1 = Frame(ventana, bg='red')
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(ventana, bg='black')
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(ventana, bg='yellow')
seccion3.pack(expand=True, fill='both')

# darle visivilidad a las secciones

ventana.mainloop()