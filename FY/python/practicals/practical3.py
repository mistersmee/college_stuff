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
        print(f'You must have been employed '
              f'for at least {MIN_YEARS} '
              f'years to qualify.')
else:
    print(f'You must earn at least $'
          f'{MIN_SALARY:,.2f} '
          f'per year to qualify.')

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

month = int(input('Enter the month number:'))
year = int(input('Enter the year:'))

if(month == '1','3','5','7','9','11'):
    print('Number of days is 11')
elif((month ==2) and ((year % 400 == 0) or (year%4 == 0 and year%100!=0))):
     print('Number of days is 29')
else:
     print('Number of days is 30')

ch = input('Enter a character:')

if(ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch =='I' or ch == 'i' or ch == 'O' or ch =='o' or ch == 'U' or ch == 'u'):
    print(ch, 'is a vowel')
else:
    print(ch, 'is a consonant')
