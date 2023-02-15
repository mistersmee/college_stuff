#!/usr/bin/env python
# encoding: utf-8

# 1. Write a program to print Restaurant Name.
# Give choice to user- 1.Veg   2.NonVeg.
# If Veg: print menu list as 1: Paneer tikka=100rs 2: Palak Paneer=150rs 3.Paneer kabab=200rs 4.roti=20rs
# if user chooses 2 dish print the bill. for example if user choose 1st and 2nd dish the bill will be 250rs.
# same for the choice non veg. display some non veg dish and on the user choice print the bill.
# note: using input validation loop.



print('Welcome to Tasty Foods Restaurant!')

veg = int(input('Enter your choice of food [1: Veg / 2: NonVeg]:'))

while not veg in (1, 2):
    print ("You must enter 1 for Veg and 2 for NonVeg!")
    veg = int(input('Enter your choice of food [1: Veg / 2: NonVeg]:'))

bill = 0

if veg == 1:
    print(f'\nThe Veg menu is:'
          f'\n\t1: Paneer Tikka Masala:  Rs. 100'
          f'\n\t2: Palak Paneer:         Rs. 150'
          f'\n\t3. Paneer Kebab:         Rs. 200'
          f'\n\t4. Roti:                 Rs. 20')

    i = 0
    while i <= 1:
        dish = int(input('Enter a dish you want [1/2/3/4]:'))
        i += 1
        if dish == 1:
            bill += 100
        elif dish == 2:
            bill += 150
        elif dish == 3:
            bill += 200
        elif dish == 4:
            bill += 20
        else:
            print('Order number item not found.')
    print(f'Your bill is Rs. {bill}')
else:
    print(f'\nThe NonVeg menu is:'
          f'\n\t1: Mutton Biryani:   Rs. 500'
          f'\n\t2: Kolhapuri Mutton: Rs. 350'
          f'\n\t3. Chicken Kebab:    Rs. 200'
          f'\n\t4. Roti:             Rs. 20')

    i = 0
    while i <= 1:
        dish = int(input('Enter a dish you want [1/2/3/4]:'))
        i += 1
        if dish == 1:
            bill += 500
        elif dish == 2:
            bill += 350
        elif dish == 3:
            bill += 200
        elif dish == 4:
            bill += 20
        else:
            print('Order number item not found.')
    print(f'Your bill is Rs. {bill}')


#2. Sum of Numbers
# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series.
#  After all the positive numbers have been entered, the program should display their sum.

i = 0
sum = 0

while i >= 0:
    i = int(input('Enter positive numbers:'))
    if i > 0:
        sum += i
    else:
        print('Negative number entered, stopping series.')
        break

print(f'The sum of the series of entered numbers is {sum}.')
