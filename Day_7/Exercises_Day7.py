# Day 7: 30 Days of python programming
import math
import statistics

# Exercises: Day 7 Sets

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# 1. Find the length of the set it_companies

print(len(it_companies))

# 2. Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies

it_companies.update(['General Electric', 'Nvidia', 'Schneider Electric'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies

it_companies.pop()
print(it_companies)

# 5. What is the difference between remove and discard

# The difference is that if the item isn't found within the set, remove will throw an error whereas discard will not.

# Exercises: Level 2

# 1. Join A and B



# 2. Find A intersection B



# 3. Is A subset of B



# 4. Are A and B disjoint sets



# 5. Join A with B and B with A



# 6. What is the symmetric difference between A and B



# 7. Delete the sets completely


