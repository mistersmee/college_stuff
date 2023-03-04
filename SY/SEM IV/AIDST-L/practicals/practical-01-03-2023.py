# Write a Python program to read a list of words and return the length of longest word
# WAP to create dictionary as student which has the keys: name, PRN, marks, phone number, Dynamic, compute the average marks of ten students
# WAP TO CREATE A DICTIONEAYR WIRH EYS AS FIERT CHARAGERTTE AND VALEU AS WORDS STARTING WIRTHT THEAT CHARAGECETE

# Program 1

def longestLength(a):
    max1 = len(a[0])
    temp = a[0]

    # for loop to traverse the list
    for i in a:
        if(len(i) > max1):

            max1 = len(i)
            temp = i

    print("The word with the longest length is:", temp,
          " and length is ", max1)


# Driver Program
a = []

k = 'y'

while k == 'y':
    a.append(input("Enter a word:"))
    k = input("Do you want to enter more words? [y/n]:")

longestLength(a)

# Program 2

d = {}
i = 0
avg = 0

while i < 10:
    print(f"Enter the details for student: {i+1}")
    d[0] = input("Enter student name:")
    d[1] = input("Enter student PRN:")
    d[2] = int(input("Enter student total marks:"))
    d[3] = input("Enter student phone number:")
    avg = avg + d[2]
    i += 1

avg = avg / 10

print("The average of 10 students marks is" + avg)


# Program 3

alphabet = {}
