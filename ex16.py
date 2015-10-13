from sys import argv

script, filename = argv

print(""" We are going to erase %r.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.""" % filename)

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

l1 = input("Line 1: ")
l2 = input("Line 2: ")
l3 = input("Line 3: ")

print("I am going to write these to the file.")

target.write("%s\n%s\n%s\n" % (l1, l2, l3))

print("And finally, we close it.")
target.close()
