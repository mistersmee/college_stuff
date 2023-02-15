#!/usr/bin/env python
# coding: utf-8

## Dictionaries

# Basic printing of values in dictionary

phonebook = { 'Chris' : '12345', 'Katie': '56789', 'Joanne': '219292824232' }

print(phonebook)
print(phonebook['Chris'])
print(phonebook['Katie'])
print(phonebook['Joanne'])

print(len(phonebook))


# Using get() to get value of a key

x = phonebook.get('Chris')
print(x)

# Using keys() to list all keys in the dictionary

x = phonebook.keys()
print(x)

# Using values() to list all values in the dictionary

x = phonebook.values()
print(x)

# Using the items function to list all items in dictionary

print(phonebook.items())

# Updating value of a value using dictionary_name[key] = new_value

phonebook['Chris'] = '555-1111'
print(phonebook)

# Updating value of a value using the update() function

phonebook.update({'Katie' : '555-2222'})
print(phonebook)

# Using the popitem() function

key, value = phonebook.popitem()
print(key, value)


# Trying to write duplicates in dictionary, but duplicates are not allowed
# The length is still shown as 2, and the last values are considered, i.e. 567 and 999

test = {'123' : '789', 'abc' : 'xyz', '123' : '567', 'abc' : '999'}
print(test)
print(len(test))

# Adding a new key-value pair using dict_name[new_key] = new_value

phonebook['Cassandra'] = '555-3333'
print(phonebook)
print(x)

# Checking for key using if statements

if 'Chris' in phonebook:
    print('Yes, Chris is in the phonebook.')

# Using the pop() function to nuke a specified key-value pair
phonebook.pop('Cassandra')
print(phonebook)

# Using the del() function to nuke a specific key-value pair

del phonebook['Chris']
print(phonebook)

#Using the clear() function to clear the dictionary

phonebook.clear()
print(phonebook)

# Dictionary comprehensions

numbers = [1, 2, 3, 4]
squares = {item:item**2 for item in numbers}
print(squares)

phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
phonebook_copy = {k:v for k,v in phonebook.items()}
print(phonebook_copy)

populations = {'New York': 8398748, 'Los Angeles': 3990456,
 'Chicago': 2705994,'Houston': 2325502,
 'Phoenix': 1660272, 'Philadelphia': 1584138}

largest = {k:v for k,v in populations.items() if v > 2000000}
print(largest)


## Sets

# Basic sets

set = {'apple', 'banana', 'cherry'}
print(set)
print(len(set))

set2 = {1,2,3,4,5,6,7,8}
set3 = {True, False, False, True}     #Duplicates are not allowed, only {False, True} printed.

print(set2)
print(set3)

set1 = {'abc',34,True,40, 'male'}

print(set1)

# Using type() function to determine the class type
print(type(set))

# Using for loop to print items in the set

set = {'apple', 'banana', 'cherry'}

for x in set:
    print(x)

# Using the add() function to add items to the set

set.add('orange')
print(set)

# Using update() to add items from another set

set.update(set1)
print(set)

# update() can also add items from lists and tuples

set = {'apple', 'banana', 'orange'}
list = ['pineapple', 'mango', 'papaya']
tuple = ['jackfruit', 'dragonfruit', 'kiwi']

set.update(list)
print(set)
set.update(tuple)
print(set)

# Using the remove() and the discard() function to remove items from the list
# discard() doesn't give an exception, whereas remove() throws a KeyError
# exception when we ask to remove an item which isn't present

set = {'apple', 'banana', 'orange'}
print(set)
set.remove('orange')
print(set)
set.discard('apple')
print(set)

# Using the pop function to remove the first item in the set when specific item is not specified

set = {'apple', 'banana', 'orange'}
print(set)
set.pop()
print(set)

# Using clear() to delete every item in the set

set.clear()
print(set)

# Union of a set
# You can use | to show union

set1 = { 'a', 'b', 'c'}
set2 = {'1', '2', '3'}

set3 = set1.union(set2)

print(set3)

# Intersection of a set
# You can use & to show intersection

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# Using the symmetric_difference_update() method

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# Using the symmetric_difference() method

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# Using difference() function
# You can also use '-', for eg, set3 = set1 - set2 for difference

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.difference(set2)
print(set3)

# Using the subset() and superset() functions
# You can also use <= to check for subset and >= to check for superse

set1 = {1, 2, 3, 4}
set2 = {2, 3}

print(set2.issubset(set1))
print(set1.issuperset(set2))

# Set comprehensions

set1 = {1, 2, 3, 4, 5}
set2 = {item for item in set1}
set3 = {item**2 for item in set1}

print(set2)
print(set3)
