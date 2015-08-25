# Defining function cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# First way: Numbers directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Second way: Variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Third way: Math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Fourth way: Combine math and variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
