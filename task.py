my_dict = {
    'piekarnia' : ["chleb", "pączek", "bułki"],
    'warzywniak': ["marchew", "seler", "rukola"],
    'ogrodniczy' : ["haczka", "łopota", "nasiona"]
}

for key, item in my_dict.items():
    print(f'Idę do {key.capitalize()}, kupuję tu następujące rzeczy {item}')
    
new = []
new = my_dict['piekarnia'] + my_dict['warzywniak']
print('W sumie kupuję', len(new), 'produktów')

print('Merry Christmas')

