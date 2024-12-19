my_dict = {
    'piekarnia' : ["chleb", "pączek", "bułki"],
    'warzywniak': ["marchew", "seler", "rukola"]
}

for key, item in my_dict.items():
    print(f'Idę do {key.capitalize()}, kupuję tu następujące rzeczy {item}')
    
