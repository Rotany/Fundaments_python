# not True = False
# not False = True

print('AND') # operador not es un signo de negación 
print('not True and True =>',  not True and True)
print('not True and False =>', not True and False)

print('not False and False =>', not False and False)
print('not False and True =>',  not False and True)


stock = input('Ingrese el numero de stock=>')
stock = int(stock)
print(not (stock>= 100 and stock <=1000 ))
