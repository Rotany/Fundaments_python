
'''
user_option = input('piedra, papel, tijera =>')
computer_option = 'piedra'
if user_option == computer_option:
    print('empate')
elif user_option == 'piedra':
    if computer_option =='tijera':
        print('piedra gana a tigera')
        print('user gano!')
    else:
        print('papel gana a piedra')
        print('computer gano!')

elif  user_option == 'papel':
    if computer_option =='piedra':
        print('papel gana a piedra')
        print('gano user')
    else:
        print('tijera gana a papel')
        print('gana computer')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('user gano')
    else:
        
        print('piedra gana a tijera')
        print('computer gano')
'''


number = '10'
number = int(number)
print(number)
result = number%2
if result == 0:
    print ('es par')
else:
    print('es impar')





