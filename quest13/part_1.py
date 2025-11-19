with open(0) as f:
    lines = f.read().strip().splitlines()
    nums = list(map(int, lines))

wheel = [1]
clockwise = True
startindex = 0

for num in nums:
    if clockwise:
        wheel.append(num)
    else:
        startindex += 1
        wheel.insert(0, num)

    clockwise = not clockwise

print(wheel[(startindex + 2025) % len(wheel)])