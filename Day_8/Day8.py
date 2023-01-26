# Day 7
import math

# Dictionaries
    # A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary
    # To create a disctionary we use curly brackets {} or the dict() built0in function
        # Syntax:
            # empty_dict = {}
        # dictionary with data values
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {'first_name' : 'Jon',
          'last_name' : 'Green',
          'age' : 34,
          'country' : 'USA',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
            'street' : 'Commonwealth Ave',
            'zip_code' : '02763',
          } 
         }

    # The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

# Dictionary Length
    # It checks the number of 'key:value' pairs in the dictionary
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # print(len(dct))

person = {'first_name' : 'Jon',
          'last_name' : 'Green',
          'age' : 34,
          'country' : 'USA',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
            'street' : 'Commonwealth Ave',
            'zip_code' : '02763',
          } 
         }
print(len(person))

# Accessing Dictionary Items
    # We can access Dictionary items by referring to its key name.
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # print(dct['key1'])
                # value1
            # print(dct['key4'])
                # value4

person = {'first_name' : 'Jon',
          'last_name' : 'Green',
          'age' : 34,
          'country' : 'USA',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
            'street' : 'Commonwealth Ave',
            'zip_code' : '02763',
          } 
         }
print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
# print(person['city'])

    # Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.

person = {'first_name' : 'Jon',
          'last_name' : 'Green',
          'age' : 34,
          'country' : 'USA',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
            'street' : 'Commonwealth Ave',
            'zip_code' : '02763',
          } 
         }
print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))

# Adding items to a Dictionary
    # We can add a new key and value pair to a dictionary
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # dct['key5'] = 'value5'

person = {'first_name' : 'Jon',
          'last_name' : 'Green',
          'age' : 34,
          'country' : 'USA',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
            'street' : 'Commonwealth Ave',
            'zip_code' : '02763',
          } 
         }
person['job_title'] = 'Engineer'
person['skills'].append('HTML')
print(person)

# Modifying items in a Dictionary
    # Syntax:
        # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        # dct['key1'] = 'value-one'

person = {'first_name' : 'Jon',
          'last_name' : 'Green',
          'age' : 34,
          'country' : 'USA',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
            'street' : 'Commonwealth Ave',
            'zip_code' : '02763',
          } 
         }
person['first_name'] = 'Jonathan'
person['age'] = 35

# Checking Keys in a Dictionary
    # We use the in operator to check if a key exists in a dictionary
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # print('key2' in dct)
                # True
            # print('key5' in dct)
                # False

# Removing Key and Value Pairs from a Dictionary
    # pop(key): removes the item with the specified key name
    # popitem(): removes the last item
    # del: removes an item with specified key name
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # dct.pop('key1')

            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # dct.popitem()

            # del dct['key2']

person = {'first_name' : 'Jon',
          'last_name' : 'Green',
          'age' : 34,
          'country' : 'USA',
          'is_married' : True,
          'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
          'address' : {
            'street' : 'Commonwealth Ave',
            'zip_code' : '02763',
          } 
         }

person.pop('first_name')
person.popitem()
del person['is_married']
print(person)

# Changing Dictionary to a List
    # the items() method changes dictionary to a list of tuples
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # print(dct.items())

# Clearing a Dictionary
    # If we don't want the items in a dictionary we an clear them using the clear() method
        # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        # print(dct.clear())

# Deleting a Dictionary
    # If we do not use the dictionary, we can delete it completely
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # del dct

# Copying a Dictionary
    # We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # dct_copy = dct.copy()

# Getting Dictionary Keys as a List
    # The keys () method gives us all the keys of a dictionary as a list
        # Syntax: dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        # keys = dct.keys()
        # print(keys)

# Getting Dictionary Values as a List
    # The values method gives us all the values of a dictionary as a list
        # Syntax:
            # dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
            # values = dct.values()
            # print(values)
            