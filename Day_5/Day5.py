# Day 5
import math

# 'There are four collection data types in Python : 
# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.  
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
# A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

# How to Create a List

lst = list()

empty_list = list() # this is an empty list, no items in the list

print(len(empty_list)) # 0

    # Using square brackets, []

lst = []

empty_list = []
print(len(empty_list)) # 0

    # lists with initial values. We use len() to find the length of a list

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yogurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

    # print the lists and its length
print('Fruits:', fruits)
print('Nunmber of fruits:', len(fruits))
print('Vegetables', vegetables)
print('Number of Vegetables:', len(vegetables))
print('Animal Products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web Technologies:', web_techs)
print('Number of web technologies', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# Lists can have items of different data types

lst = ['Jon', 34, True, {'country':'USA', 'city': 'Attlebroro Falls'}] # list containing different data types

    # Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
# last index
last_index = len(fruits) -1
last_fruit = fruits[last_index]

    # Negative Indexing
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_last)

# Unpacking List Items
lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

    # first example

fruits = ['banana', 'orange', 'mango', 'lemon', ' lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

    # second example
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing items from a list
    # positive indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

    # negative indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

# Modifying Lists

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) -1
fruits[last_index] = 'lime'
print(fruits)

# Checking items in a list

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) # True
does_exist = 'lime' in fruits
print(does_exist) # False

# Adding items to a list

lst = list()
lst.append('item')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

# inserting items into a list
    # syntax: lst.insert(index,item)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2,'apple')
print(fruits)
fruits.insert(3, 'lime')
print(fruits)

# Removing items from a list
    # sytax: lst.remove(item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits) # this method removes the first instance of the item
fruits.remove('lemon')
print(fruits)

# Removing items using pop
# the pop() method removes the specified index or the last item if index isn't specified

    # syntax: lst.pop() or lst.pop(index)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

# removing items using Del
# The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely

    # syntax: del lst[index] if only a single item
    # del lst deletes the list completely

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
# print(fruits)

# Clearing List items
# the clear() method empties the list

    # syntax: lst.clear()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# Copying a list
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().

    # syntax: lst_copy = lst.copy()

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining Lists
# There are several ways to join, or concatenate, two or more lists in Python.

    # syntax: list3 = list1 + list2

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

    # Joining using extend() method The extend() method allows to append list in a list. See the example below.
    # syntax
        # list1 = ['item1', 'item2']
        # list2 = ['item3', 'item4', 'item5']
        # list1.extend(list2)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

