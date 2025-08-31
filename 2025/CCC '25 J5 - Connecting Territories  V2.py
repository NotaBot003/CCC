import sys
input = sys.stdin.readline

debug = False

height, length, nums = int(input().strip()), int(input().strip()), int(input().strip())
grid, out, num, rep = [], [int(1e7)], 0, 0
curr_grid = [int(1e9)]
stop_point = 0
INF = int(1e9)

# for i in range(length * height):
#     rep += 1
#     num += 1
#     out.append(num)
#     if rep == length:
#         out.append(INF)
#         grid.append(out)
#         out = [INF]
#         rep = 0
#     if num == nums: num = 0
# if debug:
#     for i in grid:
#         print(*i)
for i in range(length):
    rep += 1
    num += 1
    curr_grid.append(num)
    if num == nums: num = 0
curr_grid.append(INF)
if debug: print(curr_grid)

if height == 1: print(1)
else:
    for i in range(1, height):
        rep = 0
        next_grid = [INF]
        for i in range(length):
            rep += 1
            num += 1
            next_grid.append(num)
            if num == nums: num = 0
        next_grid.append(INF)


        if debug: print(next_grid)
        for j in range(1, length + 1):
            next_grid[j] += min(curr_grid[j], curr_grid[j - 1], curr_grid[j + 1])
        curr_grid = next_grid
        # if debug:
            # print(next_grid)
            # print(curr_grid)
print(min(next_grid))
