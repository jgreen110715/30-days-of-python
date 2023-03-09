# Day 11
import math

# 30 Days Of Python: Day 11 - Functions

# Functions
    # So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them.

# Defining a Function
    # A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the def keyword. The following in the syntax for defining a function. The function block code is executed only if the function is called or invoked.

# Declaring and calling a Function
    # When wemakea function, we call it declaring a function. When we start using the it, we call it calling or invoking a function. Function can declared with or without parameters.

        # Syntax:
            # Declaring a function
                # def function_name():
                    # codes
                    # codes
                # Calling a function
                # function_name()

# Function without Parameters
    # Function can be declared without parameters.

def generate_full_name ():
    first_name = 'Jon'
    last_name = 'Green'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers () # calling a function

# Function Returning a Value - Part1
    # Function can also return values, if a function does not have a return statment, the value of the function is None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.

def generate_full_name ():
    first_name = 'Jon'
    last_name = 'Green'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name ())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers ())

# Function with Parameters
    # In a function we can pass different data types (number, string, boolean, list, tuple, dictionary, or set) as a parameter
        # Single Parameter: if out function takes a parameter we should call our function with an argument
            # Syntax:
                # Declaring a function
                # def function_name(parameter):
                    # codes
                    # codes
                # Calling a function
                # print(function_name(argument))

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings ('Jon'))

def add_ten(num):
    ten = 10
    return num + 10
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return(total)
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# Two Parameters: A function may or may note hva a parameter or parameters. A function may also have two or more parameters. If our function takes parameters, we should call it with arguments. Let us check a function with two parameters:
    # Syntax:
    # Declaring a function
    # def function_name(parameter1, parameter2):
    # codes
    # codes
    # print(funtion_name(arg1, arg2))

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Jon', 'Green'))
