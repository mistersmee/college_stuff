#!/usr/bin/env python
# encoding: utf-8

# 1. Write a program to create a file (your name.txt) in write mode. Add data like your name and roll number.

file = open('aseem.txt', 'w')

file.write('Aseem Athale\n')
file.write('C03\n')

file.close()

# 2. Write a code to add your PRN into exisiting file.

try:
    f = open('prn.txt')
    f.close()

except FileNotFoundError:
    print("File doesn't exist. FileNotFoundError occured.")

    print('Creating file now.')

    f = open('prn.txt', 'w')
    f.close()

    print('prn.txt created.')

    f = open('prn.txt', 'a')

    f.write(input('Enter your PRN:'))

    f.close()
