import sys
input = sys.stdin.readline

together = []
separate = []
groups = []

fault = 0
t = 0

for i in range(int(input())):
    together.append(list(input().strip().split()))

for i in range(int(input())):
    separate.append(list(input().strip().split()))

for i in range(int(input())):
    groups.append(list(input().strip().split(' ')))

# print(together, seperate, groups)

group_sets = [set(g) for g in groups]

for i, j in together:
    if any(i in g and j in g for g in group_sets):
        t += 1

t = abs(t - len(together))

for i, j in separate:
    if any(i in g and j in g for g in group_sets):
        t += 1


print(t)