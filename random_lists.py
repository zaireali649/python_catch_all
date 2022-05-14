import random

# generate a random string with structure aaaa-aaaa-aaaa-aaaa
# where a chunk is aaaa
def random_string_id(chunk_amount = 4, chunk_size = 4):
    lower_letters = [chr(i) for i in (range(ord("a"),ord("z")+1))]
    numbers = [str(i) for i in range(0,10)]
    characters = lower_letters + numbers

    return '-'.join([''.join([random.choice(characters) for j in range(chunk_size)]) for i in range(chunk_amount)]) 
    
    
number = random.randint(0,100)

#print(number) # print random number 0-99

capital_letters = [chr(i) for i in (range(ord("A"),ord("Z")+1))]
lower_letters = [chr(i) for i in (range(ord("a"),ord("z")+1))]

#print(capital_letters)
#print(lower_letters)

letters = capital_letters + lower_letters

#print(random.choice(letters))

print(random_string_id(chunk_amount = 6, chunk_size = 6))
