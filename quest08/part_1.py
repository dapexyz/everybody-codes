with open(0) as f:
    lines = f.read().strip().splitlines()
    nums = list(map(int, lines[0].split(',')))

nails = max(nums)
connections = list(zip(nums, nums[1:]))

def crosses_center(a, b):
    return max(a, b) - min(a, b) == nails // 2

print(sum(crosses_center(a, b) for a, b in connections))