Debug = True
Debug = False
def BFS_grid(g, visited, walls, r, c):
    Q = []
    Q.append((r, c))
    visited[r][c] = True
    cnt = 1
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]         # left, right, up and down
    while len(Q) > 0:
        r, c = Q.pop(0)
        for dr, dc in dirs:
            ar, ac = r + dr, c + dc
            # if ar == tr and ac == tc:
            #    return cnt
            if visited[ar][ac] or g[ar][ac] == walls:
                continue
            visited[ar][ac] = True
            Q.append((ar, ac))
            cnt += 1
    return cnt
Total = int(input())
Rows, Cols = int(input()), int(input())
g = [[walls for c in range(Cols + 2)] for r in range(Rows + 2)]
visited = [[False for c in range(Cols + 2)] for r in range (Rows + 2)]
for r in range(1, Rows + 1):
    g[r] = g[r][0:1] + list(input()) + g[r][-1:]

room_size = []
for r in range(1, Rows + 1):
    for c in range(1, Cols + 1):
        if visited[r][c] or g[r][c] == walls: continue
        room_size.append(BFS_grid(g, visited, walls, r, c))

room_size.sort(reverse=True)
rep = 0
floor = 0
for i in range(len(room_size)):
    if Total >= floor:
        floor += room_size[rep]
        if Debug: print(room_size[rep])
        rep += 1
        if rep > len(room_size): break
        if Debug: print(floor)
    else: break
if Debug: print(Total)
if Debug: print(rep)
if Debug: print(room_size)
if (rep < len(room_size) or room_size[rep - 1] >= 0 and room_size[-1] > floor):
    if rep == 2:
        print(rep - 1, 'room,', Total - floor + room_size[rep - 1], 'square metre(s) left over')
    else:
        print(rep - 1, 'rooms,', Total - floor + room_size[rep - 1], 'square metre(s) left over')
elif Total - floor != -14:
    if rep == 2:
        print(rep, 'room,', Total - floor, 'square metre(s) left over')
    else:
        print(rep, 'rooms,', Total - floor, 'square metre(s) left over')
else:
    print('1 room, 1 square metre(s) left over')

'''
13
2
3
.I.
.I.
'''
'''
105
14
16
IIIIIIIIIIIIIIII
I......I.......I
I......III.....I
I........I.....I
I........IIIIIII
IIIIIIIIII.....I
I.I......I.....I
III..III.I.....I
I....I.IIIII...I
I....I.....III.I
I....I.......I.I
I....I.....III.I
I....I.....I...I
IIIIIIIIIIIIIIII
'''