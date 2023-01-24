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

A.update(B)
print(A)

# 2. Find A intersection B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
int = A.intersection(B)
print(int)


# 3. Is A subset of B

print(A.issubset(B))

# 4. Are A and B disjoint sets

print(A.isdisjoint(B))

# 5. Join A with B and B with A

C = A.union(B)
D = B.union(A)
print(C)
print(D)

# 6. What is the symmetric difference between A and B

print(A.symmetric_difference(B))

# 7. Delete the sets completely

del A
del B

# Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_st = set(age)
print(len(age))
print(len(age_st))

if len(age) > len(age_st):
    print('The List of Ages is longer than the Set of Ages')
else:
    print('The Set of Ages is longer than the List of Ages')


#2. Explain the difference between the following data types: string, list, tuple and set

# A String: is any length of characters placed between '' or ""

# A List: is a muteable group, that can of different datatypes, where [] are used

# A Tuple: A tuple is a collection of different data types which is ordered and unchangeable. Uses ()

# A Set: Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items. Uses {}


# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.


