# Day 6: 30 Days of python programming
import math
import statistics

# Exercises: Day 6 Tuples
    # Exercises: Level 1

# 1. Create an empty tuple

tpl = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

sisters = ('Melissa', 'Jenn')
brothers = ('Ramsey', 'Dave')

# 3. Join brothers and sisters tuples and assign it to siblings

siblings = sisters + brothers
print(siblings)

# 4. How many siblings do you have?

print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

siblings = list(siblings)
parents = ['Mum', 'Dad']
family_members = siblings + parents
family_members = tuple(family_members)
print(family_members)

# Exercises: Level 2

# 1. Unpack siblings and parents from family_members

siblings = family_members[:4]
parents = family_members[4:]
print('My siblings are:', siblings)
print('I call my parents:', parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('apples', 'oranges', 'bananas')
vegetables = ('carrots', 'tomatoes', 'peppers')
animal_products = ('milk', 'honey', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_tp = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print(len(food_stuff_tp))
print(food_stuff_tp[int(len(food_stuff_tp) / 2)])

# 5. Slice out the first three items and the last three items from food_staff_lt list

first_three_items = food_stuff_tp[:3]
last_three_items = food_stuff_tp[-3:]

print('The first three items:', first_three_items)
print('The last three items:', last_three_items)

# 6. Delete the food_staff_tp tuple completely

food_stuff_tp = tuple(food_stuff_tp)
del food_stuff_tp

# 7. Check if an item exists in tuple:

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    # Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

    # Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)