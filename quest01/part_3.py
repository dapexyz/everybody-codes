with open(0) as f:
    lines = [line.strip() for line in f]

names = lines[0].split(',')
instructions = lines[2].split(',')

for inst in instructions:
    direction = inst[0]
    amount = int(inst[1:])

    if direction == 'L':
        amount *= -1

    target = amount % len(names)

    names[0], names[target] = names[target], names[0]

print(names[0])