# This is about variable

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#counting car available
print 'There are', cars, "cars avaiable"

#counting drivers available
print 'There are only', drivers, 'drivers available'

#couting empty cars for day
print 'There will be', cars_driven, 'empty cars today'

#counting carpool_capacity
print 'We can transport', carpool_capacity, 'people today.'

#counting passengers
print 'we have', passengers, "to carpool today."

#counting passengers per car
print 'We need to put about', average_passengers_per_car, 'in each car.'
