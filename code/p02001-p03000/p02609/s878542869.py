N = int(input())
X = input()

def e(x, y):
    t = [0] * len(x)
    if y <= 0: return (-1, t)
    if y == 1: return (0, t)
    res = 0
    z = 1
    for i in range(len(x) - 1, -1, -1):
        t[i] = z
        if x[i] == '1':
            res = (res + z) % y
        z = (z << 1) % y
    return (res, t)

def popcount(x):
    x = (x & 0x5555555555555555) + (x >> 1 & 0x5555555555555555)
    x = (x & 0x3333333333333333) + (x >> 2 & 0x3333333333333333)
    x = x + (x >> 4) & 0x0f0f0f0f0f0f0f0f
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7f

fm = [-1] * (2 * (10 ** 5) + 1)
fm[0] = 0
def f(x):
    if fm[x] >= 0: return fm[x]
    fm[x] = 1 + f(x % popcount(x))
    return fm[x]


pc = X.count('1')
s0, t0 = e(X, pc + 1)
s1, t1 = e(X, pc - 1)

for i in range(N):
    t = 0
    if X[i] == '0':
        t = (s0 + t0[i]) % (pc + 1)
    else:
        if pc == 1:
            print(0)
            continue
        t = (s1 - t1[i]) % (pc - 1)
    print(1 + f(t))
