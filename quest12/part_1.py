from collections import deque

with open(0) as f:
    grid = [[int(c) for c in line] for line in f.read().strip().splitlines()]

N = len(grid)
M = len(grid[0])

dirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

q = deque([(0, 0)])

t = 0
visited = set()

while q:
    r, c = q.popleft()
    if (r, c) in visited:
        continue
    visited.add((r, c))

    t += 1
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M:
            if grid[r][c] >= grid[nr][nc]:
                q.append((nr, nc))

print(t)