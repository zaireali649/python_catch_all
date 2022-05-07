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
    #print(number)
    new_var.append(number**2)
    #print(number ** 2)

#print(new_var)

numbers_squared = [number ** 2 for number in numbers]
    
#print(numbers_squared)

numbers_squared_odd = [number ** 2 for number in numbers if number % 2 == 1]

#print(numbers_squared_odd)

rand_numbers = []

for i in range(10):
    rand_numbers.append(random.randint(0, 1000) )

print(rand_numbers)

max_val = -1

for number in rand_numbers:
    if number > max_val:
        max_val = number
        
print(max_val)

rand_numbers.sort()

print(rand_numbers)

#print(rand_numbers[-2])

max_val = -101

for number in rand_numbers:
    if number > max_val:
        max_val = number

new_arr = []

for number in rand_numbers:
    if number != max_val:
        new_arr.append(number)

max_val = -101

for number in new_arr:
    if number > max_val:
        max_val = number
        

print(max_val)

print(max(rand_numbers))

max_val = max(rand_numbers)

new_arr = []

for number in rand_numbers:
    if number != max_val:
        new_arr.append(number)
        
max_val = max(new_arr)

print(max_val)
        
