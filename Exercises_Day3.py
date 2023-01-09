# Day 3: 30 Days of python programming
import math

# Exercises: Day 3

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
