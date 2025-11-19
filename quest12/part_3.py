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

def solve(positions, exclude=[]):
    q = deque(positions)

    visited = set()
    t = 0

    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        if (r,c) in exclude:
            continue
        visited.add((r, c))

        t += 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if grid[r][c] >= grid[nr][nc] and (nr, nc) not in exclude:
                    q.append((nr, nc))
    return (t, visited)

all_destroyed = set()
best_strikes = []

for _ in range(3):
    best = (-1, None, [])

    for r in range(N):
        for c in range(M):
            s = solve([(r, c)], all_destroyed)
            if s[0] >= best[0]:
                best = (s[0], (r, c), s[1])

    all_destroyed |= best[2]
    best_strikes.append(best[1])

print(solve(best_strikes)[0])
