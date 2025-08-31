m = int(input())
d = int(input())

if (m <= 2 and d <= 17) or m == 1:
    print("Before")
if m == 2 and d == 18:
    print("Special")
if (m >= 2 and d >= 19) or m >= 3:
    print("After")
