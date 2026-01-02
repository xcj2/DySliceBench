import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter
from heapq import heappush, heappop

p, g, ig = 998244353, 3, 332748118
W = [pow(g, (p - 1) >> i, p) for i in range(24)]
iW = [pow(ig, (p - 1) >> i, p) for i in range(24)]
 
def convolve(a, b):
    def fft(f):
        for l in range(k, 0, -1):
            d = 1 << l - 1
            U = [1]
            for i in range(d):
                U.append(U[-1] * W[l] % p)
 
            for i in range(1 << k - l):
                for j in range(d):
                    s = i * 2 * d + j
                    t = s + d
                    f[s], f[t] = (f[s] + f[t]) % p, U[j] * (f[s] - f[t]) % p
 
    def ifft(f):
        for l in range(1, k + 1):
            d = 1 << l - 1
            U = [1]
            for i in range(d):
                U.append(U[-1] * iW[l] % p)
 
            for i in range(1 << k - l):
                for j in range(d):
                    s = i * 2 * d + j
                    t = s + d
                    f[s], f[t] = (f[s] + f[t] * U[j]) % p, (f[s] - f[t] * U[j]) % p
 
    n0 = len(a) + len(b) - 1
    k = (n0).bit_length()
    n = 1 << k
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    fft(a), fft(b)
    for i in range(n):
        a[i] = a[i] * b[i] % p
    ifft(a)
    invn = pow(n, p - 2, p)
    for i in range(n0):
        a[i] = a[i] * invn % p
    del a[n0:]
    return a

N = int(input())
P = 998244353
nn = 2 * N + 10
fa = [1] * (nn+1)
fainv = [1] * (nn+1)
for i in range(nn):
    fa[i+1] = fa[i] * (i+1) % P
fainv[-1] = pow(fa[-1], P-2, P)
for i in range(nn)[::-1]:
    fainv[i] = fainv[i+1] * (i+1) % P

dfa = [1] * (nn+1)
for i in range(2, nn+1):
    dfa[i] = dfa[i-2] * i % P
dfa += [1]

X = list(Counter([int(input()) for _ in range(2 * N)]).values())
M = len(X)
Y = [[] for _ in range(M)]
for x in X:
    L = [1]
    s = 1
    for i in range(x // 2):
        s = s * ((x - i * 2) * (x - i * 2 - 1) // 2) % P
        L.append(s * fainv[i+1] % P)
    Y.append(L)

for i in range(1, M)[::-1]:
    Y[i] = convolve(Y[i*2], Y[i*2+1])

ans = 0
for i, x in enumerate(Y[1]):
    ans = (ans + x * (-1 if i & 1 else 1) * dfa[N * 2 - i * 2 - 1]) % P
print(ans)