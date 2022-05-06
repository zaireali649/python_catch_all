import random

new_var = []

#print(type(new_var), new_var)

numbers = list(range(0,10))

#print(numbers)

numbers.reverse()

#print(numbers)

random.shuffle(numbers)

#print(numbers)

numbers.sort()

#print(numbers)

#numbers.append(100)

#print(numbers)

#random.shuffle(numbers)

#print(numbers)

index = numbers.index(7)

#print(numbers[index])

for number in numbers:
    print(number)
    new_var.append(number**2)
    #print(number ** 2)

print(new_var)

numbers_squared = [number ** 2 for number in numbers]
    
print(numbers_squared)

numbers_squared_odd = [number ** 2 for number in numbers if number % 2 == 1]

print(numbers_squared_odd)