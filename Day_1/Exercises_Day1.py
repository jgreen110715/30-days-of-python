# Day 2: 30 Days of python programming
import math

#Exercises - 30 Days Of Python: Day 1 - Introduction

# Part 1
# Run the following opperations. The operands are 3 and 4

print(3 + 4) # addition (+)
print(4 - 3) # subtraction (-)
print(4 * 3) # multiplication (*)
print(4 % 3) # modulus (%)
print(4 / 3) # division (/)
print(4 ** 3) # exponential (**)
print(4 // 3) # floor division operator (//)

# Part 2
# Write strings on the python interactive shell.

name = 'Jon'
print(name)
familyName = 'Green'
print(familyName)
country = 'USA'
print(country)
course = 'I am enjoying 30 days of python'
print(course)

# Part 3
# Check the data types of the following data:

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Green', 'Python', 'USA']))
print(type(name))
print(type(familyName))
print(type(country))

# Exercise: Level 3
# Find an Euclidian distance between (2,3) and (10,8)

#import math Library
import math

p = [2 , 3]
q = [10 , 8]

print(math.dist(p, q))
