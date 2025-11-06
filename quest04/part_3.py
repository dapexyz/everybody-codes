import math

with open(0) as f:
    gears = [list(map(int, line.split('|'))) for line in f.read().strip().splitlines()]

T = 1
last_gear = gears[0][0]

for i in range(1, len(gears)):
    gear = gears[i]

    if len(gear) == 1:
        T *= last_gear / gear[0]
        last_gear = gear[0]
    else:
        T *= last_gear / gear[0]
        last_gear = gear[1]

print(math.floor(T * 100))
