import sys
input = sys.stdin.readline

rep = int(input().strip())
forcast = []
left = 0
maxStreak = 0
p = 0

for i in range(rep):
    forcast.append(input().strip())

if forcast.count('S') == rep:
    print(rep - 1)
    sys.exit(0)

for right in range(rep):
    if forcast[right] == 'P':
        p += 1

    while p > 1:
        if forcast[left] == 'P':
            p -= 1
        left += 1

    maxStreak = max(maxStreak, right - left + 1)
print(maxStreak)

'''
7
S
P
S
S
P
P
S

'''
