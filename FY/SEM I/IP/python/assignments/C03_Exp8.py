#!/usr/bin/env python
# coding: utf-8

# 1. A group of 6 kids are playing hide n seek game.
#  Among 6 kids one is allocated as leader.
# whenever leader will say start the dice will roll & the den will be on one of the kid randomly.
# do the code and store how many time the respective kid has got the den (hint: use random function)

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
