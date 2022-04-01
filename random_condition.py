"""
Your module description
"""

import random

# generate a random number
number = random.randint(0,100)

if(number > 75):
    print("big number")
elif(number < 25):
    print("small number")
elif(number == 50):
    print("exactly 50")
else:
    print("medium number")
    
print(number)