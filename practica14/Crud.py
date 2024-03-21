import random

class Crud:
    def __init__(self):
        self.__usuarios = []
        
    #  metodo para generar una cuenta random al usuario   
    def generarCuenta(self):
        # join para unir los elementos generados de random choices k es el parametro siempre usaremos k
        cuenta = ''.join(random.choices('123456789', k=5))
        return cuenta
    
    # metodo para buscar que las cuentas no se repitan en la lista que tienen los diccionarios con los datos de usuario
    def buscarUsuarioPorCuenta(self,cuenta):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                return usuario['Titular']
        return None
    
    def getNombreUsuario(self,cuenta):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                return usuario['Titular']
        return None
    
    def getRegistros(self):
        return self.__usuarios
    
    def consultarCuentas(self):
        cuentas = []
        print('Lista de cuentas registradas:')
        for usuario in self.getRegistros():
            cuentastr = 'Cuenta: {}, Titular: {}, Edad: {}, Saldo: {}'.format(usuario['Cuenta'], usuario['Titular'],usuario['Edad'],usuario['Saldo'])
            print(cuentastr)
            cuentas.append(cuentastr)
        return cuentas
    
    def crearUsuario(self,titular,edad,saldo=0):
        cuenta = self.generarCuenta()
        # bucle que inpide que las cuentas se repitan, cada que se cree un usuario nuevo este buble busca en la lista que el usuario no tenga la cuenta que se
        # genero de manera random, si regresa un true la funcion significa que ya esta, si es false no existe.
        while self.buscarUsuarioPorCuenta(cuenta):
            cuenta = self.generarCuenta()
            
        usuario = {
            'Cuenta':cuenta,
            'Titular':titular,
            'Edad':int(edad),
            'Saldo':float(saldo)
        }
        self.__usuarios.append(usuario)
        print('El usuario con los datos: '+ str(usuario) + ' fue registrado')
        return cuenta,saldo
        
    def getSaldo(self,cuenta):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                print('El saldo de la cuenta es: ', usuario['Saldo'])
                return usuario['Saldo']
        return None
        
    def ingresarEfectivo(self,cuenta,monto):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                saldoActual = usuario['Saldo']
                nuevoSaldo = saldoActual + monto
                usuario['Saldo'] = nuevoSaldo
                print('Se ingeso un monto de: ', monto, 'de la cuenta: ',cuenta)
                print('El saldo anterio era de: ',saldoActual, 'El nuevo saldo es: ',nuevoSaldo)
                return
        print('No existe la cuenta')
        
    def retirarEfectivo(self,cuenta,monto):
        for usuario in self.__usuarios:
            if usuario['Cuenta'] == cuenta:
                if usuario['Saldo'] < monto:
                    print('El saldo de la cuenta: ',cuenta, 'no es suficiente para retirar')
                    return
                saldoActual = usuario['Saldo']
                nuevoSaldo = saldoActual - monto
                usuario['Saldo'] = nuevoSaldo
                print('Se retiro un monto de: ', monto, 'de la cuenta: ',cuenta)
                print('El saldo anterio era de: ',saldoActual, 'El nuevo saldo es: ',nuevoSaldo)
                return
            
        print('No existe la cuenta.')
            
    def transferencia(self,cuentaOrigen,cuentaDestino,monto):
                usuarioOrigen = None
                usuarioDestino = None
                # los asignamos como none para manejar bien las situaciones en las que no existen sus cuentas
                
                for usuario in self.__usuarios:
                    if usuario['Cuenta'] == cuentaOrigen:
                        usuarioOrigen = usuario
                    elif usuario['Cuenta'] == cuentaDestino:
                        usuarioDestino = usuario
                        
                # casos en los que la cuenta no se encontro usaremos el return para salir de la funcion
                if usuarioOrigen is None:
                    print('No se encointro la cuenta de origen', cuentaOrigen)
                    return
                if usuarioDestino is None:
                    print('La cuenta de destino no se encontro', cuentaDestino)
                    return
                
                # verificar que la cuenta de origen tenga el saldo suficiente para transferir
                if usuarioOrigen['Saldo'] < monto:
                    print('La cuenta: ',cuentaOrigen, 'no cuenta con el saldo suficiente para transferir')
                    return
                
                # hacer la transferencia
                usuarioOrigen['Saldo'] -= monto
                usuarioDestino['Saldo'] += monto
                
                print("Transferencia exitosa de", monto, "de la cuenta", cuentaOrigen, "a la cuenta", cuentaDestino)
                print("Nuevo saldo de la cuenta", cuentaOrigen, "es:", usuarioOrigen['Saldo'])
                print("Nuevo saldo de la cuenta", cuentaDestino, "es:", usuarioDestino['Saldo'])
                return cuentaOrigen, cuentaDestino, monto
# banco = Crud()               
# while True:
    
#     print('Bienvenido al banco')
#     inputUsuario = input('1. Crear usuario\n2. Consultar cuentas\n3. Consultar saldo\n4. Ingresar efectivo\n5. Retirar efectivo\n6. Transferencia\n7. Salir\n')
    
#     if inputUsuario == '1':
#         titular = input('Ingrese el nombre del titular: ')
#         edad = input('Ingrese la edad del titular: ')
#         banco.crearUsuario(titular,edad)
    
#     elif inputUsuario == '2':
#         banco.consultarCuentas()
        
#     elif inputUsuario == '3':
#         cuenta = input('Ingrese la cuenta a consultar: ')
#         banco.getSaldo(cuenta)
    
#     elif inputUsuario == '4':
#         cuenta = input('Ingrese la cuenta a la que se le ingresara el efectivo: ')
#         monto = float(input('Ingrese el monto a ingresar: '))
#         banco.ingresarEfectivo(cuenta,monto)
        
#     elif inputUsuario == '5':
#         cuenta = input('Ingrese la cuenta de la que se retirara el efectivo: ')
#         monto = float(input('Ingrese el monto a retirar: '))
#         banco.retirarEfectivo(cuenta,monto)
    
#     elif inputUsuario == '6':
#         cuentaOrigen = input('Ingrese la cuenta de origen: ')
#         cuentaDestino = input('Ingrese la cuenta de destino: ')
#         monto = float(input('Ingrese el monto a transferir: '))
#         banco.transferencia(cuentaOrigen,cuentaDestino,monto)
        
#     elif inputUsuario == '7':
#         print('Gracias por usar el banco')
#         break