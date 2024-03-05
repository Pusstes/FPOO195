from tkinter import Tk, Frame, Button, messagebox

# metodos para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('Ventana de informacion','Hola esta es la informacion'))
    print(messagebox.showerror('Error','Hiciste algo mal'))
    print(messagebox.showwarning('Alerta','Cuidado alfggo esta mal'))
    print(messagebox.askokcancel('¿Quieres cancelar?','Neta'))

# metodo para modificar el boton y crear mas
def addbtn():
    botonVerde.config(text='+') #cambiaremos el texto del boton, originalmente tiene 'verde', se cambiara a '+'
    # creacion del boton nuevo
    botonRosa = Button(seccion3, text='nuevo', bg='pink', fg='black')
    botonRosa.configure(height=3,width=5)
    botonRosa.pack()
    

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

#agregar botones
botonAzul = Button(seccion1, text='Azul', bg='blue', fg='white')
#tenemos la seccion donde estara el boton, bg = color de fondo fg= color de letra
# posicionar el boton
botonAzul.place(x=1000, y=100, width=100, height=30)

# grid
botonNegro = Button(seccion2, text='Negro', bg='black', fg='white')
botonNegro.configure(height=2,width=10)
botonNegro.grid(row=0,column=0)

botonAmarillo = Button(seccion2,text='Amarillo',bg='yellow',fg='red',command=mostrarMensajes)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1,column=0)

# pack
botonVerde = Button(seccion3, text='verde', bg='green', fg='black', command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()

botonVerde2 = Button(seccion3, text='verde', bg='green', fg='black')
botonVerde2.configure(height=2,width=10)
botonVerde2.pack()


ventana.mainloop()