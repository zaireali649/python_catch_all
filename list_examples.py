


"""
Your module description
"""

import random

listy = [2, 3, 4.3, "string_stuff", "another_string"]

for element in listy:
    #print(element)
    pass

letters = ["a","y","f","d","z"]

#print(type(letters))

#print(dir(letters))
#print('\n')

#print(letters)
letters.reverse()
#print(letters)
letters.sort()
#print(letters)
letters.append("t")
#print(letters)

#for letter in letters:
    #print(letter)
    
random_list = []

for i in range(10):
    random_list.append(random.randint(0,500))

#print(random_list)
#print(len(random_list))

random_list_modification = [x * 2 for x in random_list]

#print(random_list_modification)

random_list_2 = [random.randint(0,500) for variable_name in range(10)]

#print (random_list_2)
random_list_2.sort()
#print(random_list_2)

random_list_3 = [random.randint(0,500) for variable_name in range(10)]
#print(random_list_3)
#print(sorted(random_list_3))

#print(dir("this is a string"))

#print("this is a string".capitalize().swapcase())

stringy = "this is a string"
#print(stringy)
stringy = "T" + stringy[1:]
#print(stringy)

def spongebob_meme(string_input):
    string_output = ""
    
    counter = 0
    for s in string_input:
        if (counter % 2 == 0):
            string_output = string_output + s.capitalize()
        else:
            string_output = string_output + s.lower()
        
        if(s != " "):
            counter = counter + 1
    
    return string_output
    
print(spongebob_meme("you need to learn python"))

