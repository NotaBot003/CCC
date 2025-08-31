import sys
input = sys.stdin.readline

inputs = input().strip()
cipher = 'a' * 0
lettercount = 0
num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
rep = 0

for i in inputs:
    if i not in num:
        if rep != 0:
            cipher += (letter * int(number))
        letter = i
        lettercount = 1
    if i in num:
        if lettercount == 1:
            number = i
        else:
            number += i
        lettercount = 0
        rep = 1

cipher += (letter * int(number))
c = int(input())

c = c - (c // len(cipher) * len(cipher))
print(cipher[c])

"""
a4b1c2d10
100
"""
