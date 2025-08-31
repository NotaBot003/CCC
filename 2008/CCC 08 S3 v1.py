def bfs(grid, r, c, visited):
    q = []
    visited = []
    q.append(grid)
    while len(q) > 0:

rows = int(input())
columns = int(input())
grid = [[ for i in range(columns)]]
visited = [[False for c in range(columns+2)] for r in range(rows+2)]
