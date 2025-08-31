a, b, x, y = map(int, input().split())

if a + x - abs(a - x) > b + y - abs(b - y):
    print(abs(a - x) + 2 * b + 2 * y + x + a)
if a + x - abs(a - x) <= b + y - abs(b - y):
    print(abs(b - y) + 2 * a + 2 * x + b + y)


"""
3 1 1 2 
"""