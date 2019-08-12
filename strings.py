# Strings in python are surrounded by either single or double quotation marks.

name = 'Brad'
age = 37

# Concatenate

nameAndAge = name + ' - ' + str(age)

print(nameAndAge)

# String formatting


# ARguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String methods
s = 'hello world'

# Capitalize String 
print(s.capitalize())
print(s.upper())
print(len(s)
) # location of parens does not matter