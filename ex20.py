# Importing argv class from sys module (or library)
from sys import argv

# Unpacking argv
script, input_file = argv

# Defining print_all function
def print_all(f):
    print(f.read())

# Defining rewing function (get cursor back to beginning of the file)
def rewind(f):
    f.seek(0)

# Defining print_a_line function
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")

# Opening the file given as an argument to the script
current_file = open(input_file)

# Running the defined functions
print("First let's print the whole file:")
print_all(current_file)

print("Now let's rewind, kind of like a tape")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
