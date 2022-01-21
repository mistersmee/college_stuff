#!/usr/bin/env python
# encoding: utf-8

# 1. Write a program to Calculate division obtain by student.

AP_SCORE = 80
A_SCORE = 75
B_SCORE = 60
C_SCORE = 45
D_SCORE = 35

# Get percentage from the user.
score = int(input('Enter your percentage: '))

# Determine the grade.
if score >= AP_SCORE:
    print('Your grade is A+.')
elif score >= A_SCORE:
    print('Your grade is A.')
elif score >= B_SCORE:
    print('Your grade is B.')
elif score >= C_SCORE:
    print('Your grade is C.')
elif score >= D_SCORE:
    print('Your grade is D.')
else:
    print('You have failed.')

# 2. Write a program for deciding Even/odd number.

num1 = int(input('Enter a number: '))

if num1 % 2 == 0:
    print('The given number is even.')
else:
    print('The number is odd.')

# 3. Write a program for finding largest of three numbers.
num1 = int(input('Enter a number:'))
num2 = int(input('Enter another number:'))
num3 = int(input('Enter another number:'))

if num1 > num2 and num1 > num3:
    print(num1,'is greater than', num2,'and', num3)
elif num2 > num1 and num2 > num3:
    print(num2,'is greater than', num1,'and', num3)
elif num3 > num2 and num3 > num1:
    print(num3,'is greater than', num2,'and', num1)
else:
    print('The given numbers are equal.')

# 4. Design and develop a program to read a year as an input and find
# whether it is leap year or not. Also consider end of the centuries.

year = int(input('Please enter a Year:'))

if ( year % 4 == 0 ):
    if ( year % 100 == 0 ):
        if ( year % 400 == 0):
            print('%d is a leap year' %year)
        else:
            print('%d is not a leap year' %year)
    else:
        print('%d is a leap year' %year)
else:
    print('%d is not a leap year' %year)

# 5.         Write a C program to input electricity unit charge and calculate the total electricity bill according to the given condition:
# ·        For first 50 units Rs. 0.50/unit
# ·        For next 100 units Rs. 0.75/unit
# ·        For next 100 units Rs. 1.20/unit
# ·        For unit above 250 Rs. 1.50/unit
# ·        An additional surcharge of 20% is added to the bill.

units = int(input('Enter your electricity usage units:'))

if units < 50:
    bill = 0.50 * units
    print('Your electricity bill is Rs. %f' %bill)
elif units >= 50 and units < 150:
    bill = 0.75 * units
    print('Your electricity bill is Rs. %f' %bill)
elif units >= 150 and units < 250:
    bill = 1.20 * units
    print('Your electricity bill is Rs. %f' %bill)
else:
    bill = 1.20 * units
    surch = 0.20 * bill
    bill = bill + surch
    print('Your electricity bill is Rs. %f' %bill)

# 6. Program for calculator which performs basic arithmetic operations like addition, subtraction, multiplication, division of a two number.
num1 = int(input('Enter a number:'))
num2 = int(input('Enter another number:'))
op = input('Enter the symbol of the operation you want to perform on the two numbers (+,-,*,/):')

if op == '+':
    add = num1 + num2
    print('The addition of the two numbers is:', add)
elif op == '-':
    sub = num1 - num2
    print('The subtraction of two numbers is:', sub)
elif op == '*':
    mult = num1 * num2
    print('The multiplication of two numbers is:', mult)
elif op == '/':
    div = num1 / num2
    print('The division of two numbers is:',div)

# 7. Write a program to display days in month based on user input month number.

month = int(input('Enter the month number:'))

if(month == '1' or month == '3'or month == '5' or month == '7' or month == '9' or month == '11'):
    print('Number of days is 31')
elif month == 2:
     print('Number of days is 28')
else:
     print('Number of days is 30')

# 8. Write a program to check given character is vowel or consonant.

ch = input('Enter an alphabetic character:')

if(ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch =='I' or ch == 'i' or ch == 'O' or ch =='o' or ch == 'U' or ch == 'u'):
    print(ch, 'is a vowel')
else:
    print(ch, 'is a consonant')

# 9. Write a program to check given username and password (both integer) if correct then display “Login Successfully” otherwise display “Try Again”.
login = int(input('Enter a numeric username:'))
password = int(input('Enter the numeric password: '))

if login == '812838938' and password == '832948924848':
    print('Login Successfully.')
else:
    print('Try Again')


# 10. Write a program for deciding candidate is eligible for marriage or not (Consider gender also M/F).

gen = input('Enter your gender (M/F):')
age = int(input('Enter your age:'))

if gen == 'M' and age > 21:
    print('You are eligible for marriage.')
elif gen == 'F' and age > 18:
    print('You are eligible for marriage.')
else:
    print('You are not eligible for marriage.')
