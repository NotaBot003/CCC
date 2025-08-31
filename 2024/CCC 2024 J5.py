def BFS(patch, visited, srow, scol):
    Q = [(srow, scol)]
    visited[srow][scol] = True
    pumpkin_values = {
        'S': 1,
        'M': 5,
        'L': 10
    }
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    total_value = 0
    while Q:
        r, c = Q.pop()
        if patch[r][c] in pumpkin_values:
            total_value += pumpkin_values[patch[r][c]]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(patch) and 0 <= nc < len(patch[0]) and not visited[nr][nc] and patch[nr][nc] != '*':
                visited[nr][nc] = True
                Q.append((nr, nc))
    return total_value

R = int(input())
C = int(input())
patch = []
visited = [[False for _ in range(C)] for _ in range(R)]
for _ in range(R):
    patch.append(list(input().strip()))
srow = int(input())
scol = int(input())
total_value = BFS(patch, visited, srow, scol)
print(total_value)
