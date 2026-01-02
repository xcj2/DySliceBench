import sys
import math
import cmath
sys.setrecursionlimit(1000000)

def dft_divide(f, l):
    if l == 1:
        return
    ll = l // 2
    f0 = [f[2 * i] for i in range(ll)]
    f1 = [f[2 * i + 1] for i in range(ll)]
    dft_divide(f0, ll)
    dft_divide(f1, ll)
    dft_solve(f, f0, f1, l)
    return

def dft_solve(f, f0, f1, l):
    ll = l // 2
    for i in range(l):
        z = cmath.exp(2j * i * cmath.pi / l)
        f[i] = f0[i % ll] + z * f1[i % ll]
    return

def idft_divide(f, l):
    if l == 1:
        return
    ll = l // 2
    f0 = [f[2 * i] for i in range(ll)]
    f1 = [f[2 * i + 1] for i in range(ll)]
    idft_divide(f0, ll)
    idft_divide(f1, ll)
    idft_solve(f, f0, f1, l)
    return

def idft_solve(f, f0, f1, l):
    ll = l // 2
    for i in range(l):
        z = cmath.exp(-2j * i * cmath.pi / l)
        f[i] = f0[i % ll] + z * f1[i % ll]
    return

def multiply(f, g):
    lf, lg = len(f), len(g)
    m = 2 ** (int(math.log2(lf + lg)) + 1)
    for i in range(m - lf):
        f.append(0)
    for i in range(m - lg):
        g.append(0)
    dft_divide(f, m)
    dft_divide(g, m)
    fg = [f[i] * g[i] for i in range(m)]
    idft_divide(fg, m)
    c = [round(fg[i].real / m) for i in range(m)]
    return c, m

n, m = map(int, input().split())
a = list(map(int, input().split()))
ma = max(a)
happiness1 = [0] * (ma + 1)
happiness2 = [0] * (ma + 1)
for i in a:
    happiness1[i] += 1
    happiness2[i] += 1
c, lc = multiply(happiness1, happiness2)
cnt = 0
ans = 0
for i in range(min(200000, lc - 1), -1, -1):
    if c[i] + cnt >= m:
        ans += (m - cnt) * i
        cnt += (m - cnt)
    else:
        ans += c[i] * i
        cnt += c[i]
    if cnt == m:
        break
print(ans)