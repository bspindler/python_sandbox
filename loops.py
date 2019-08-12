# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

people = ['John', 'Paul', 'Sarah', 'Susan']

# Simple for loop
print('--- loop ---')
for person in people:
    print(f'current person: {person}')

# Break 
print('--- break ---')
for person in people:
    if person == 'Sarah':
        break
    print(f'current person: {person}')

# Continue 
print('--- continue ---')
for person in people:
    if person == 'Sarah':
        continue
    print(f'current person: {person}')

# range
print('--- range ---') 
for i in range(len(people)):
    print(people[i])

print('-- custom range --') 
for i in range(0,11):
    print(f'number: {i}')    

# While
print('--- while ---')
count = 0
while count < 10:
    print(f'Count: {count}')
    count += 1

