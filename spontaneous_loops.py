import random

number = 5

while number < 10:
    #print(number)
    number = number + 1
    
for devin in range(10):
    number = random.randint(0,10)
    #if(number == 50):
    #    print("we broke")
    #    break
    if(number == 5):
        #print("we continued")
        continue
    print(devin, number)
    
print(devin) # prints out last element from count in for loop above

print(list(range(10)))

cap_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]

print(cap_letters)

every_other_cap_letter = [letter for letter in cap_letters if (ord(letter) % 2) == 0]

print(every_other_cap_letter)

letter = random.choice(cap_letters)
print(letter)

def generate_random_letters(count = 1):
    cap_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    
    s = ""
    
    for i in range(count):
        s += random.choice(cap_letters)
    return s

word = ""
count = 0
while word != "CAT":
    word = generate_random_letters(3)
    count += 1
    
print(count, word)