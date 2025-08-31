def rotate_90(grid):
    new_grid = []
    for col, _ in enumerate(grid):
        new_row = []
        for row in grid:
            new_row.append(row[col])
        new_grid.append(new_row)
    return new_grid[::-1]


list = []
for _ in range(int(input())):
    list.append([int(i) for i in input().split()])

while True:
    for a, b in enumerate(list):
        for idx, rotate in enumerate(b):
            try:
                if rotate >= b[idx + 1]:
                    break
            except IndexError:
                pass
            try:
                if rotate >= list[a + 1][idx]:
                    break
            except IndexError:
                pass
        else:
            continue
        break
    else:
        break
    list = rotate_90(list)
for a in list:
    print(' '.join(map(str, a)))