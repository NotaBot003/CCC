n = int(input())
d1 = input()
d2 = input()
out = 0

for i in range(n):
    a = d1[i]
    b = d2[i]
    if a == "C" and b == "C":
        out += 1
print(out)