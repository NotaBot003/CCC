n = int(input())
s = int(input())
t = 0
ss = n

for i in range(s):
    t = t + ss
    ss = ss * 10

t = t + ss

print(t)