# A Dictionary is a collection which is unordered, changeable and indexed.  No duplicate members. 

# Create a Dictionary
person = {
    'first_name': 'John',
    'last_name': 'Smith',
    'age':  30
}

print(person, type(person))

# Use constructor 
person2 = dict(first_name='Sara', last_name='Smith')

print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('first_name'))

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get dict keys
print('keys: ', person.keys())

# Get dict items
print('items: ', person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'boston'

print(person2)

# Remove an item 
del(person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()

print(person)

# Length
print(len(person2))

# List of dicts
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)

print(people[1]['name'])

