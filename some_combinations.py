import random

random_dict = {}

for i in range(5):
    random_dict[i] = [random.randint(0,100) for j in range(random.randint(1,10))]

for key, value in random_dict.items(): # iterate through dictionary
    print(key, '################################')
    for i in value: # iterate through a list
        print(i)