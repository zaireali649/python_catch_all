import random

random_dictionary = {chr(random.randint(ord('A'),ord('Z'))):i for i in range(0,10)}

print(random_dictionary)

for key, value in random_dictionary.items():
    print(key, value)