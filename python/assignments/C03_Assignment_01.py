#!/usr/bin/env python
# coding: utf-8

# 1. Print “Hello world”

print("Hello world!")

# 2. Print “Welcome to ‘KIT’”

print("Welcome to 'KIT'")

# 3. Perform all arithmetic operations (Addition (+), Subtraction (-), Multiplication (*), division (/), Exponent (**) and
# modulo (%)) on any numbers (Choose appropriate data)

num1 = 30
num2 = 20

add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
exp = num1 ** num2
mod = num1 % num2

print("The addition of two numbers",num1,"and",num2,"is:",add)
print("The subtraction of two numbers",num1,"and",num2," is:",sub)
print("The multiplication of two numbers",num1,"and",num2," is:",mult)
print("The division of two numbers",num1,"and",num2," is:",div)
print("The exponent of",num1,"to the power of",num2,"is:",exp)
print("The modulo (remainder after the division) of two numbers",num1,"and",num2," is:",mod)

# 4. Calculate Area of Circle , Triangle ,Rectangle and Square

## Area of circle

pi = 3.14
r = 10

area = pi * r * r

print("The area of a circle with radius",r,"is:",area)


## Area of triangle


b = 100
h = 50

area = 0.5 * b * h

print("The area of a triangle with base",b,"and height",h,"is:",area)


## Area of square


l = 100

area = l * l

print("The area of a square with lengths of the sides",l,"is:",area)


## Area of rectangle


l = 10
b = 10

area = l * b

print("The area of a rectangle with length",l,"and breadth",b,"is:",area)


# 5. Calculate Perimeter of Circle, Triangle, Rectangle and Square.


## Perimeter of circle

pi = 3.14
r = 10

peri = pi * 2 * r

print("The perimeter/circumference of the circle with radius",r,"is:",peri)


# Perimeter of triangle

side1 = 500
side2 = 450
side3 = 250

peri = side1 + side2 + side3

print("The perimeter of the triangle with sides",side1, side2, side3,"is:",peri)


# Perimeter of square


l = 100

peri = l * 4

print("The perimeter of a square with sides",l,"is:",peri)


# Perimeter of rectangle


l = 90
b = 70

peri = 2 * (l + b)

print("The perimeter of a rectangle with length",l,"and breadth",b,"is:",peri)

# 6. Perform Swapping of two variable values :
# Example:
# Before swapping
# a =20 and b =10
# After swapping
# a=10 and b=20

num1 = 30
num2 = 60

print("The value of number 1 is",num1, "and that of number 2 is",num2)

temp = num1
num1 = num2
num2 = temp

print("After interchange, the value of number 1 is",num1, "and that of number 2 is",num2)


# 7. Perform Python Program to Convert Kilometers to Miles. ( 1 kilometer = 0.621371 miles)

km_dist = 231

mil_mult = 0.621371

mil_dist = km_dist * mil_mult

print("Your travelled",km_dist,"km distance in miles is:",mil_dist)


# 8. Write a Python Program to Convert Celsius To Fahrenheit.


cel_temp = 24

fah_temp = ( 1.8 * cel_temp ) +32

print("Your temperature",cel_temp,"°C in Fahrenheit is:",fah_temp, "°F")
