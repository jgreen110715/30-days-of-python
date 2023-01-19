# Day 5: 30 Days of python programming
import math
import statistics

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

# 22. Remove the middle IT company or companies from the list


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.remove(it_companies[int(len(it_companies) / 2)])

print(it_companies)


# 23. Remove the last IT company from the list

it_companies.remove(it_companies[-1])
print(it_companies)

# 24. Remove all IT companies from the list

it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list

del it_companies

# 26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full = front_end + back_end
print(full)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = full.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

    # Exercises: Level 2

# 1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages)
print('The min age is:', min_age)
print('The max age is:', max_age)



# Add the min age and the max age again to the list

ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

# Find the median age (one middle item or two middle items divided by two)

mid_age = int(statistics.median(ages))
print('The median age is:', mid_age)

# Find the average age (sum of all items divided by their number )

avg_age = int(statistics.mean(ages))
print('The average age is:', avg_age)

# Find the range of the ages (max minus min)

range_age = max_age - min_age
print(range_age)

# Compare the value of (min - average) and (max - average), use abs() method

comp_min = abs(min_age - avg_age)
comp_max = abs(max_age - avg_age)
print(comp_max == comp_min)
print(comp_max > comp_min)