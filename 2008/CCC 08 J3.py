kb =\
"ABCDEF"\
"GHIJKL"\
"MNOPQR"\
"STUVWX"\
"YZ -.d"
#print(kb)
r1,c1 = 0,0
s = input()
s += "d"
total = 0
for ch in s:
    #print(ord(ch))
    posi = kb.index(ch)
    r2 = posi//6
    c2 = posi %6
    #print(posi, r2, c2)
    dist = abs(r2-r1)+abs(c2-c1)
    total += dist
    r1,c1 = r2,c2
print(total)