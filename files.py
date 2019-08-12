# Python has functions for creating, reading, updating, and deleting files

# create/open a file
myFile = open('myfile.txt', 'w') # all it takes to create a file

# get some info
print('Name: ', myFile)
print('Is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a') # a == append 
myFile.write('I also like PHP')
myFile.close()


# Read from file
myFile = open('myfile.txt', 'r+') # r+ == readd
text = myFile.read(1000)
print(text)