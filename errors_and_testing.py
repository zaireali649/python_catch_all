import random

''' 

for i in range(100):
    try:
        print(random.randint(0, 10) / random.randint(0, 10))
        if(i == 99):
            print(bad_variable / random.randint(0, 10))
        elif(i == 98):
            print(random.randint(0, 10) / "string")
        
    #except:
        #print("You cant divide by zero")
    except Exception as e:
        print(e)
'''

number = random.randint(0, 100)
#print(number)

def grade_number(number):
    responses = []
    
    if(number > 11): # none
        responses.append("GG")
    if(number > 7): # 8, 9, 10
        responses.append("G")
    elif(number < 3): # 0, 1, 2
        responses.append("L")
    else: # 3, 4, 5, 6, 7
        responses.append("mid")
    
    #print(responses)
    return responses

print("G" in grade_number(9))
print("L" in grade_number(2))
print("mid" in grade_number(5))
print("GG" in grade_number(15))
print("G" in grade_number(15))
print("G" in grade_number(15) and "GG" in grade_number(15))

#print("we finished the code")
