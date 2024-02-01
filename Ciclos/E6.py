saldo = 0 
while True: 
    operacion = input("Ingrese una operación (D para depósito, R para retiro, o Enter para finalizar): ")
    operacion = operacion.upper() 
    if operacion == "": 
        break 
    monto = int(input("Ingrese el monto: ")) 
    if operacion == "D": 
        saldo += monto 
    elif operacion == "R": 
        saldo -= monto 
    print("Saldo actual:", saldo) 
print("Saldo final:", saldo)