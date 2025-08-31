n = int(input())

hi = 0
who = ''
for i in range(n):
    name = input()
    bid  = int(input())
    if bid > hi:
        hi = bid
        who = name

print (who) 
