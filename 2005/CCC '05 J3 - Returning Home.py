Directions = []
rep = 0
while True:
    rep += 1
    temp = input()
    Directions.append(temp)
    if temp == 'SCHOOL':
        break
rep = rep/2
# print(Directions)
Directions.reverse()
# print(rep)
# print(Directions)
for i in range(int(rep - 1)):
    # print(i)
    if Directions[i + i + 1] == "R":
        BackD = 'LEFT'
    if Directions[i + i + 1] == "L":
        BackD = 'RIGHT'
    print('Turn', BackD, 'onto', Directions[i + i + 2], 'street.')
rep = int(rep)

if Directions[rep + rep - 1] == "R":
    BackD = 'LEFT'
if Directions[rep + rep - 1] == "L":
    BackD = 'RIGHT'
print('Turn', BackD, 'into your HOME.')
