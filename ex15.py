# Importing argv
from sys import argv

# Unpacking
script, filename = argv

# Opening file
txt = open(filename)

# Printing file content
print("Here's your file %r:" % filename)
print(txt.read())

# Asking for filename to read
print("Type the filename again:")
file_again = input("> ")

# Opening file
txt_again = open(file_again)

# Printing file content again
print(txt_again.read())

# Closing files
txt.close()
txt_again.close()

