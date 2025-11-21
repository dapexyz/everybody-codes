with open(0) as f:
    lines = f.read().strip().splitlines()

    grid = [list(line) for line in lines]

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
    return new_grid

t = 0
for _ in range(10):
    grid = simulate_round(grid)
    t += score(grid)

print(t)






