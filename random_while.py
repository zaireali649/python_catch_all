
"""
Your module description
"""

import random

big_number = 0
small_number = 0
med_number = 0
eq_number = 0
numbers = []

found_equal = False

while(not found_equal):
    # generate a random number
    number = random.randint(0,100)
    
    if(number > 75):
        big_number += 1
    elif(number < 25):
        small_number += 1
    elif(number == 50):
        eq_number += 1
        found_equal = True
    else:
        med_number += 1
        
    numbers.append(number)
    
print("small number: ", small_number)
print("medium number: ", med_number)
print("big number: ", big_number)
print("eq number: ", eq_number)

print("Ran num times: ", len(numbers))
