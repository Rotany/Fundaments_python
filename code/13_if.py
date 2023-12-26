
# operador if es un condiciaonal
if True:
    print( 'debería ejecutarse')

if False:
    print('no debería ejecutarse')
'''
pet = input('Cual es tu mascota favorita =>')
if pet == 'perro':
    print('genial tienes buen gusto')

elif pet == 'gato':
    print('espero tengas suerte')

elif pet == 'pez':
    print('eres genial')
else:
    print('no tienes ninguna mascota interesante ')
'''

'''
stock = int(input('digita el stock =>'))
if stock>= 100 and stock <=1000 :
    print('el stock es correcto')
else:
    print('el stock es incorrecto ')
'''


num = int(input('Cual es el numero =>'))
result = num % 2 
if result == 0:
    print( 'es par')
else:
    print('es impar')
