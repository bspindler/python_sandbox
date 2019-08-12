# If/Else conditions are used to decide to do something based on something being true or false

x = 10 
y = 10

# Comparision Operators (==, !=, >, <, >=, <=) - Used to compare values
# simple if 
if x > y: 
    print(f'{x} is greater than {y}')

# if/else
if x > y:
    print(f'{x} is greater than {y}')
else: 
    print (f'{x} is smaller than {y}')

# if/elif/else
if x > y: 
    print(f'{x} is greater than {y}')
elif y > x: 
    print(f'{y} is greater than {x}')
else: 
    print(f'not sure') 

# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than 10')

# not
if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership operators (not, not in)

numbers = [1,2,3,4,5]

if x not in numbers: 
    print(f'{x} is not in {numbers}')
else:
    print(f'{x} is in {numbers}')

# Identify operators (is, is not). Compare objects are equal,
# not that they have the same value, but that they are the same object
# in memory

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)