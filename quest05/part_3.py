from functools import cmp_to_key

with open(0) as f:
    lines = f.read().strip().splitlines()

def get_level_values(fishbone):
    values = []

    for x in fishbone:
        s = ''
        for y in x:
            if y != None:
                s += str(y)

        values.append(int(s))
    
    return values

def compare(a, b):
    ida, qa, la = a
    idb, qb, lb = b

    if qa != qb:
        return qb - qa
    
    for i in range(max(len(la), len(lb))):
        ca = None if i >= len(la) else la[i]
        cb = None if i >= len(lb) else lb[i]

        if ca == cb:
            continue

        return cb - ca

    return idb - ida

T = []
for id,line in enumerate(lines):
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
    T.append((id + 1, int(''.join(str(x[1]) for x in fishbone)), get_level_values(fishbone)))

print(sum(x[0] * (i + 1) for i,x in enumerate(sorted(T, key=cmp_to_key(compare)))))