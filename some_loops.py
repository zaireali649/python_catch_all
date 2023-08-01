import random

numbers = [0,1,2,3,4,5]

#print(numbers)

for i in range(10):
    print(i)
    
counter = 0
while(counter < 5):
    print(random.randint(10,15))
    counter += 1
