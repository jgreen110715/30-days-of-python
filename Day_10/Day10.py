# Day 10
import math

# 30 Days Of Python: Day 10 - Loops

# Loops
    # Life is full of routines. In programming we also o lots of repetitve tasks.. In order to handle repetitive tasks, programming languages use loops. Python programming language also provide the following types of two loops:
        # 1. while loop
        # 2. for loop

# While Loop
    # We use the reserved word while to make a while loop. It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.
        # Syntax:
            # while condition:
                # code goes here

count = 0
while count < 10:
    print(count)
    count += 1
# prints from 0 to 4

    # In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.
        # Syntax:
            # while condition:
                # code goes here
            # else:
                # code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# the above loop will be false when the count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.

# Break and Continue - Part 1
    # Syntax:
        # while condition:
            # code goes here
        # if another_condition:
            # break

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# The above while loop only prints 0, 1, 2, but when it reaches 3, it stops

    # Continue: with the continue statement we can skip the current iteration, and continue with the next:
        # Syntax:
            # while condition:
                # code goes here
            # if another_condition:
                # continue

count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1

# The above while loop only prints 0, 1, 2, 4 (skips 3)

# For Loop
    # A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. For Loop is for iterating over a sequence, that is either a list, a tuple, a dictionary, a set, or a string.

        # For loop with list
            # Syntax:
                # for iterator in lst:
                    # code goes here

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is a temporary name to refer to the list's items, valid only inside this loop
    print(number) # the numbers will be printed line by line from 0 to 5

        # For Loop with string
            # Syntax:
                # for iterator in string:
                    # code goes here

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

        # For loop with tuple
            # Syntax:
                # for iterator in tuple:
                    # code goes here

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

        # For loop with dictionary, looping through a dictionary gives you the key of the dictionary 
            # Syntax:
                # for iterator in dictionary:
                    # code goes here

person = {
    'first_name': 'Jon',
    'last_name': 'Green',
    'age': 34,
    'country': 'USA',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Elm Street',
        'zipcode': '10001'
    }                    
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

        # Loops in set
            # Syntax:
                # for iterator in set:
                    # code goes here

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)