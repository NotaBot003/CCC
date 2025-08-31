n = int(input())
sp = 0
st = 1

for i in range(n):
    ps = int(input())
    f = int(input())

    if ((5 * ps) - (3 * f)) > 40:
        sp = sp + 1
    else: st = st * 0

if st == 1:
    print (str(sp)+"+")
else: print(sp)

