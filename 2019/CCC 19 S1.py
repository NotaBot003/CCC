a = 1
b = 2
c = 3
d = 4

inputs = input()
h = inputs.count("H")
v = inputs.count("V")

for i in range(h):
    a, b, c, d = c, d, a, b
for i in range(v):
    a, b, c, d = b, a, d, c

print(str(a) + " " + str(b))
print(str(c) + " " + str(d))
