# write a python program to accept a string value and display the reverse of it
# write a python program to read a 4 digit number and display the sum of the digits
# write a program to read a string and check if it is palindrome
# write a python program to accept a 5 digit number and display the reverse of

string =input("enter a string: ")
reverse_string=string[::-1]

print("revrese string is", reverse_string )

string =input("enter a string: ")
reverse_string=string[::-1]

if string == reverse_string:
        print ("this string is palindrome.")

else :
    print("entered string is not a palindrome.")

def add (x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def div(X,Y):
    return x/y


def ello():

    print("1.additon\n2.subtraction\n3.multiply\n4.division")
    choice = int(input ("enter no : "))
    a = int(input ("enter first no : "))
    b = int(input ("enter second no : "))



    if choice == 1:
        print  ("display addition: ",add(a,b))
    elif choice == 2:
        print  ("display subtraction: ",sub(a,b))

    elif choice == 3:
        print  ("display multiply: ",multiply(a,b))

    elif choice == 4:
        print  ("display division: ",div(a,b))
    else:
        print("Invalid input")

ello()


number = int(input("Enter a 4-digit number: "))

sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)

print("The sum of digits in", number, "is", sum_of_digits)

number =  int(input("Enter a 5-digit number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
