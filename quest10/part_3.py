from collections import deque

with open(0) as f:
    grid = [list(line) for line in f.read().strip().splitlines()]
    
N = len(grid)
M = len(grid[0])

SHEEPS = set()
HIDEOUTS = set()
DRAGON = (0, 0)

for r in range(N):
    for c in range(M):
        if grid[r][c] == 'S':
            SHEEPS.add((r, c))
        elif grid[r][c] == 'D':
            DRAGON = (r, c)
        elif grid[r][c] == '#':
            HIDEOUTS.add((r, c))
 
queue = deque([(0, DRAGON)])
visited = set()
eaten = set()
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

cache = {}
def solve(sheeps, dragon, sheep_turn):
    key = (sheeps, dragon, sheep_turn)
    
    if key in cache:
        return cache[key]
    
    ret = 0

    if sheep_turn:
        # dragon won
        if not sheeps:
            cache[key] = 1
            return 1

        can_move = False
        for i, (r, c) in enumerate(sheeps):
            nr = r + 1
            if (nr < N and (nr, c) in HIDEOUTS) or dragon != (nr, c):
                can_move = True

                if nr == N: # sheep escaped
                    continue

                new_sheeps = []

                for j, (sr, sc) in enumerate(sheeps):
                    if j == i:
                        new_sheeps.append((sr + 1, sc))
                    else:
                        new_sheeps.append((sr, sc))

                ret += solve(tuple(new_sheeps), dragon, False)

        if can_move:
            cache[key] = ret
            return ret
        else:
            ret = solve(sheeps, dragon, False)
            cache[key] = ret
            return ret
    else:
        r, c = dragon
        for dr, dc in possible_moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                new_sheeps = []

                for sr, sc in sheeps:
                    if (nr, nc) == (sr, sc) and grid[sr][sc] != '#':
                        continue
                    new_sheeps.append((sr, sc))

                ret += solve(tuple(new_sheeps), (nr, nc), True)
        
        cache[key] = ret
        return ret

print(solve(tuple(SHEEPS), DRAGON, True))