with open(0) as f:
    names, rules_in = f.read().strip().split('\n\n')
    names = names.split(',')
    rules_in = rules_in.splitlines()

rules = {}

for rule in rules_in:
    letter, following = rule.split(' > ')
    following = following.split(',')

    for c in following:
        rules[letter] = rules.get(letter, []) + [c]

unique_names = set([])
valid_prefixes = [name for name in names if all(name[i + 1] in rules.get(name[i], []) for i in range(len(name) - 1))]

for name in valid_prefixes:
    to_explore = set([name])

    while to_explore:
        cur = to_explore.pop()
        
        if len(cur) > 11:
            continue

        if len(cur) >= 7:
            unique_names.add(cur)

        for c in rules.get(cur[-1], []):
            to_explore.add(cur + c)

print(len(unique_names))