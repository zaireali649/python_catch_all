import random

#number = random.randint(0,10)
number = 7
number += 1 # number = number + 1

threshold = 5
if(number > threshold):
    print(number, " is greater than ", threshold)
elif(number == threshold):
    print(number, " equals ", threshold)
else:
    print(number, " is less than ", threshold)