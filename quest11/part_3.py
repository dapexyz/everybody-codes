with open(0) as f:
    cols = list(map(int, f.read().strip().splitlines()))

assert cols == sorted(cols)

cols = list(reversed(cols))
t = 0
cur = 0

for i in range(len(cols)):
    cur += cols[i] - (sum(cols) // len(cols))
    t = max(t, cur)

print(t)

