from tkinter import messagebox
import sqlite3 #importar la librería de sqlite
import bcrypt #esta importación es para encriptar la contraseña

class Controlador:
    #método para abrir la conexión a la base de datos
    def conexion(self):
        try:
            conexion = sqlite3.connect("C:/Users/ulqui/Desktop/UPQ/5to_cuatri/POO/FPOO195/TkSQLite/DB195bien.db") #ruta de la base de datos
            print("Conexión exitosa") #mensaje de éxito
            return conexion
        except sqlite3.OperationalError:
            print("Error al abrir la base de datos")
           
    #método para encriptar la contraseña
    def encriptapass(self, cont):
        passPlana = cont
        passPlana = passPlana.encode() #convertir a bytes
        sal = bcrypt.gensalt() #generar sal
        passHash = bcrypt.hashpw(passPlana, sal) #encriptar contraseña
        return passHash #regresar la contraseña encriptada
    
    #método para insertar un usuario
    def insertUsuario(self,nom,corr,cont):
        conexion = self.conexion() #abrir la conexión
        if (nom == "" or corr == "" or cont == ""): #validar que los campos no estén vacíos
            messagebox.showerror("Error", "Todos los campos son obligatorios") #mensaje de error
            conexion.close() #cerrar la conexión
            return #salir del método
        else: #si los campos no están vacíos
            cursor = conexion.cursor() #crear un cursor que permita ejecutar sentencias sql
            conH = self.encriptapass(cont) #encriptar la contraseña
            datos = (nom, corr, conH) #almacenar los datos en una tupla
            sqlInsert = "INSERT INTO tbUsuarios (nombre, correo, contra) VALUES (?,?,?)" #sentencia sql para insertar un usuario
            cursor.execute(sqlInsert, datos) #ejecutar la sentencia sql
            conexion.commit() #confirmar la transacción
            conexion.close() #cerrar la conexión
            messagebox.showinfo("Éxito", "Usuario registrado") #mensaje de éxito
            
    #método para buscar un usuario
    def buscarUsuario(self, id):
        conexion = self.conexion()
        print(id)
        if (id == ""):
            messagebox.showerror("Error", "El campo es obligatorio")
            conexion.close()
            return None
        else:
            try:
                gerry = conexion.cursor()
                sqlSelect = 'SELECT * FROM tbUsuarios WHERE id = ?'
                gerry.execute(sqlSelect,(int(id),))
                usuario = gerry.fetchall()
                conexion.close()
                return usuario
            except sqlite3.OperationalError as e:
                print("Error al buscar el usuario", e)
                return None
            
    #método para consultar todos los usuarios
    def obtenerUsuarios(self):
        conexion = self.conexion()
        try:
            gerry = conexion.cursor()
            sqlSelect = 'SELECT * FROM tbUsuarios'
            gerry.execute(sqlSelect)
            usuarios = gerry.fetchall()
            conexion.close()
            return usuarios
        except sqlite3.OperationalError as e:
            print("Error al buscar los usuarios", e)
            return None
        
    #metodo para actualizar un usuario
    def actualizarUsuario(self,id,campo,valor):
        conexion = self.conexion()
        try: #manejo de excepciones
            cursor = conexion.cursor() #crear un cursor
            if campo == "nombre": #validar el campo a actualizar
                sqlUpdate = "UPDATE tbUsuarios SET nombre = ? WHERE id = ?" #sentencia sql para actualizar el nombre
            elif campo == "correo":
                sqlUpdate = "UPDATE tbUsuarios SET correo = ? WHERE id = ?"
            elif campo == "contra":
                sqlUpdate = "UPDATE tbUsuarios SET contra = ? WHERE id = ?"
            else:
                messagebox.showerror("Error", "Campo no válido")
                conexion.close()
                return
            cursor.execute(sqlUpdate,(valor,int(id))) #ejecutar la sentencia sql
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario actualizado")
        except sqlite3.OperationalError as e:
            print("Error al actualizar el usuario", e)