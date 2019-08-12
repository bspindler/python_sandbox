"""
Variable rules: 
 - Variable names are case sensitive (name and NAME are different variables) 
 - Must start with a letter or an underscore
 - Can have numbers but can not start with one
"""

#x = 1          # int 
#y = 2.5        # float 
#name = 'John'  # str 
#is_cool = True # bool

# Multiple assignment 
x, y, name, is_cool = (1, 2.5, 'John', True)

# Basic math 
a = x + y 

print(x, y, name, is_cool, a)

# check type of x
print(type(x))

# Casting
x = str(x)

print(type(x), x)

y = int(y)
print(type(y), y)

z = float(y)
print(type(z), z)

