import sys
mod = pow(10, 9) + 7
sys.setrecursionlimit(pow(10, 8))

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, (y-1)//2)**2 * x % mod
    
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def div(a, b):
    return mul(a, power(b, mod-2))

import sys
input = sys.stdin.readline


N = int(input())

d2 = [1]
inverse = [0, 1]
for _ in range(N):
    d2.append(2*d2[-1]%mod)
for i in range( 2,  10):
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )

G = [[] for _ in range(N+1)]
for v in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

v2i = [0 for _ in range(N+1)]
def itt(v, p):
    cn = 0
    ms = []
    for u in G[v]:
        if u == p:
            continue
        un = itt(u, v)
        ms.append(un)
        cn += un
    if p != None:
        ms.append(N-1-cn)
    v2i[v] = ms
    return cn+1
itt(1, None)
r = 0
for v in range(1, N+1):
    ff = v2i[v]
    for f in ff:
        r += d2[f] - 1 % mod
r = N*d2[N-1]-N-r
for _ in range(N):
    r = r*500000004 % mod
print(r)
