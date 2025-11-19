with open(0) as f:
    lines = f.read().strip().splitlines()

wheel = [1]
clockwise = True
startindex = 0

for i,line in enumerate(lines):
    print(i, len(lines))
    source, target = map(int, line.split('-'))
    for num in range(source, target + 1):
        if clockwise:
            wheel.append(num)
        else:
            startindex += 1
            wheel.insert(0, num)

    clockwise = not clockwise

print(wheel[(startindex + 20252025) % len(wheel)])
