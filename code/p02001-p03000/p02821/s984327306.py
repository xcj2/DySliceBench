import sys
import math
import cmath
sys.setrecursionlimit(1000000)

def dft_divide(f, l):
    if l == 1:
        return
    ll = l // 2
    f0, f1 = [0] * ll, [0] * ll
    for i in range(ll):
        f0[i] = f[2 * i]
        f1[i] = f[2 * i + 1]
    dft_divide(f0, ll)
    dft_divide(f1, ll)
    dft_solve(f, f0, f1, l)
    return

def dft_solve(f, f0, f1, l):
    ll = l // 2
    zz = cmath.exp(2j * cmath.pi / l)
    z = 1
    for i in range(l):
        f[i] = f0[i % ll] + z * f1[i % ll]
        z *= zz
    return

def idft_divide(f, l):
    if l == 1:
        return
    ll = l // 2
    f0, f1 = [0] * ll, [0] * ll
    for i in range(ll):
        f0[i] = f[2 * i]
        f1[i] = f[2 * i + 1]
    idft_divide(f0, ll)
    idft_divide(f1, ll)
    idft_solve(f, f0, f1, l)
    return

def idft_solve(f, f0, f1, l):
    ll = l // 2
    zz = cmath.exp(-2j * cmath.pi / l)
    z = 1
    for i in range(l):
        f[i] = f0[i % ll] + z * f1[i % ll]
        z *= zz
    return

def multiply(f, g, ma):
    lf, lg = len(f), len(g)
    m = 2 ** (int(math.log2(lf + lg)) + 1)
    for i in range(m - lf):
        f.append(0)
    for i in range(m - lg):
        g.append(0)
    dft_divide(f, m)
    dft_divide(g, m)
    fg = [0] * m
    for i in range(m):
        fg[i] = f[i] * g[i]
    idft_divide(fg, m)
    c = [0] * (2 * ma + 1)
    for i in range(2 * ma + 1):
        c[i] = round(fg[i].real / m)
    return c

n, m = map(int, input().split())
a = list(map(int, input().split()))
ma = max(a)
happiness1 = [0] * (ma + 1)
happiness2 = [0] * (ma + 1)
for i in a:
    happiness1[i] += 1
    happiness2[i] += 1
c = multiply(happiness1, happiness2, ma)
cnt = 0
ans = 0
for i in range(2 * ma, -1, -1):
    if c[i] + cnt >= m:
        ans += (m - cnt) * i
        cnt += (m - cnt)
    else:
        ans += c[i] * i
        cnt += c[i]
    if cnt == m:
        break
print(ans)