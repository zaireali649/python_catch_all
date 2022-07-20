var_1 = "some string of characters"

var_2 = 65

var_3 = 2.54

# expect str 
print(type(var_1))
# expect int
print(type(var_2))
# expect float
print(type(var_3))

var_4 = "65"

# expect str
print(type(var_4))

#var_5 = input("gimmie a number: ")
# expect str
#print(type(var_5))

var_6 = 5/10
# expect float
print(type(var_6))

var_7 = True
# expect bool
print(type(var_7))

var_8 = int(var_4)
# expect int
print(type(var_8))

try:
    var_9 = int("break it")
except:
    var_9 = 0

# expect 0
print(var_9)

var_10 = float(649)
# expect float
print(type(var_10))
# expect 649.0
print(var_10)

var_11 = int(49.3)
# expect int
print(type(var_11))
# expect 49
print(var_11)