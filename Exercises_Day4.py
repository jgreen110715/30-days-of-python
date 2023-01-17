# Day 4: 30 Days of python programming
import math

# Exercises: Day 4 Strings

# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
e = ' '
f = a + e + b + e + c + e + d
print(f)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

web_course = ['Coding', 'For', 'All']
result = ' '.join(web_course)
print(result)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".

company = result

# 4. Print the variable company using print().

print(company)

# 5. Print the length of the company string using len() method and print().

print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.

print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.

print(company.lower()) 

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.

print(company[7:])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.find('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
pyForAll = company.replace('Coding', 'Python')
print(pyForAll)

# 12. Change Python for All to Python for Everyone using the replace method or other methods.

pyForEveryone = pyForAll.replace('All', 'Everyone')
print(pyForEveryone)

# 13. Split the string 'Coding For All' using space as the separator (split()) .

print(company.split(' '))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

tech_comp = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(tech_comp.split(', '))

# 15. What is the character at index 0 in the string Coding For All.

print(company[0])

# 16. What is the last index of the string Coding For All.

last_index = len(company) - 1
print(last_index)

# 17. What character is at index 10 in "Coding For All" string.

print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

pyForAll = 'Python For Everyone'
p = pyForAll[pyForAll.find('P')]
f = pyForAll[pyForAll.find('F')]
e = pyForAll[pyForAll.find('E')]
pfe = p + f + e

print(pfe)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.

codingForAll = 'Coding For All'
c = codingForAll[codingForAll.find('C')]
f = codingForAll[codingForAll.find('F')]
a = codingForAll[codingForAll.find('A')]
cfa = c + f + a

print(cfa)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.

print(codingForAll.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.

print(codingForAll.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.

print(codingForAll.rindex('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

twentyThree = 'You cannot end a sentence with because because because is a conjunction.'

first_occ = twentyThree.index('because')
print(first_occ)

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

last_occ = twentyThree.rfind('e') + 2
print(last_occ)

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

first_phrase = twentyThree[:first_occ]
last_phrase = twentyThree[last_occ:]

print(first_phrase + last_phrase)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(first_occ)

# 27. Does 'Coding For All' start with a substring Coding?

a = 'Coding For All'

print(a.startswith('Coding'))

# 28. Does 'Coding For All' end with a substring coding?

print(a.endswith('Coding'))

# 29. '   Coding For All      '  , remove the left and right trailing spaces in the given string.

a = '   Coding For All      '
c = a.find('C')
d = a.find('All') + 3
print( c , d)
result = a[c:d]
print(result)

# 30. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

print('thirty_days_of_python returns True when using the isidentifier method.')

# 31. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

pyLib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(pyLib)

print(result)

#32. Use the new line escape sequence to separate the following sentences

nLine = 'I am enjoying this challenge.\nI just wonder what is next'

print(nLine)

# 33. Use a tab escape sequence to write the following lines.

tab = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'

print(tab)

# 34. Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
sentence = 'The area of a circle with radius {} is {} meters square'.format(radius, area)

print(sentence)

# 35. Make the following using string formatting methods:

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
