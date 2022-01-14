#!/usr/bin/env python
# coding: utf-8

# 1.1 Perform all arithmetic operations (Addition (+), Subtraction (-), Multiplication (*), division (/),
# Exponent (**) and modulo (%)) on any numbers (Choose appropriate data)

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
exp = num1 ** num2
mod = num1 % num2

print("The addition of the given numbers is:",add)
print("The subtraction of the given numbers is:",sub)
print("The multiplication of the given numbers is:",mult)
print("The division of the given numbers is:",div)
print("The exponent of",num1,"to the power of",num2,"is:",exp)
print("The modulo (remainder of their division) of the given numbers is:",mod)


# 1.2 Calculate Area of Circle, Triangle, Rectangle and Square.

## Area of circle

pi = 3.14
r = int(input("Enter the radius of the circle:"))

area = pi * r * r

print("The area of the circle with radius",r,"is:",area)


## Area of triangle


b = int(input("Enter the value of base of the triangle:"))
h = int(input("Enter the value of height of the triangle:"))

area = 0.5 * b * h

print("The area of a triangle with base",b,"and height",h,"is:",area)


## Area of square


l = int(input("Enter the value of the length of a side of a square:"))

area = l * l

print("The area of a square with sides",l,"is:",area)


## Area of rectangle


l = int(input("Enter the value of the length of a rectangle:"))
b = int(input("Enter the value of the breadth of a rectangle:"))

area = l * b

print("The area of a rectangle with length",l,"and breadth",b,"is:",area)


# 1.3 Calculate Perimeter of Circle, Triangle, Rectangle and Square.

## Perimeter of circle

pi = 3.14
r = int(input("Enter the radius of the circle:"))

peri = pi * 2 * r

print("The perimeter of the circle with radius",r,"is:",peri)


# Perimeter of triangle

side1 = float(input("Enter the value of side 1 of a triangle:"))
side2 = float(input("Enter the value of side 2 of a triangle:"))
side3 = float(input("Enter the value of side 3 of a triangle:"))

peri = side1 + side2 + side3

print("The perimeter of the triangle is:",peri)


# Perimeter of square


l = int(input("Enter the value of the length of a side of a square:"))

peri = l * 4

print("The perimeter of a square with sides",l,"is:",peri)


# Perimeter of rectangle


l = int(input("Enter the value of the length of a rectangle:"))
b = int(input("Enter the value of the breadth of a rectangle:"))

area = 2 * (l + b)

print("The perimeter of a rectangle with length",l,"and breadth",b,"is:",peri)

# 1.4 Perform Swapping of two variable values
# Example:
# Before swapping
# a =20 and b =10
# After swapping
# a=10 and b=20

num1 = float(input("Enter one number:"))
num2 = float(input("Enter another number:"))

print("The value of number 1 is",num1, "and that of number 2 is",num2)

temp = num1
num1 = num2
num2 = temp

print("After interchange, the value of number 1 is",num1, "and that of number 2 is",num2)

# 2. Perform Python Program to Convert Kilometers to Miles. ( 1 kilometer = 0.621371 miles)

km_dist = float(input("Enter the distance travelled in kilometers(km):"))
mil_mult = 0.621371
mil_dist = km_dist * mil_mult

print("Your travelled distance in miles is:",mil_dist)

# 3. Write a Python Program to Convert Celsius To Fahrenheit.

cel_temp = float(input("Enter the temperature in Celsius to be converted to Fahrenheit:"))
fah_temp = ( 1.8 * cel_temp ) +32

print("Your temperature in Fahrenheit is:",fah_temp, "°F")


# 4. Display your basic information in following format by using string , integer and float variables
# Basic Information:
# Name: “Your full name”
# Address: your permanent address here
# Mobile Number: 99******22
# Email ID: abc@kitcoek.in
# Marks of 3 Subjects: PCM group subject
# Average of PCM group – 77.78

name = input("Enter your full name:")
address = input("Enter your permanent address:")
mobile = int(input("Enter your mobile number:"))
email = input("Enter your email ID:")
num1 = float(input("Enter marks received in Physics:"))
num2 = float(input("Enter marks received in Chemistry:"))
num3 = float(input("Enter marks received in Maths:"))

avg = ( num1 + num2 + num3 ) / 3

print("Basic Information:")
print("Name:",name)
print("Address:",address)
print("Mobile Number:",mobile)
print("Email ID:",email)
print("Average marks of PCM group :",avg)

# 5. Write a python program to find out sale price of an Item.
# Suppose a retail business is planning to have a storewide sale where the prices of all items will be 20 percent
# off. We have been asked to write a program to calculate the sale price of an item after the discount is
# subtracted. (Take data from user side / from keyboard)

orig_price  = float(input("Enter the original price of the item:"))
disc_price = orig_price - ( 0.2 * orig_price )

print("The 20% off discounted price of the item is:",disc_price)

# 6. Write a python program to calculate the average of the three test scores. Perform the calculation and
# store the result in the average variable:
# Average = (test1 + test2 + test3) / 3.0

num1 = float(input("Enter the marks scored in subject 1:"))
num2 = float(input("Enter the marks scored in subject 2:"))
num3 = float(input("Enter the marks scored in subject 3:"))

avg = (num1 + num2 + num3 ) / 3

print("The average of your marks",num1,",",num2,",",num3,"is:",avg)


# 7. Write a python program to gets a number of seconds from the user, and it converts that number of
# seconds to hours, minutes, and seconds.
# For example, it would convert 11,730 seconds to 3 hours, 15 minutes, and 30 seconds.

total_sec = int(input("Enter number of seconds to be converted into H:M:S :"))
hr = total_sec / 3600
min = ( total_sec % 3600) / 60
sec = total_sec % 60

print(total_sec,"seconds in H:M:S format is:",int(hr),":",int(min),":",int(sec))
