with open(0) as f:
    lines = f.read().strip().splitlines()
    nums = list(map(int, lines[0].split(',')))

nails = max(nums)
connections = list(zip(nums, nums[1:]))

def crosses(A, B):
    a1, b1 = sorted(A)
    a2, b2 = sorted(B)
    return (a1 < a2 < b1 < b2) or (a2 < a1 < b2 < b1)
    
possible_cuts = set([])

for i in range(len(nums)):
    for j in range(i, len(nums)):
        possible_cuts.add((nums[i], nums[j]))

T = 0
# inefficient
for i, cut in enumerate(possible_cuts):
    if i % 1000 == 0:
        print(i / len(possible_cuts) * 100)
    count = 0

    for connection in connections:
        if crosses(cut, connection):
            count += 1

    if cut in connections:
        count += 1

    T = max(T, count)

print(T)