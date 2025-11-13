with open(0) as f:
    lines = f.read().strip().splitlines()
    lines = [line.split(':')[1] for line in lines]

def is_child(child, parent1, parent2):
    for i in range(len(child)):
        cur = child[i]

        if cur != parent1[i] and cur != parent2[i]:
            return False
    return True

t = 0

for idx, line in enumerate(lines):
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            if i == idx or j == idx:
                continue

            child = line
            parent1 = lines[i]
            parent2 = lines[j]

            if is_child(child, parent1, parent2):
                s1 = sum(child[c] == parent1[c] for c in range(len(child)))
                s2 = sum(child[c] == parent2[c] for c in range(len(child)))

                t += s1 * s2

print(t)
