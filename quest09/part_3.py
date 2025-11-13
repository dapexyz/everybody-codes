with open(0) as f:
    lines = f.read().strip().splitlines()
    lines = [line.split(':')[1] for line in lines]

def is_child(child, parent1, parent2):
    for i in range(len(child)):
        cur = child[i]

        if cur != parent1[i] and cur != parent2[i]:
            return False
    return True

G = {}

for idx, line in enumerate(lines):
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            if i == idx or j == idx:
                continue

            child = line
            parent1 = lines[i]
            parent2 = lines[j]

            if is_child(child, parent1, parent2):
                G[idx] = G.get(idx, []) + [i]
                G[idx] = G.get(idx, []) + [j]
                G[i] = G.get(i, []) + [idx]
                G[j] = G.get(j, []) + [idx]

visited = set()
biggest = []

for i in range(len(lines)):
    stack = [i]
    family = []

    while stack:
        cur = stack.pop()

        if cur in visited:
            continue
        visited.add(cur)
        family.append(cur)

        for adj in G.get(cur, []):
            stack.append(adj)

    if len(family) > len(biggest):
        biggest = family

print(sum(b + 1 for b in biggest))