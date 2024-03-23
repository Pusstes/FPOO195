from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    
    def conexion(self):
        try:
            conexion = sqlite3.connect("C:/Users/ulqui/Desktop/UPQ/5to_cuatri/POO/FPOO195/TkSQLite/db195.db")
            print("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
            print("Error al abrir la base de datos")
           
    
    def encriptapass(self, cont):
        passPlana = cont
        passPlana = passPlana.encode() #convertir a bytes
        sal = bcrypt.gensalt() #generar sal
        passHash = bcrypt.hashpw(passPlana, sal) #encriptar contraseña
        return passHash
    
    def insertUsuario(self,nom,corr,cont):
        conexion = self.conexion()
        if (nom == "" or corr == "" or cont == ""):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            conexion.close()
            return
        else:
            cursor = conexion.cursor()
            conH = self.encriptapass(cont)
            datos = (nom, corr, conH)
            sqlInsert = "INSERT INTO tbUsuarios (nombre, correo, contra) VALUES (?,?,?)"
            cursor.execute(sqlInsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Éxito", "Usuario registrado")
            