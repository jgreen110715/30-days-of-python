# Day 4
import math

# Strings
# Escape Sequences in Strings

print('I hope everyone is enjoying the Pythong Challenge. \n Are you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash symbol (\\)')
print('In every programming language, it starts with \"Hello, World\"')

# String formatting
# strings only

first_name = 'Jon'
last_name = 'Green'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)

print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius **2
formated_string = 'The area of a circle with a radius %d is %.2f.' %(radius, area)

print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' %(python_libraries)

print(formated_string)

# New Style String Formatting (str.format)

first_name = 'Jon'
last_name = 'Green'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)

print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# String Interpolation / f-Strings
a = 4
b = 3

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Python Strings as Sequences of Characters

# Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# Slicing Python Strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but doesn't include 3
print(first_three)
last_three = language[3:6]
print(last_three)
# Another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)

# Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] # index 0 - 6 by 2s
print(pto)

# String Methods

#capitalize(): Converts the first character of the string to capital letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): Returns the index of the first occurrence of a substring, if not found returns -1

challenge = 'thirty days of python'
print(challenge.find('y')) # 5
print(challenge.find('th')) # 0

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1

challenge = 'thirty days of python'
print(challenge.rfind('y')) # 16
print(challenge.rfind('th')) # 17

# format(): formats string into a nicer output

first_name = 'Jon'
last_name = 'Green'
age = 34
job = 'Engineer'
country = 'USA'
sentence = 'I am {} {}. I am {} years old. I am an {}. I live in the {}'.format(first_name, last_name, age, job, country)
print(sentence)

radius = 10
area = math.pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) # 7
print(challenge.index(sub_string, 9))

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string)) # 7
print(challenge.rindex(sub_string, 9))

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumric character

challenge = 'thirty days of python 2023'
print(challenge.isalnum()) # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha()) # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)

challenge = 'thirty days of python'
print(challenge.isdecimal()) # False
challenge = '123'
print(challenge.isdecimal()) # True
challenge = '\u00B2'
print(challenge.isdecimal()) # False
challenge = '12 3'
print(challenge.isdecimal()) # False, space is not allowed

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit()) # True
challenge = '\u00B2'
print(challenge.isdigit()) # True

# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # 1/2
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase

challenge = ' thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase

challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React#'

# strip(): Removes all given characters starting from the beginning and end of the string

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty day of py'

# replace(): Replaces substring with a given string

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): Splits the string, using given string or space as a separator

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters

challenge = 'thirty days of python'
print(challenge.swapcase()) # THIRTY DAYS OF PYTHON

challenge = 'Thirty Days Of Python'
print(challenge.swapcase()) # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False