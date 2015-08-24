#Some variables
#Setting cars number
cars = 100
#Setting space in a car value
space_in_a_car = 4
#Setting number of drivers
drivers = 30
#Setting number of passengers
passengers = 90
#Setting number of cars not driven
cars_not_driven = cars - drivers
#Setting number of cars driven
cars_driven = drivers
#Evaluate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#Evaluate average number of passengers per car
average_passengers_per_car = passengers / cars_driven

#Printing those variables
print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
