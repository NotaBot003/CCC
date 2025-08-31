import sys
input = sys.stdin.readline

inputs = input().strip()
cipher = []
lettercount = 0
num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
rep = 0
lenght = 0

for i in inputs:
    if i not in num:
        if rep != 0:
            lenght += int(number)
            cipher.append((letter, int(lenght)))
        letter = i
        lettercount = 1
    if i in num:
        if lettercount == 1:
            number = i
        else:
            number += i
        lettercount = 0
        rep = 1

lenght += int(number)
cipher.append((letter, int(lenght)))
c = int(input())

c = c - (c // lenght * lenght)
# print(cipher, c)
# print(cipher[1])

for i in range(lenght):
    if cipher[i][1] <= c:
        maxim = cipher[i]
    else:
        maxim = cipher[i]
        break

print(maxim[0])

"""
a4b1c2d10
100
aaaabccdddddddddd
"""
