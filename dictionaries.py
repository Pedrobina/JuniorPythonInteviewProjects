import os
os.system('cls||clear')
#KeyValues pairs, they are ORDERED and CHANGEABLE. No duplicates!

capitals = {'USA': 'Washington D.C.',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia':'Moscow'}


print(capitals.get('USA'))
print(capitals.get('Japan'))


capitals.update({'Germany': 'Berlin'})

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)

#works like a touple
for key, value in capitals.items():
    print(f'Country: {key}| Capital: {value}')





os.system('exit')