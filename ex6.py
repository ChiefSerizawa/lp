# Setting some variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing x and y
print(x)
print(y)

# Printing x and y with a header
print("I said: %r." % x)
print("I also said: '%s'" % y)

# Setting some variables
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

# Printing them
print(joke_evaluation % hilarious)

# Setting again
w = "This is the left side of... "
e = "A string with a right side."

# Printing again
print(w+e)
