with open(0) as f:
    nums = list(map(int, f.read().strip().split(',')))

print(max(nums.count(num) for num in set(nums)))