with open(0) as f:
    names, rules = f.read().strip().split('\n\n')
    names = names.split(',')
    rules = rules.splitlines()

invalid_names = []

for rule in rules:
    for name in names:
        if name in invalid_names:
            continue
        
        matches = True

        letter, following = rule.split(' > ')
        following = following.split(',')

        for i in range(len(name)):
            cur = name[i]

            if cur != letter:
                continue

            if i == len(name) - 1:
                continue

            if name[i + 1] not in following:
                matches = False

        if not matches:
            invalid_names.append(name)


print([n for n in names if n not in invalid_names][0])