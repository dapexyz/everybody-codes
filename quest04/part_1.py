with open(0) as f:
    gears = list(map(int, f.read().strip().splitlines()))
    
    rotation_multiplier = {}
    for i in range(len(gears)):
        rotation_multiplier[i] = 1 if i == 0 else rotation_multiplier[i-1] * gears[i - 1] / gears[i]

print(int(rotation_multiplier[len(gears) - 1] * 2025))