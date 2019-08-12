# A list is a collection which is ordered and changeable.  Allows duplciate members. 

# Create a list 
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1,2,3,4,5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos') 

print(fruits)

# Remove from list
fruits.remove('Grapes')

print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')

print(fruits)

# Remove by position 
fruits.pop(2)

print(fruits)

# reverse
fruits.reverse()

print(fruits)

# sorts
fruits.sort()
print(fruits)

# reverse sort 
fruits.sort(reverse=True)
print(fruits)
