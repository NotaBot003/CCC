num = int(input())
disvis = {0, 4, 5, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19}

t = 0

t += num // 20
num %= 20
if num in disvis:
    t += 1
print(t)

