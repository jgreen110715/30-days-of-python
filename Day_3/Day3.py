# Day 3

# Example: Integers
# Arithmetic Operations in Python
# integers

print('Addition: ', 1 + 2) # 3
print("Subtraction: ", 2 -1) # 1
print('Multiplication: ', 2 * 3) # 6
print('Division: ', 4 / 2) # 2.0 Division in Python gives a floating number
print('Division: ', 6 / 2) # 3.0
print('Division: ', 7 / 2 ) #3.5
print('Division without the remainder: ', 7 // 2) # 3, gives the answer as an int
print('Division without the remainder: ', 7 // 3) # 2
print('Modulus: ', 3 % 2) # 1, gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 *2 or 2^3

# Example: Floats

print('Floating point number: PI', 3.14)
print('Floating point number, gravity: ', 9.81)

# Example: Complex numbers

print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is and integer data type
b = 2 # b is a variable name and 2 is an integer data type

# arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Calculating the area of a circle
radius = 10
area_of_a_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_a_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of a rectangle: ', area_of_rectangle)
 
# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# Calculating the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 kg/m^3
print(density, 'Kg/m^3')
