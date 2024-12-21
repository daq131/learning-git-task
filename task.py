my_dict = {
    'piekarnia' : ["chleb", "pączek", "bułki"],
    'warzywniak': ["marchew", "seler", "rukola"]
}

for key, item in my_dict.items():
    print(f'Idę do {key.capitalize()}, kupuję tu następujące rzeczy {item}')
    
new = []
new = my_dict['piekarnia'] + my_dict['warzywniak']
print('W sumie kupuję', len(new), 'produktów')

text = 'bla'
print(3*'bla')
print(1918-1795)