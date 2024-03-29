# A module is basically a file containing a set of functions to include in  your application 
# There are core python modules, modules you can install using the pip package manager (including Django)
# as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time 

today = datetime.date.today()
today = date.today()
timestamp = time()

print(today, timestamp)

# Pip module
import camelcase
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))

# Import custom module
import validator
from validator import validate_email

print(validate_email('me@home.com'))