# A Tuple is a collection which is ordered and unchangeable.  Allows duplicate members. 
# create a tuple
fruits = ('Apples', 'Oranges', 'Grapes') # parens makes it a tuple! but don't confuse with constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

fruits3 = ('Apples')

# get value
print(fruits[1])

# Delete tuple
del fruits2
# print(fruits2)  # NameError: name 'fruits2' is not defined

# Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed.  No duplicate members. 
fruits_set = {'Apples', 'Oranges', 'Mango'}
print('Apples' in fruits_set)
print(fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

#Remove from set
fruits_set.remove('Grapes')

print(fruits_set)

# Clear set
fruits_set.clear()

print(fruits_set)
