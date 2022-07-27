import random

number = random.randint(0,10)

print(number)

if (number > 5): # explicitly >
    print("larger than 5")
elif(number == 5):
    print("number is 5")
else: # implicitly <
    print("smaller than 5")