# Day 3: 30 Days of python programming
import math

# Exercises: Day 3 Operators

# 1. Declare your age as integer variable
my_age = 34

# 2. Declare your height as a float variable
my_height = 74.0 # in inches

# 3. Declare a variable that store a complex number
comp_num = 1j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter the base length of a triange: '))
height = float(input('Enter the height of a triangle: '))
area_of_triangle = 0.5 * (base) * (height)
print('The area of the triangle is: ', area_of_triangle)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
perimeter = a + b + c
print('The perimeter of the triangle is: ', perimeter)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length of rectangle: '))
width = int(input('Enter the width of a rectangle: '))
area_of_rectangle = length * width
perimeter_of_rect = 2 * (length + width)
print('The area of the rectangle is: ', area_of_rectangle)
print('The perimeter of the rectangle is: ', perimeter_of_rect)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14. 
r = int(input('Enter a radius: '))
area_of_cir = 3.14 * r ** 2
print('The area of the circle is: ', area_of_cir)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Calculating the x-intercept

y = 0
x = (0 - 2) / 2
x_intercept = x
print('The x-intercept of y = 2x - 2 is: ', x)

# Calculating the y-intercept

x = 0
y = 2 * x - 2
y_intercept = y
print('The y-intercept of y = 2x - 2 is: ', y)

# Calculating the slope

y1 = 0
y2 = y_intercept
x1 = 0
x2 = x_intercept

slope = (y2 - y1) / (x2 - x1)

print('The slope of y= 2x -2 =: ', slope)

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# Slope

x1 = 2
x2 = 6
y1 = 2
y2 = 10

m = (y2 - y1) / (x2 - x1)

print('The slope of the given points (2,2) and (6,10) is: ', m)

# Euclidean distance

p = [2 , 2]
q = [6 , 10]

euclidean_dist = math.dist(p,q)

print('The Euclidean distance of the given points (2,2) and (6,10) is: ', euclidean_dist)

# 10. Compare the slopes in tasks 8 and 9

if slope == m:
    print('The slope from questions 8 and 9 are equal')
elif slope > m:
    print('The slope from question 8 is greater than the slope of question 9')
else:
    print('The slope from question 9 is greater than the slope of question 8')

eight_nine_eq = slope == m
eight_nine_greater = slope > m

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
import math
# quadratic formula y = ax^2 + bx + c

a = 1
b = 6
c = 9
y = 0

# find the discriminant
d = b**2 - 4 * a * c

if d < 0:
    print('this equation has no real solutions')
elif d == 0:
    x = (-b + math.sqrt(b ** 2 - 4 * a *c)) / (2 * a)
    print('This equation has one solution: ', x)
    y = a * x ** 2 + b * x + c
else:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a *c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a *c)) / (2 * a)
    print('This equation has two solutions: ', x1, 'and', x2)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

a = 'python'
b = 'dragon'

a_len = len(a)
b_len = len(b)

falsy_statement = a_len > b_len

print('The length of the word python is: ', a_len)
print('The length of the word dragon is:', b_len)

print('Is python a longer word than dragon?', falsy_statement)

# 13. Use an operator to check if 'on' is found in both 'python' and 'dragon'

if 'on' in a:  
    pyth = True
if 'on' in b:
    drag = True
if pyth == drag:
    print('(on) is in both words python and dragon')


# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence = 'I hope this course is not full of jargon.'
print('Is the word jargon in the sentence?: ', 'jargon' in sentence)

# 15. There is no 'on' in both dragon and python

if 'on' in a or b:
    print('(On) is in either the word python OR dragon')
else:
    print('(On) is in neither the word python or dragon')

# 16. Find the length of the text python and convert the value to float and convert it to string

print('The length of the word python as a float is: ', float(len('python')))
print('The length of the word python as a string is: ', str(len('python')))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

x = int(input('Enter a value to check to see it it is an even number: '))

mod = x % 2

if x == 0:
    print('The value you entered is zero')
elif mod > 0:
    print('The value you entered is an odd number')
else:
    print('The value you entered is an even number')

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_div = int(7//3)

print(floor_div)

if floor_div == int(2.7):
    print('The floor division of 7 by 3 is equal to the int converted value of 2.7')
else:
    print('The floor division of 7 by 3 is not equal to the int converted value of 2.7')

#19. Check if type of '10' is equal to type of 10
a = type('10')
b = type(10)

if a == b:
    print('The types are the same')
else:
    print('The types do not match')

#20. Check if int('9.8') is equal to 10

a = float('9.8')
b = int(a)

print(b)

if b == 10:
    print('The int of string (9.8) is equal to the int (10)')
else:
    print('The values are not the same')

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input('Enter hours: '))
rate = int(input('Enter rate per house: '))
earn = hours * rate
print('Your weekly earning is ', earn)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.

years = int(input('Enter the number of years you have lived: '))
seconds = years * 60 * 60 * 24 * 365

print("You have lived for ", seconds , 'seconds')

# 23. Write a Python script that displays the following table

for x in range(1,6):
    print(x , 1, x**1, x**2, x**3)
