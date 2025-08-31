rep = int(input())
ant = 100
dave = 100
for i in range(rep):
    inputs = input()
    [a, d] = map(int, inputs.split())
    if a > d:
        dave -= a
    if a < d:
        ant -= d
print(ant)
print(dave)

