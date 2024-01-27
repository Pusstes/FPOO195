contraseña0 = 's195'
contraseña_normal = str(input('ingresa una contraseña: '))
contraseña_minuscula = contraseña_normal.lower()

if contraseña_minuscula == contraseña0:
    print('La contraseña que tecleaste es la misma que la original.')
else:
    print('La contraseña que tecleaste no es la misma que la original')