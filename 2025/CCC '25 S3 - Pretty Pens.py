rep, colors, changes = map(int, input().split())

pens = [[] for i in range(colors)]

for i in range(rep):
   c, p = map(int, input().split())
   pens[c - 1].append(p)
print(pens)


"""
6 3 0
1 6
2 9
3 4
2 7
3 9
1 3
"""