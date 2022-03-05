#!/usr/bin/env python
# coding: utf-8

## Lists

# Basic list

a = [1, 2.2, 'kit']

print(a)

# Print element from list
print(a[1])

# Use while loop to print elements from the list

s = [1, 2.2, 5.5, 6.6, 'abc', 'xyz']
i = 0

while i < len(s):
    print(f'At index {i},element is {s[i]}')
    i += 1
    
# Use for loop to print elements from the list
for i in s:
    print(i)

# Square the elements in the list

a = [1, 2, 3, 4, 5, 6, 7, 8]

for i in a:
    sq = i * i
    print(sq)

# Slicing lists

s = ['p', 'y', 't', 'h', 'o', 'n']

print(s)
print(s[1:3])
print(s[2:])
print(s[:-5])
print(s[:])
print(s[::-1])

# Appending a list

s.append(122)

print(s)

# Using while loop to append elements to a list

a = ['zoo', 'star']
i = 1

while i <= 5:
    value = input()
    a.append(value)
    i += 1
print(a)

# Inserting elements into lists

subject = ['English', 'Maths', 'Marathi', 'Science']

print(subject)

subject.insert(2,'Hindi')

print(subject)

subject.insert(3,'History')

print(subject)

# Extending lists

list1 = [10, 20, 30]
list2 = [15, 35, 77, 88, 90]

print(f'Before using the extend function, list 1 is: {list1}')

list1.extend(list2)

print(f'After using the extend function, list 2 is: {list1}')

# Deleting/Popping elememnts from list
# Clearing a lists

s = ['p', 'y', 't', 'h', 'o', 'n']

print(s)

del(s[1])

print(s)

s.pop()

print(s)

s.clear()

print(s)

# Sorting and reversing lists

s = [22, 1, 5, 4, 2, 66, 12]

s.sort()

print(s)

s.reverse()

print(s)

# Index function of a list

t = [22, 33 , 44, 55, 66, 77, 88, 99]

print(t.index(88))
print(t)

# Nested lists

list3 = [10, 20, [30, 49, 88], 7, ['kit', 'coek']]

for i in list3:
    print(i)

# Printing nested list using while loop & Printing sub-elements of nested lists

list3 = [10, 20, [30, 49, 88], 7, ['kit', 'coek']]
i = 0

while i < len(list3):
    print(list3[i])
    i += 1

print(list3)
print(list3[2][1])
print(list3[2][2])
print(list3[4][1])

# Searching in list for a specific element using for loop and if condition

test = [1, 6, 3, 5, 4, 2]

for i in test:
    if i == 4:
        print('Element present.')
    else:
        print('Element absent.')
        
if 4 in test:
    print('Element present.')


# Using copy function on lists and concatenating lists

list1 = [1, 2, 3, 4, 5, 6, 7]

list2 = list1.copy()

print(list2)

list2.clear()

print(list2)

list2 += list1

print(list2)


# Repitition operator on lists

numbers = [0] * 5

print(numbers)

# Using for loop and range and length functions to print elements from lists

s = [1, 2.2, 5.5, 6.6, 'abc', 'xyz']

for i  in range(len(s)):
    print(f'At index {i},element is {s[i]}')

## Tuples

# Basic tuples

thistuple = ("apple", "banana", "cherry")

print(thistuple)

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

# An empty tuple

empty_tuple = ()

print (empty_tuple)

# Creating non-empty tuples
 
tup = ('python', 'geeks')

print(tup)

# Code for concatenating 2 tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
 
print(tuple1 + tuple2)

# Code for creating nested tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)

print(tuple3)

# code to test slicing
 
tuple1 = (0 ,1, 2, 3)

print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])

# Code for printing the length of a tuple
 
tuple2 = ('python', 'geek')

print(len(tuple2))

thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Using the list and tuple functions to convert from tuples to lists and from lists to tuples

number_tuple = (1, 2, 3)

number_list = list(number_tuple)

print(number_list)

str_list = ['one', 'two', 'three']

str_tuple = tuple(str_list)

print(str_tuple)


## Dictionaries


# Basic dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

for i in thisdict:
    print(f'at key {i} value is {thisdict[i]}')

d = {1:10, 2:20, 3:30}
d[1] = 100

print(d)
