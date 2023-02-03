# Day 9: 30 Days of python programming
import math
import statistics

# Exercises: Day 9 - Conditionals
# Level 1

#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
    # Output:
        # Enter your age: 30
        # You are old enough to learn to drive.
    # Output:
        # Enter your age: 15
        # You need 3 more years to learn to drive.

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print('You need ' + str(18-age) + ' more years to learn to drive.')

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
    # Output:
        # Enter your age: 30
        # You are 5 years older than me.

print('who is older me or you?')
my_age = 34
your_age = int(input('Enter your age: '))
if my_age > your_age:
    print('You are', my_age - your_age , 'years younger than me.')
elif my_age < your_age:
    print('You are', your_age - my_age,'years older than me.')
else:
    print('We are the same age.')

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
    # Output:
        # Enter number one: 4
        # Enter number two: 3
        # 4 is greater than 3

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(a, 'is greater than', b)
elif a < b:
    print(a, 'is smaller than', b)
else:
    print(a, 'is equal to', b)

# Level 2

# 1. Write a code which gives grade to students according to theirs scores:
    # 90-100, A
    # 70-89, B
    # 60-69, C
    # 50-59, D
    # 0-49, F

score = int(input('Enter your score: '))
if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
elif score >= 50:
    print('D')
else:
    print('F')

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer.

month = input('Enter a month: ')
month = month.upper()
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn.')
if month == 'December' or month == ' January' or month == 'February':
    print('the season is Winter.')
if month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring.')
if month == 'June' or month == ' July' or month == 'August':
    print('The season is Summer.')

# 3. The following list contains some fruits:
    # fruits = ['banana', 'orange', 'mango', 'lemon']
#   If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ')
fruit = fruit.lower()
if fruit in fruits:
    print('That fruit is already in the list')
else:
    fruits.append(fruit)
    print(fruits)

# Level 3

# 1. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Jon',
    'last_name': 'Green',
    'age': 34,
    'country': 'USA',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# 1.1 Check if the person dictionary has skills key, if yes print('person has skills') else print('person has no skills')
if 'skills' in person:
    print('first_name', 'has skills')
else:
    print('first_name', 'has no skills')

# 1.2 Check if the person dictionary has skills key, if yes check if the person has 'Python' skill and print('person has Python skill') else print('person has no Python skill')
if 'skills' in person:
    if 'Python' in person['skills']:
        print('first_name', 'has Python skill')
    else:
        print('first_name', 'has no Python skill')

# 1.3 If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'skills' in person:
    if 'Javascript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')
