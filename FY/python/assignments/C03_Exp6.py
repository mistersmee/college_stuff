#!/usr/bin/env python
# encoding: utf-8


#1. Total Sales
# Design a program that asks the user to enter a store’s sales for each day of the week.
# The amounts should be stored in a list. 
# Use a loop to calculate the total sales for the week and display the result.


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