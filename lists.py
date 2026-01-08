import os
os.system('cls||clean')
''' Colletions = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates Ok
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates Ok. Faster
'''

fruits = ['apple', 'orange', 'banana', 'coconut', 'banana']
fruits_set = {'apple', 'orange', 'banana', 'coconut', 'banana'}
print(fruits)
print(fruits[::-1])
print(fruits[:3])

fruits.append('pineapple')

for fruit in fruits:
    print(fruit)

fruits.sort()
fruits.reverse()
print(fruits)
print(fruits.index('orange'))
print(fruits.count('banana'))


print(fruits_set)

os.system('exit')