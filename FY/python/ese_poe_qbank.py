#!/usr/bin/env python
# encoding: utf-8

# P1

list1 = []
p = 0
n = 0
i = 0
index = 0

keep_going = 'y'
while keep_going == 'y':
    num1 = int(input('Enter a number:'))
    list1.append(num1)
    keep_going = input('Add more numbers?[y/n]:')

while i < len(list1):
    index = list1[i]
    if index > 0:
        p += 1
    else:
        n += 1
    i += 1

print(f'Positive numbers: {p}')
print(f'Negative numbers: {n}')

# P2

num = int(input('Enter a number:'))
rem = 0
rnum = 0

while num > 0:
    rem = num % 10
    rnum = (rnum * 10) + rem
    num = num // 10

print(rnum)

# P3

for i in range(1,6):
    for j in range(1, i + 1):
        print('*', end = '')
    print('\r')
for i in range(5 , 0, -1):
    for j in range(0, i -1):
        print('*', end='')
    print('\r')

# P4

list2 = []
i = 0
index = 0

keep_going = 'y'
while keep_going == 'y':
    num1 = int(input('Enter a number:'))
    list2.append(num1)
    keep_going = input('Add more numbers?[y/n]:')

while i < len(list2):
    index = list2[i]
    if index % 2 == 0:
        print(f'{index} is even.')
    else:
        print(f'{index} is odd.')
    i += 1

# P5

fact = 1
num = int(input('Enter a number:'))

for i in range(1, num + 1):
    fact = fact * i

print(f'The factorial of {num} is {fact}')


# P6

list3 = []
i = 0
index = 0

keep_going = 'y'
while keep_going == 'y':
    num1 = int(input('Enter a number:'))
    list3.append(num1)
    keep_going = input('Add more numbers?[y/n]:')

while i < len(list3):
    index = list3[i]
    if index % 5 == 0:
        print(f'{index} is divisible by 5.')
    else:
        print(f'{index} is not divisible by 5.')
    i += 1

# P7

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
    
    keep_going = 'y'
    while keep_going == 'y':
        dish = int(input('Enter a dish you want [1/2/3/4]:'))
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
        keep_going = input('Do you want to order more dishes?[y/n]:')
    print(f'Your bill is Rs. {bill}')
else:
    print(f'\nThe NonVeg menu is:'
          f'\n\t1: Mutton Biryani:   Rs. 500'
          f'\n\t2: Kolhapuri Mutton: Rs. 350'
          f'\n\t3. Chicken Kebab:    Rs. 200'
          f'\n\t4. Roti:             Rs. 20')
    
    keep_going = 'y'
    while keep_going == 'y':
        dish = int(input('Enter a dish you want [1/2/3/4]:'))
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
        keep_going = input('Do you want to order more dishes?[y/n]:')
    print(f'Your bill is Rs. {bill}')

# P8

A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

def calc_avg(*scores):
	avg = (score1 + score2 + score3 + score4 + score5) / 5
	return avg

def determine_grade(score):
    if score >= A_SCORE:
        print('Your grade is A.')
    elif score >= B_SCORE:
        print('Your grade is B.')
    elif score >= C_SCORE:
        print('Your grade is C.')
    elif score >= D_SCORE:
        print('Your grade is D.')
    else:
        print('Your grade is F.')
    
score1 = int(input('Enter score of test 1:'))    
score2 = int(input('Enter score of test 2:'))  
score3 = int(input('Enter score of test 3:'))  
score4 = int(input('Enter score of test 4:'))  
score5 = int(input('Enter score of test 5:')) 

avg = calc_avg(score1,score2,score3,score4,score5)
determine_grade(avg)


# P9

for i in range(1,6):
    for j in range(1, i + 1):
        print('*', end = '')
    print('\r')

# P10

for i in range(5 , 0, -1):
    for j in range(0, i -1):
        print('*', end='')
    print('\r')

# P11

n = int(input("Enter the number of rows: "))
m = (2 * n) - 2
for i in range(0, n):
    for j in range(0, m):
        print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")

# P12

def food(*top):
    item = 'bread'
    
    print(f'item = {item}')
    print('Toppings:')
    
    for s in top:
        print(f'\t{s}')

k = 'y'
toppings = []
print("Let's make a sandwich!")

while k == 'y':
    t = input('Enter a topping:')
    toppings.append(t)
    k = input('Do you want to add more toppings?[y/n]:')

food(toppings)

# P13

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

# P14

print('Welcome to Medical Store!')

bill = 0

print(f'Medicines for diseases:')
print(f'\n\t1. Fever\n\t2.Cough and Cold\n\t3.Headache\n\t4.Chest pain')
keep_going = 'y'
while keep_going == 'y':
        med = int(input('Choose which disease you want medicine for[1/2/3/4]:'))
        if med == 1:
            print('Medicine is: Paracetamol: Rs. 50')
            bill += 50
        elif med == 2:
            print('Medicine is: Azithromycin: Rs. 100')
            bill += 100
        elif med == 3:
            print('Medicine is: Crocin: Rs. 20')
            bill += 20
        elif med == 4:
            print('Medicine is: Nurokind: Rs. 500')
            bill += 500
        else:
            print('Medicine not available for selected disease.')
        keep_going = input('Do you want to buy more medicine?[y/n]:')
print(f'Your bill is Rs. {bill}')

# P15

def prime():
    for Number in range (1, 51):
        count = 0
        for i in range(2, (Number//2 + 1)):
            if(Number % i == 0):
                count = count + 1
                break

        if (count == 0 and Number != 1):
            print("%d" %Number, end = ' ')

prime()

# P16

try:
    f = open('aseem.txt')
    f.close()

except FileNotFoundError:
    print("File doesn't exist. FileNotFoundError occured.")
    print('Creating file now.')
    
    f = open('aseem.txt', 'w')
    f.close()
    
    print('aseem.txt created.')
    f = open('aseem.txt', 'w')
    
    f.write('Aseem Athale\n')
    f.write('C03\n')
    
    f.close()
    print('Wrote name and roll number to file.')

    f = open('aseem.txt', 'a')

    f.write(input('Enter your address:'))

    f.close()

else:
    f = open('aseem.txt', 'a')

    f.write(input('Enter your address:'))

    f.close()

# P17

def get_total(value_list):
    total = 0

    for i in range(0,6):
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
print(f'The total is {get_total(numbers)}.')

# P18

sales = []
i = 0

while i <= 6:
    value = input("Enter the store's sales for each day of the week:")
    sales.append(value)
    i += 1

total = 0

for s in range(len(sales)):
    total += int(sales[s])

print(f'The total sales of the store in a week is Rs.{total}')

# P19

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

# P20

for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print("%d" %Number, end = ' ')

# P21

num = int(input('Enter a number:'))
rem = 0
rnum = 0
add = 0

while num > 0:
    rem = num % 10
    rnum = (rnum * 10) + rem
    add += 1
    num = num // 10

print(rnum)
print(add)

# P22

n = 0
for i in range(5, 0, -1):
    n += 1   # assign value to n of i after each iteration
    for j in range(0, i):
        # print reduced value in each new line
        print(n, end=' ')
    print("\r")

# P23

def sumdig(num):
    rem = 0
    add = 0

    while num > 0:
        rem = num % 10
        add += 1
        num = num // 10
    print(rnum)
    print(add)

sumdig(int(input('Enter a number:')))

# P24

input_year = int(input("Enter the Year to be checked: "))
if (input_year%400 == 0):
          print("%d is a Leap Year" %input_year)
elif (input_year%100 == 0):
          print("%d is Not the Leap Year" %input_year)
elif (input_year%4 == 0):
          print("%d is a Leap Year" %input_year)
else:
          print("%d is Not the Leap Year" %input_year)

# P25

str1 = input('Enter a string:')
vow = 0
cons = 0
wht = 0
for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u') or (i == 'A' or i == 'I' or i == 'E' or i == 'O' or i == 'U'):
        vow += 1
    elif i == ' ' or i == '.':
        wht += 1
    else:
        cons += 1

print(f'There are {vow} vowels and {cons} consonants in the string.')

# P26

MyList = ["b", "a", "a", "c", "b", "a", "c", 'a']
res = {}

for i in MyList:
    res[i] = MyList.count(i)
    
print(res)

# P27

num1 = int(input('Enter a number:'))
num2 = int(input('Enter another number:'))
op = input('Enter the symbol of the operation you want to perform on the two numbers (+,-,*,/):')

if op == '+':
    add = num1 + num2
    print('The addition of the two numbers is:', add)
elif op == '-':
    sub = num1 - num2
    print('The subtraction of the two numbers is:', sub)
elif op == '*':
    mult = num1 * num2
    print('The multiplication of the two numbers is:', mult)
elif op == '/':
    div = num1 / num2
    print('The division of the two numbers is:', div)
else:
    print('Operation not permitted.')

# P28

def get_total(value_list):
    total = 0

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
print(f'The total is {get_total(numbers)}.')

srch = input('Enter the search item:')

if srch in numbers:
    print('Item present.')
else:
    print('Item not present.')

# P29

def listodd():
    numbers = []
    for i in range(0,10):
        s = int(input('Enter a number:'))
        numbers.append(s)

    for i in numbers:
        if i % 2 != 0:
            print(i)

listodd()

# P30

try:
    f = open('sales.txt','r')
    f.close()

except:
    print('sales.txt file not found.')
    k = input('Do you want to create sales.txt?[y/n]:')
    
    
    if k == 'y':
        print('Creating file now.')

        f = open('sales.txt','w')

        f.write('24987.62')
        f.write('26978.97')
        f.write('32589.45')
        f.write('31978.47')
        f.write('22781.76')
        f.write('29871.44')

        f.close()
    else:
        print('Exiting...')
        quit()

else:
    f = open('sales.txt','w')

    f.write('24987.62')
    f.write('26978.97')
    f.write('32589.45')
    f.write('31978.47')
    f.write('22781.76')
    f.write('29871.44')

    f.close()
    

# P31

month = int(input('Enter the month number:'))
year= int(input('Enter the year:'))
    
if((month == 2) and ((year % 4== 0)  or ((year %100 == 0) and (year % 400 == 0)))):
    print("Number of days is 29");

elif(month == 2):
    print("Number of days is 28");

elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("Number of days is 31");

else :
    print("Number of days is 30");

# P32

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

# P33

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

# P34

import random

kids = []
s = 0

print('This is a 6 player game.')

while s <= 5:
    names = input('Enter names of 6 kids playing the game:')
    kids.append(names)
    s += 1

leader = input('Choose a leader amongst the 6 kids:')

if leader in kids:
    print(f'The leader is {leader}')
    kids.remove(leader)

tc1 = 0
tc2 = 0
tc3 = 0
tc4 = 0
tc5 = 0

k = input('Do you want to start the game?[y/n]:')

while k =='y':
    j = random.choice(kids)
    
    c1 = j.count(kids[0])
    tc1 += c1
    
    c2 = j.count(kids[1])
    tc2 += c2
    
    c3 = j.count(kids[2])
    tc3 += c3
    
    c4 = j.count(kids[3])
    tc4 += c4
    
    c5 = j.count(kids[4])
    tc4 += c4

    print(f'The den is on {j}')
    k = input('Do you want to continue the game?[y/n]:')

print(f'The den was on {kids[0]} {tc1} times.')
print(f'The den was on {kids[1]} {tc2} times.')
print(f'The den was on {kids[2]} {tc3} times.')
print(f'The den was on {kids[3]} {tc4} times.')
print(f'The den was on {kids[4]} {tc5} times.')
