with open(0) as f:
    lines = f.read().strip().splitlines()

wheel = [1]
clockwise = True
startindex = 0

a = []
b = []
for i,line in enumerate(lines):
    start, end = map(int, line.split('-'))
    if clockwise:
        a.append((start, end))
    else:
        b.append((start, end))

    clockwise = not clockwise

for start, end in a:
    for i in range(start, end + 1):
        wheel.append(i)

for start, end in b[::-1]:
    for i in range(end, start - 1, -1):
        wheel.append(i)

print(wheel[(startindex + 202520252025) % len(wheel)])