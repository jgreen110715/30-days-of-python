# Day 7
import math

# Sets
    # Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

# Creating a Set
    # We use curly brackets, {} to creat a set or the set() built-in functions    
    
    # Creating an empty set
        # Syntax
            # st = {}
            # st = set()

    # Creating a set with initial items
        # Syntax
            # st = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting Set's length
    # We use the len() method to find the length of a set
        # Syntax:
            # st =  {'item1', 'item2', 'item3', 'item4'}
            # len(st)

fruits =  {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# Accessing items in a set
    # We use loops to access items. We will see this in the loop section

# Checking an item
    # To check if an item exists in a list we use the in membership operator
        # Syntax:
            # st = {'item1', 'item2', 'item3', 'item4'}
            # print("Does set st contain item3? ", 'item3' in st)

fruits =  {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits) # True

# Adding Items to a set
    # Once a set is created we cannot change any items but can add additional items
        # add one item using add() 
            # Syntax:
                # st = {'item1', 'item2', 'item3', 'item4'}
                # st.add('item5')

fruits =  {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

    # add multiple items using update(). the update() allows to add multiple items to a set.
    # The update() take a list argument
        # Syntax:
            # st = {'item1', 'item2', 'item3', 'item4'}
            # st.update(['item5', 'item6', 'item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)

print(fruits)

# Removing items from a Set
    # We can remove and item from a set using remove() method. If the item is not found, remove() method will raise erros, so it is good to check if the item exists in the given set. however, discard() method doesn't raise any errors
        # Syntax:
            # st = {'item1', 'item2', 'item3', 'item4'}
            # st.remove('item2')
    # The pop() method removes a random item from a list and it returns the removed item

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()

    # if we are interested in the removed item.

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)

# Clearing Items in a Set
    # If we want to clear or empty the set we use the clear() method
        # Syntax:
            # st = {'item1', 'item2', 'item3', 'item4'}
            # st.clear() 

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# Deleting a Set
    # If we want to delete the set itself we use the del operator
        # Syntax: 
            # st = {'item1', 'item2', 'item3', 'item4'}
            # del st

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting List to Set
    # We can convert lists to sets and sets to lists. Converting list to set removes duplicates and only unique items will be reserved
        # Syntax:
            # st = {'item1', 'item2', 'item3', 'item4', 'item1'}
            # st = set(lst) - The order is random because sets in general are unordered

fruits = {'banana', 'orange', 'mango', 'lemon', 'orange', 'banana'}
fruits = set(fruits)
print(fruits)

# Joining Sets
    # We can join two sets using the union() or update() method
        # Union() method returns a new set
            # Syntax:
                # st1 = {'item1', 'item2', 'item3', 'item4'}
                # st2 = {'item5', 'item6', 'item7', 'item8'}
                # st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

        # Update() method inserts a set into a given set
            # Syntax: 
                # st1 = {'item1', 'item2', 'item3', 'item4'}
                # st2 = {'item5', 'item6', 'item7', 'item8'}
                # st1.update(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

