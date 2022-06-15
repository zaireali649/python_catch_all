stuff_dictionary = {}

stuff_dictionary['fruits'] = ['apple','cranberry','grapefruit','peaches']

stuff_dictionary['colors'] = ['red','blue','yellow']

stuff_dictionary['numbers'] = list(range(100))

print(stuff_dictionary.keys())

for key, value in stuff_dictionary.items():
    print(key)
    print(value)

stuff_dictionary_other = {'juices':['cranberry','apple','grape']}

print(stuff_dictionary_other)