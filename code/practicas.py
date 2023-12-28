'''
list_numeros = [1, 2, 3, 4, 5, 15, 16, 20, 30]

def fizzbuzz (list_numeros):
    for num in list_numeros:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz.upper()")
        

fizzbuzz( list_numeros)
'''




def fizzbuzz ():
    for num in range(3,55):
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        
fizzbuzz()



