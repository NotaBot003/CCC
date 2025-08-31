c = int(input())

g1 = input().split(' ')
g2 = input().split(' ')
t = (g2.count('1') + g1.count('1')) * 3

for i in range(c):
    if g1[i] == '1' and i < c - 1:
        if g1[i + 1] == '1':
            t -= 2
    if g2[i] == '1' and i < c - 1:
        if g2[i + 1] == '1':
            t -= 2
    if g1[i] == "1" and g2[i] == "1" and i % 2 == 0:
        t -= 2

print(t)

"""
5
0 0 0 0 0
1 1 1 1 1
"""