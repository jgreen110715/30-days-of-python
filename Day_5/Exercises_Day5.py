# Day 5: 30 Days of python programming
import math

# Exercises: Day 5 Lists
    # Exercises: Level 1

# 1. Declare an empty list

lst = []

# 2. Declare a list with more than 5 items

family = ['Jon', 'Liz', 'Basil', 'Winter', 'Buggy', 'Mika']

# 3. Find the length of your list

print(len(family))

# 4. Get the first item, the middle item and the last item of the list

first_item = family[0]
middle_item = family[int(len(family) / 2 - 1)]
last_item = family[-1]

print(first_item, middle_item, last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

about_me = ['Jon', 34, 74, 'Married', 'Attleboro Falls']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()

print(it_companies)

# 8. Print the number of companies in the list

print(len(it_companies))

# 9. Print the first, middle and last company

print(it_companies[0], it_companies[3], it_companies[-1])

# 10. Print the list after modifying one of the companies

it_companies[0] = 'Schneider Elecric'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Tesla')

# 12. Insert an IT company in the middle of the companies list

it_companies.insert(3, 'Lenovo')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)

cap = it_companies[1]

print(cap.upper())

# 14. Join the it_companies with a string '#;  '

str = ['#;']
it_companies.extend(str)
print(it_companies)

# 15. Check if a certain company exists in the it_companies list.

does_exist = 'Google' in it_companies
print(does_exist)

# 16. Sort the list using sort() method

it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method

it_companies.sort(reverse=True)
print(it_companies)

# 18. Slice out the first 3 companies from the list

print(it_companies[:3])

# 19. Slice out the last 3 companies from the list

print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list

print(it_companies[int(len(it_companies) / 2 - 1)])

# 21. Remove the first IT company from the list

it_companies.remove(it_companies[0])
print (it_companies)

