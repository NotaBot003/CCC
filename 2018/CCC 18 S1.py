v = int(input())

small = 0
out = 100000000000000000000000
neighborhoods = []
for i in range(v):
    neighborhoods.append(int(input()))
neighborhoods.sort()
for i in range(v - 2):
    b = (neighborhoods[i])
    c = (neighborhoods[i + 2])
    small = c - b
    if out > small:
        out = small
output = out / 2
print(output)


