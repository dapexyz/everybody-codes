TEST = False

with open(0) as f:
    line = f.read().strip()

pattern = line

REPEAT = 1 if TEST else 1000
DISTANCE_LIMIT = 10 if TEST else 1000

layout = pattern * REPEAT

T = 0

for i,c in enumerate(layout):
    cur = layout[i]

    if cur.isupper():
        continue
    
    relevant_layout_part = layout[max(i - DISTANCE_LIMIT,0):i + DISTANCE_LIMIT + 1]

    if cur == 'a':
        T += relevant_layout_part.count('A')
    elif cur == 'b':
        T += relevant_layout_part.count('B')
    elif cur == 'c':
        T += relevant_layout_part.count('C')
    else:
        assert False

print(T)