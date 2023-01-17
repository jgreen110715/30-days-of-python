# Day 2: 30 Days of python programming
import math
# Exercises: 30 Days Of Python: Day 2 - Variables, Builtin Functions
# Level 1

firstName = 'Jon'
lastName = 'Green'
fullName = 'Jon Green'
country = 'USA'
city = 'Attleboro Falls'
age = 34
year = 2023
is_married = True
is_true = True
is_light_on = False
day, date, month, street = 'Thursday', 5, 'January', 'Commonwealth Ave'

print(day, month, date, year)

# Exercise: Level 2

print('Length of first name:', len(firstName))
print('Is last name longer than first name?', len(lastName) > len(firstName))

num_one = 5
num_two = 4
print(num_one + num_two)
print(num_one - num_two)
print(num_one * num_two)
print(num_one / num_two)
print(num_one % num_two)
print(num_one ** num_two)
print(num_one // num_two)

r = 30
areaOfCircle = math.pi * (r ** 2)
print('The area of the circle with radius 30 is:', areaOfCircle)

circumOfCircle = math.pi * 2 * r
print('The circumference of the circle with radius 30 is:',circumOfCircle)

r = input('Enter a radius:')
areaOfCircle = math.pi * (int(r) ** 2)
print('The area of the circle with a radius of ',r, ': ', areaOfCircle)

firstName = input('Enter your first name:')
lastName = input('Enter your last name:')
country = input('Enter your home country:')
age = input('Enter your age:')

print(firstName, lastName, country, age)
