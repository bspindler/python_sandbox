# A class is like a blueprint for creating objects.  An object has properties and methods (functions) 
# associated with it.  Almost everything in Python is an object

# Create Class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email 
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def increase_age(self):
        self.age += 1

# Extends class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
print(type(brad), brad)
janet = Customer('Janet Z', 'janet@gmail.com', 57)
print(type(janet), janet)
janet.set_balance(500)
print(janet.greeting())

# Access properties
print(brad.name, brad.email, brad.age)

# Run method on class
print(brad.greeting())
brad.increase_age()
print(brad.greeting())