#!/usr/bin/env python
# coding: utf-8

# 1. Write a program performing operations on 3 user defined functions as below with following properties:
# add() : Function with no arguments, no return type
# sub() : Function with arguments, no return type
# mul() : Function with arguments, return type
# div() : Function with no arguments, return type

def add():
    num1 = 50
    num2 = 2025325

    sum = num1 + num2

    print(sum)

add()

def sub(num1,num2):
    num1 = num1
    num2 = num2

    sub = num1 - num2

    print(sub)

num1 = int(input('Enter a number:'))
num2 = int(input('Enter another number:'))

sub(num1, num2)

def mul(num1, num2):
    num1 = num1
    num2 = num2

    mul = num1 * num2

    return mul

num1 = int(input('Enter a number:'))
num2 = int(input('Enter another number:'))

print(mul(num1, num2))

def div():
    num1 = 500
    num2 = 100

    div = num1 / num2

    return div

print(div())

# 2. Write a program using function to add data in list 5 times & print the list.

def get_total(value_list):
    total = 0

    for i in range(0,5):
        for s in value_list:
            total += s

    return total

numbers = []
k = 'y'
while k == 'y':
    s = int(input('Enter a number:'))
    numbers.append(s)
    k = input('Do you want to enter more numbers?[y/n]:')

print(numbers)
print(f'The total added 5 times is {get_total(numbers)}.')

# 3. Write a program using function to find Sum of Digits of a Number using functions.

def digsum(num):
    total = 0
    div = 0

    while num > 0:
        div = num % 10
        total += div
        num = num // 10

    return total

num1 = int(input('Enter a number:'))

print(f'The sum of digits of the number is {digsum(num1)}')

# 4. Declare a function city () and call Pune and Kolhapur function.
#  In Pune take user input name and age of Pune citizen and print if he is eligible for voting or not.
# Same apply for Kolhapur people.

def city(cname):

    if cname == 'Pune':
        name = input('Enter your name:')
        age = int(input('Enter your age:'))

        if age > 18:
            print('You are eligible for voting.')
        else:
            print('You are not eligible for voting.')

    elif cname == 'Kolhapur':

        name = input('Enter your name:')
        age = int(input('Enter your age:'))

        if age > 18:
            print('You are eligible for voting.')
        else:
            print('You are not eligible for voting.')

town = input('Enter the name of the city [Pune/Kolhapur]:')

while town not in ('Pune','Kolhapur'):
    print('Invalid city name, please enter only "Pune" or "Kolhapur".')
    town = input('Enter the name of the city [Pune/Kolhapur]:')

city(town)

# 5. Write a program using factions to print the item=bread and
# topping should have multiple values inputted by user such as butter, cheese, jam, chocolate syrup etc

def food(top):
    item = 'bread'

    print(f'item = {item}')
    print('Toppings:')

    for s in top:
        print(f'\t{s}')

k = 'y'
toppings = []

while k == 'y':
    print("Let's make a sandwich!")
    t = input('Enter a topping:')
    toppings.append(t)
    k = input('Do you want to add more toppings?[y/n]:')

food(toppings)
