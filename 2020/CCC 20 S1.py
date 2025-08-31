n = int(input())
rcd = []
max_speed = 0
for _ in range(n):
    t, p = map(int, input().split())
    rcd.append((t, p))
print(rcd)
rcd.sort()
# [(0, 100), (20, 50), (10, 120)]
for i in range(1, n):
    t1, p1 = rcd[i - 1]
    t2, p2 = rcd[i]
    dt = t2 - t1
    dp = abs(p2 - p1)
    speed = dp / dt
    max_speed = max(max_speed, speed)
print(max_speed)