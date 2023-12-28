#Escribir un programa que almacene la cadena de caracteres contraseña
# en una variable, pregunte al usuario por la contraseña e imprima por pantalla 
#si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
key = 'contraseña'
pasword = input('ingrese contraseña=>')
if key == pasword.lower():
    print('contraseña correcta')
else:
    print('contraseña no coincide')
'''

# Escribir un programa que pregunte al usuario su edad 
# y muestre por pantalla si es mayor de edad o no.
    
edad = int(input('cuantos años tienes=>'))
if edad >= 18:
    print('eres mayor de edad')
else:
    print('no eres mayor de edad')

# Escribir un programa que pida al usuario dos números y
# muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
    
n = float(input('ingrese dividendo'))
m= float(input('ingrese divisor'))
if 'm' == 0:
    print('error. No se puede dividir por cero')
else:
    print('n/m')


