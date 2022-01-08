#!/usr/bin/env python
# coding: utf-8

# Swapping values of two variables

num1 = 30
num2 = 60

print("The value of number 1 is",num1, "and that of number 2 is",num2)

temp = num1
num1 = num2
num2 = temp

print("After interchange, the value of number 1 is",num1, "and that of number 2 is",num2)

# Input operations

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

add = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2
mod = num1%num2

print("The addition of the given numbers is:",add)
print("The subtraction of the given numbers is:",sub)
print("The multiplication of the given numbers is:",mult)
print("The division of the given numbers is:",div)
print("The modulo (remainder of their division) of the given numbers is:",mod)


# Area of circle

pi = float(input("Enter the value of pi:"))
r = int(input("Enter the radius of the circle:"))

area = pi*r*r

print("The area of the circle with radius",r,"is:",area)


# Area of triangle


b = int(input("Enter the value of base of the triangle:"))
h = int(input("Enter the value of height of the triangle:"))

area = 0.5*b*h

print("The area of a triangle with base",b,"and height",h,"is:",area)


# Area of square


l = int(input("Enter the value of the length of a side of a square:"))

area = l*l

print("The area of a square with sides",l,"is:",area)


# Area of rectangle


l = int(input("Enter the value of the length of a rectangle:"))
b = int(input("Enter the value of the breadth of a rectangle:"))

area = l*b

print("The area of a rectangle with length",l,"and breadth",b,"is:",area)


# Simple interest

prin = int(input("Enter the value of principal amount:"))
yrs = int(input("Enter the time period of the investment:"))
rate = float(input("Enter the rate of simple interest:"))

si = (prin*yrs*rate)/100

print("The simple interest on your investment is:",si)

# Swapping with Input

num1 = float(input("Enter one number:"))
num2 = float(input("Enter another number:"))

print("The value of number 1 is",num1, "and that of number 2 is",num2)

temp = num1
num1 = num2
num2 = temp

print("After interchange, the value of number 1 is",num1, "and that of number 2 is",num2)

# Average of 5 numbers with Input

num1 = float(input("Enter the marks scored in subject 1:"))
num2 = float(input("Enter the marks scored in subject 2:"))
num3 = float(input("Enter the marks scored in subject 3:"))
num4 = float(input("Enter the marks scored in subject 4:"))
num5 = float(input("Enter the marks scored in subject 5:"))

avg = (num1+num2+num3+num4+num5)/5

print("The average of 5 numbers",num1,",",num2,",",num3,",",num4,",",num5,"is:",avg)

# Program to get three test scores and display their average, and congratulates user if the average is a high score
# Example program for 'if'

HIGH_SCORE = 95

test1 = int(input("Enter the score for test 1:"))
test2 = int(input("Enter the score for test 2:"))
test3 = int(input("Enter the score for test 3:"))

avg = (test1+test2+test3)/3

print("The average score is:",avg)

if avg >= HIGH_SCORE:
    print("Congratulations!")
    print("That is a great average!")

# Program to check if number is even or odd, demo for if-else

num = int(input("Enter a number:"))

if (num%2==0):
    print("The given number is even.")
else:
    print("The number is odd.")

# Program to calculate overtime

base_hrs = 40
ot_multiplier = 1.5

hrs = float(input("Enter the number of hours worked:"))
pay_rate = float(input("Enter the hourly pay rate:"))

if hrs>base_hrs:
    ot_hrs = hrs - base_hrs
    ot_pay = ot_hrs * pay_rate * ot_multiplier
    gross_pay = base_hrs * pay_rate + ot_pay
else:
    gross_pay = hrs * pay_rate

print("The gross pay is $", format(gross_pay, ',.2f'), sep='')
