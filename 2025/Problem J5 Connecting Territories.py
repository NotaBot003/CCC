debug = False

height = int(input())
length = int(input())
nums = int(input())
grid = []

num = 0
rep = 0
out = []

for i in range(length * height):
    rep += 1
    num += 1
    out.append(num)
    if rep == length:
        grid.append(out)
        out = []
        rep = 0
    if num == nums: num = 0
if debug:
    for i in grid:
        print(*i)

value = int(grid[0][0])
for j in range(2):
    value += int(grid[1][j])
    least = value
    value -= int(grid[1][j])

for i in range(1, length - 1):
    value = int(grid[0][i])
    for j in range(3):
        value += int(grid[1][i + j - 1])
        least = min(least, value)
        value -= int(grid[1][i + j - 1])

value = int(grid[0][0])
for j in range(2):
    value += int(grid[1][j - 1])
    least = min(least, value)
    value -= int(grid[1][j - 1])

print(least)

"""
2
1
7
"""

