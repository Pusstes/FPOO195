# if
# z = 5
# if z % 2 == 0:
#     print('z is even')


# if else
# z = int(input('ingresa un numero entero: '))
# if z % 2 == 0:
#     print('z is even')
# else:
#     print('z is odd')


room = 'bed'
area = '14.0'

if room == 'Kit':
    print('looking around in the kitchen')
elif room == 'bed':
        print('looking around the bedroom')
else:
    print('looking around elsewhere')
    if area > 15:
        print('big place!')
            
    else:
        print('pretty small')