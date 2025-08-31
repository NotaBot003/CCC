Debug = True
# Debug = False
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # left, right, up and down
def BFS_grid(g, visited, steps, wall, sr, sc, tr, tc):
    Q = []
    Q.append((sr, sc))
    visited[sr][sc] = True
    steps[sr][sc] = 1
    while len(Q) > 0:
        r, c = Q.pop(0)
        for dr, dc in dirs:
            if g[r][c] == '-' and dc == 0: continue
            if g[r][c] == '|' and dr == 0: continue
            ar, ac = r + dr, c + dc
            if visited[ar][ac] or g[ar][ac] == wall:
                continue
            visited[ar][ac] = True
            steps[ar][ac] = steps[r][c] + 1
            Q.append((ar, ac))
            if ar == tr and ac == tc:
                return steps[ar][ac]
    return -1

T = int(input())
for t in range(T):
    Rows, Cols = int(input()), int(input())
    wall = '*'
    g = [[wall for c in range(Cols + 2)] for r in range(Rows + 2)]
    visited = [[False for c in range(Cols + 2)] for r in range(Rows + 2)]
    steps = [[-1 for c in range(Cols + 2)] for r in range (Rows + 2)]
    for r in range(1, Rows + 1):
        # g[r] = g[r][0:1] + list(map(int, input().split())) + g[r][-1:]
        g[r] = [wall] + list(input()) + [wall]
        if Debug: print(g[r])
        if Debug: print(Rows)
    sr, sc = 1, 1
    tr, tc = Rows, Cols
    cross = BFS_grid(g, visited, steps, wall, sr, sc, tr, tc)
    if Rows == 1 and Cols == 1:
        print("1")
    else: print(cross)
'''
3
2
2
-|
*+
3
5
+||*+
+++|+
**--+
2
3
+*+
+*+
'''