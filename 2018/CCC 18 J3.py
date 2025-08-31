distance = input()

distance = distance.split()
[da, db, dc, dd] = list(map(int, distance))

a = 0
b = da
c = db
d = dc
e = dd

print (str(a) + " " + str(a + b) + " " + str(a + b + c) + " " + str(a + b + c + d) + " " + str(a + b + c + d +e))
print (str(b) + " " + str(a) + " " + str(a + c) + " " + str(a + c + d) + " " + str(a + c + d +e))
print (str(b + c) + " " + str(c) + " " + str(a) + " " + str(a + d) + " " + str(a + d +e))
print (str(b + c + d) + " " + str(c + d) + " " + str(d) + " " + str(a) + " " + str(a + e))
print (str(b + c + d + e) + " " + str(c + d + e) + " " + str(d + e) + " " + str(a + e) + " " + str(a))