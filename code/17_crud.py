numbers = [1,2,3,5,6,7,8]
print(numbers[2])
numbers[-1] = 10
print(numbers)
numbers.append(700)
print(numbers)
numbers.insert(0, 'chao')
print(numbers)
numbers.insert(-1, 'amor')
print(numbers)

Tasks = ['Todo1', 'Todo2','todo3']
print(Tasks)

new_list = Tasks + numbers
print(new_list)

index = new_list.index('amor') # para saber la posicion de un dato

print(index)
new_list[index] = 'tuyo'
print(new_list)

new_list.remove('tuyo')
print(new_list)

new_list.pop()
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [2,5,8,7,9]
numbers_a.sort()
print(numbers_a)


letters = ['A', 'B', 'C', 'D', 'E', 'F']

letters.append('G')
letters[0]= 'Z'
letters.remove('C')
letters.reverse()

print(letters)
