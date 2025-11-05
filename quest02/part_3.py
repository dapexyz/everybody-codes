with open(0) as f:
    line = f.read().strip()

    X, Y = tuple(map(int, line.split('[')[1].split(']')[0].split(',')))
    A = X + Y*1j

def check(point):
    res = 0 + 0*1j

    for i in range(100):
        res *= res
        res = (int(res.real / 100000)) + (int(res.imag / 100000)*1j)
        res += point

        if not (-1000000 <= res.real <= 1000000 and -1000000 <= res.imag <= 1000000):
            return False

    return True

T = 0

for r in range(1001):
    for c in range(1001):
        T += check((A.real + c) + ((A.imag + r) * 1j))

print(T)

