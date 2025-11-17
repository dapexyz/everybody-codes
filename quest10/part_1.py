from collections import deque

with open(0) as f:
    grid = [list(line) for line in f.read().strip().splitlines()]
    
N = len(grid)
M = len(grid[0])

SHEEPS = set()
DRAGON = (0, 0)

for r in range(N):
    for c in range(M):
        if grid[r][c] == 'S':
            SHEEPS.add((r, c))
        elif grid[r][c] == 'D':
            DRAGON = (r, c)

queue = deque([(0, DRAGON)])
visited = set()
t = 0

possible_moves = [
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
]

while queue:
    cur = queue.popleft()
    moves, (r, c) = cur

    if (r, c) in visited:
        continue
    visited.add((r, c))

    if (r, c) in SHEEPS:
        t += 1

    if moves == 4:
        continue

    for dr, dc in possible_moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M:
            queue.append((moves + 1, (nr, nc)))

print(t)
