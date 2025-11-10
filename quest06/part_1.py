with open(0) as f:
    line = f.read().strip()

m = 0
p = 0

for c in line:
    if c == 'A':
        m += 1
    elif c == 'a':
        p += m

print(p)