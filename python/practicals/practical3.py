#!/usr/bin/env python
# coding: utf-8

# Comparing strings

name1 = 'Mary'
name2 = 'Mark'

if name1 > name2:
    print('Mary is greater than Mark')
else:
    print('Mary is not greater than Mark')

# Comparing strings with password

# This program compares two strings.
# Get a password from the user.
password = input('Enter the password: ')

# Determine whether the correct password
# was entered.
if password == 'prospero':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')


# Nested if-else

# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.

years_on_job = int(input('Enter the number of ' + 'years employed: '))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed 'for at least {MIN_YEARS} 'years to qualify.')
else:
    print('You must earn at least $' '{MIN_SALARY:,.2f}' 'per year to qualify.')

# if-elif-else

# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Named constants to represent the grade thresholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

# Determine the grade.
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
