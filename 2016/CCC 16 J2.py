a = input()
b = input()
c = input()
d = input()

a = a.split()
b = b.split()
c = c.split()
d = d.split()

[aa, ab, ac, ad] = list(map(int, a))
[ba, bb, bc, bd] = list(map(int, b))
[ca, cb, cc, cd] = list(map(int, c))
[da, db, dc, dd] = list(map(int, d))

cone = aa + ba + ca + da
ctwo = ab + bb + cb + db
cthree = ac + bc + cc + dc
cfour = ad + bd + cd + dd

rone = aa + ab + ac + ad
rtwo = ba + bb + bc + bd
rthree = ca + cb + cc + cd
rfour = da + db + dc + dd

if cone == ctwo == cthree == cfour == rone == rtwo == rthree == rfour:
    print("magic")
else:
    print("not magic")