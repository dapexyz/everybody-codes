with open(0) as f:
    line = f.read().strip()

ma = 0
mb = 0
mc = 0
p = 0

for c in line:
    if c == 'A':
        ma += 1
    elif c == 'B':
        mb += 1
    elif c == 'C':
        mc += 1
    elif c == 'a':
        p += ma
    elif c == 'b':
        p += mb
    elif c == 'c':
        p += mc

print(p)