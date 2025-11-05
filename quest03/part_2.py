with open(0) as f:
    nums = list(map(int, f.read().strip().split(',')))

print(sum(sorted(list(set(nums)))[:20]))


