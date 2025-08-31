rep = 0
place = 0
par = int(input())
parl = []
for i in range(par):
    parl.append(int(input()))
parl.sort()
parl.reverse()
#[75, 75, 70, 70, 70, 70, 60, 60]
first = parl.count(parl[0])
#2
second = parl.count(parl[first])
#4
third = parl.count(parl[second+first])
print(parl[second+first], third)