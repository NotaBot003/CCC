import sys
input = sys.stdin.readline

a = list(input().strip())
t = 0

l, cl = a.count("L"), a.count("L")
cs = a.count("S")

ready = False
start1 = len(a) - 1
start2 = len(a) - cs - 1

# def twswap(x, y, z):
#     temp = a[x]
#     a[x] = a[y]
#     a[y] = a[z]
#     a[z] = temp
#     return

# Sort L (efficiently)
for i in range(cl):
    if a[i] == "S":
        for s in range(start1, len(a) - cs - 1, -1):
            if a[s] == "L":
                a[s], a[i] = a[i], a[s]
                t += 1
                start1 = s
                break
    elif a[i] == "M":
        for m in range(start2, cl - 1, -1):
            if a[m] == "L":
                a[m], a[i] = a[i], a[m]
                t += 1
                start2 = m
                break

# Sort L (complete)
for i in range(cl):
    if a[i] != "L":
        while True:
            if a[l] == 'L':
                a[i], a[l] = a[l], a[i]
                t += 1
                break
            l += 1

s = len(a) - 1
# Sort M / S
for i in range(len(a) - cs):
    if a[i] == 'S':
        while True:
            if a[s] == 'M':
                a[s], a[i] = a[i], a[s]
                t += 1
                break
            s -= 1
print(t)
# print(a)
"""
LSMSMLLMS
LLMSMLSMS
LLLSMMSMS
"""
"""
LLSSML SLMS MMLSS
"""