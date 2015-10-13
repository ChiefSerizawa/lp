from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("\nPrevious printings used CLI to get data from users.")
print("Next printings use input() function\n")
first = input("Give a first variable: ")
snd = input("And a second one (an int plz): ")
print("First:", first)
print("Second: (Your int plus 1):", int(snd)  + 1)
