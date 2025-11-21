with open(0) as f:
    lines = f.read().strip().splitlines()

    target_pattern = [c for line in lines for c in line]
    grid = tuple([tuple('.' * 34)] * 34)

N = len(grid)
M = len(grid[0])

diagonals = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

def score(grid):
    return sum(sum(c == '#' for c in line) for line in grid)

def simulate_round(grid):
    new_grid = []
    for r in range(N):
        row = []
        for c in range(M):
            cur = grid[r][c]

            diagonal_active = sum(
                0 <= r + dr < N and 0 <= c + dc < M and grid[r + dr][c + dc] == '#' for dr, dc in diagonals
            )

            if cur == '#':
                if diagonal_active % 2 == 0:
                    cur = '.'
            else:
                if diagonal_active % 2 == 0:
                    cur = '#'
            
            row.append(cur)
        new_grid.append(row)
    return tuple(tuple(row) for row in new_grid)

def target(grid):
    ret = []
    for r in range(13, 21):
        ret += [grid[r][c] for c in range(13, 21)]
    return ret

grids = []
t = 0
while True:
    if target(grid) == target_pattern:
        t += score(grid)
    if grid in grids:
        break
    grids.append(grid)
    grid = simulate_round(grid)
"""
print(len(grids))
print(grids.index(grid))
print(t)
print(score(grid))
"""
grids = grids[1:] # empty starting grid


ROUNDS = 1000000000 
t *= ROUNDS // len(grids)
remaining = ROUNDS % len(grids)

for grid in grids[:remaining]:
    if target(grid) == target_pattern:
        t += score(grid)


print(t)



