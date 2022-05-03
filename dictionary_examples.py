pokemans_dictionary = {}

#print(type(pokemans_dictionary))

pokemans_dictionary['charmander'] = {"type1":"Fire"}
pokemans_dictionary['squirtle'] = {"type1":"Water"}
pokemans_dictionary['wartortle'] = {"type1":"Water"}
pokemans_dictionary['blastoise'] = {"type1":"Water"}

#print(pokemans_dictionary["squirtle"])

pokemans_dictionary["squirtle"]["#"] = "7"

#print(pokemans_dictionary["squirtle"])

#for key in pokemans_dictionary:
#    print(pokemans_dictionary[key])
    
#for key in pokemans_dictionary.keys():
#    print(pokemans_dictionary[key])
    
#for key, value in pokemans_dictionary.items():
#    print(key, value)

delete_these = []

for key, value in pokemans_dictionary.items():
    if("water".lower() in value['type1'].lower()):
#        print(key, value)
        delete_these.append(key)

#for key in delete_these:
#    del pokemans_dictionary[key]

#print('\n')

#for key, value in pokemans_dictionary.items():
#    print(key, value)

response = {
    'MD5OfMessageBody': 'string',
    'MD5OfMessageAttributes': 'string',
    'MD5OfMessageSystemAttributes': 'string',
    'MessageId': 'string',
    'SequenceNumber': 'string'
}

print(response)