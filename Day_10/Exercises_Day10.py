# Day 10: 30 Days of python programming
import math
import statistics

# Exercises: Day 10 - Loops

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

count = 0
while count < 11:
    print(count)
    count += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for number in numbers:
    print(number)

count = 10
while count >= 0:
    print(count)
    count -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

count = 0
while count <= 7:
    print (count * '#')
    count += 1

# 4. Use nested loops to create the following:
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #
  # # # # # # # #

for i in range(8):
    for j in range(8):
        print('# ', end='')
    print('#')

# 5. Print the following pattern:
    # 0 x 0 = 0
    # 1 x 1 = 1
    # 2 x 2 = 4
    # 3 x 3 = 9
    # 4 x 4 = 16
    # 5 x 5 = 25
    # 6 x 6 = 36
    # 7 x 7 = 49
    # 8 x 8 = 64
    # 9 x 9 = 81
    # 10 x 10 = 100

count = 0
while count <= 10:
    print(count, 'x', count, '=', count * count)
    count += 1

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lang = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lang:
    print(i)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0, 101, 2):
    print(i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(1, 101, 2):
    print(i)

# Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    # The sum of all numbers is 5050

sum = 0
for i in range(0, 101):
    sum += i
    i += 1
print('The sum of all the numbers is:', sum)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    # The sum of all evens is 2550, and the sum of all ods is 2500

sum_even = 0
sum_odd = 0
for j in range(0, 101, 2):
    sum_even += j
    j += 1
for k in range(1, 101, 2):
    sum_odd += k
    k += 1
print('The sum of all evens is:', sum_even, 'and the sum of all odds is:', sum_odd)

# Exercises: Level 3

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.



# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.



# 3. Go to the data folder and use the countries_data.py file.
    # What are the total number of languages in the data
    # Find the ten most spoken languages from the data
    # Find the 10 most populated countries in the world