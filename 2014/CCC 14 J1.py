a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180: print ("Error")
if a + b + c == 180 and a == b == c: print ("Equilateral")
if a + b + c == 180 and a == b != c or b == c != a or c == a != b: print ("Isosceles")
if a + b + c == 180 and a != b != c != a: print ("Scalene")
