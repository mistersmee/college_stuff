#!/usr/bin/env python
# encoding: utf-8

# 1. Write a program for Reversing of string.

string = input('Enter a string:')

print(f'The string reversed is {string[::-1]}')


# 2. Write a program to attach string1 to string2. take string1 as your first name and string2 as your lastname.

fname = input('Enter your first name:')
lname = input('Enter your last name:')

fname = fname + ' ' + lname

print(f'Your full name is {fname}')

# 3. Write a program to take user input your first name and convert it into captial & display it.

name = input('Enter your first name:')
capname = name.upper()

print(f'Your name in uppercase letters is: {capname}')
