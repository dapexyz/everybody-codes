with open(0) as f:
    lines = f.read().strip().splitlines()
    nums = list(map(int, lines[0].split(',')))

connections = list(zip(nums, nums[1:]))

def crosses(A, B):
    a1, b1 = sorted(A)
    a2, b2 = sorted(B)
    return (a1 < a2 < b1 < b2) or (a2 < a1 < b2 < b1)
    
T = 0

for i in range(1, len(connections)):
    cur = connections[i]

    for j in range(i):
        if crosses(cur, connections[j]):
            T += 1

print(T)