# Escribir una función que calcule el total de una factura tras aplicarle
# el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
# IVA a aplicar, y devolver el total de la factura. Si se invoca la función
# sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calcular_iva(monto, iva):
    if iva == "":
         total_iva = monto * .21
         total_monto = monto + total_iva
    else:
         iva = float(iva)
         total_iva = monto * iva
         total_monto = monto + (total_iva/100)
    
    return total_monto
   

monto = float(input('Ingresa el monto de tu factura: '))
iva = input('Ingresa el monto de IVA que te cobraran:')
print(f"Tu factura sera de {calcular_iva(monto, iva)}")