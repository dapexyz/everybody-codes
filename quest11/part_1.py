with open(0) as f:
    cols = list(map(int, f.read().strip().splitlines()))

ROUND = 0

for phase in range(1, 3):
    flag = True
    while flag and ROUND < 10:
        flag = False
        for i in range(len(cols) - 1):
            a, b = cols[i:i+2]

            if phase == 1 and a > b:
                flag = True
                cols[i + 1] = b + 1
                cols[i] = a - 1
            elif phase == 2 and a < b:
                flag = True
                cols[i + 1] = b - 1
                cols[i] = a  +1

        if flag:
            ROUND += 1

print(sum((i + 1) * cols[i] for i in range(len(cols))))