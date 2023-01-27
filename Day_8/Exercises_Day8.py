# Day 8: 30 Days of python programming
import math
import statistics

# Exercises: Day 7 Dictionaries

# 1. Create an empty dictionary called dog

dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Buggy'
dog['color'] = 'White'
dog['breed'] = 'Great Pyrenees'
dog['legs'] = 4
dog['age'] = 2
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name' : 'Jon',
    'last_name' : 'Green',
    'gender' : 'Male',
    'age' : 34,
    'marital_status' : True,
    'skills' : ['Python', 'C#', 'Java'],
    'country' : 'USA',
    'city' : 'Attleboro Falls',
    'address' : 'home'
    }
print(student)

# 4. Get the length of the student dictionary

print(len(student))

# 5. Get the value of skills and check the data type, it should be a list

print(student.get('skills'))
print(type(student.get('skills')))

# 6. Modify the skills values by adding one or two skills

student['skills'].append('HTML')
student['skills'].append('funny') 
print(student.get('skills'))

# 7. Get the dictionary keys as a list

keys = student.keys()
print(keys)

# 8. Get the dictionary values as a list

values = student.values()
print(values)

# 9. Change the dictionary to a list of tuples using items() method

print('dictionary as a list:', student.items())

# 10. Delete one of the items in the dictionary

student.pop('address')

# 11. Delete one of the dictionaries

del dog