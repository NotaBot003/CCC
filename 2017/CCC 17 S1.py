n = int(input())
sw = input()
se = input()

sw = sw.split()
se = se.split()
c = 0
d =0
ro = 0
tr = 0
r = list(map(str, sw))

for i in range(n):
    a = int(sw[i])
    b = int(se[i])
    #print(a, b)
    if r != 1:
        c = c + a
        d = d + b
    else:
        c = a
    ro = ro + 1
    #print(ro, c, d)
    if c == d:
        tr = ro

print(tr)