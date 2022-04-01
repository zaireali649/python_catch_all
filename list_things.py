"""
Your module description
"""

lorem_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"

lorem_list = lorem_string.split(' ')

print((lorem_list))

url_string = "https://us-east-1.console.aws.amazon.com/cloud9/ide/aa64ae38872244ee9d60fd201875a517"
url_list = url_string.split('/')

url_string_2 = '/'.join(url_list)

print((url_list))
print((url_string_2))

for word in lorem_list:
    print(len(word)) # print length of word

no_a_lorem_string = [word.replace("a","") for word in lorem_list]

print(no_a_lorem_string)
    