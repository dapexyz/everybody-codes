with open(0) as f:
    line = f.read().strip()

    X, Y = tuple(map(int, line.split('[')[1].split(']')[0].split(',')))
    A = X + Y*1j

result = 0 + 0*1j

for i in range(3):
    result *= result
    result = (int(result.real / 10)) + (int(result.imag / 10))*1j
    result += A

print(f"[{int(result.real)},{int(result.imag)}]")