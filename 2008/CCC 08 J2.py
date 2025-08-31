bfour = 0

a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
while bfour == 0:
    button = int(input())
    n = int(input())
    for i in range(n):
        if button == 1:
            a, b, c, d, e = b, c, d, e, a
        if button == 2:
            a, b, c, d, e = e, a, b, c, d
        if button == 3:
            a, b, c, d, e = b, a, c, d, e
        if button == 4:
            bfour = bfour + 1

print(str(a) +  " " + str(b) + " " + str(c) + " " + str(d) +  " " + str (e))




