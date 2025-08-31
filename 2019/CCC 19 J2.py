n = int(input())

for i in range(n):
    inputs = input()
    inputs = inputs.split()
    [aa, ab] = list(inputs)
    aa = int(aa)
    print(ab*aa)