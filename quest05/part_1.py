with open(0) as f:
    line = f.read().strip()

    identifier, numbers = line.split(':')
    identifier = int(identifier)
    numbers = list(map(int, numbers.split(',')))

fishbone = [[None, numbers[0], None]]

for n in numbers[1:]:
    found = False
    for f in fishbone:
        left, spine, right = f
        if left == None and n < spine:
            found = True
            f[0] = n
            break
        if right == None and n > spine:
            found = True
            f[2] = n
            break
    if not found:
        fishbone.append([None, n, None])

print(''.join(str(x[1]) for x in fishbone))