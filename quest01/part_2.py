with open(0) as f:
    lines = [line.strip() for line in f]

names = lines[0].split(',')
instructions = lines[2].split(',')

cur = 0

for inst in instructions:
    direction = inst[0]
    amount = int(inst[1:])

    if direction == 'L':
        amount *= -1

    cur = (cur + amount) % len(names)

print(names[cur])