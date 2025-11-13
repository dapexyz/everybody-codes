with open(0) as f:
    lines = f.read().strip().splitlines()
    lines = [line.split(':')[1] for line in lines]

    parent1, parent2, child = lines

t1 = 0
t2 = 0

for i in range(len(child)):
    p1, p2 = parent1[i], parent2[i]
    cur = child[i]

    if cur == p1:
        t1 += 1

    if cur == p2:
        t2 += 1

print(t1 * t2)
