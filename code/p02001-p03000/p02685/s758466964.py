from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def solve():
    n, m, k = rl()
    mod = 998244353
    ans = 0
    C = 1
    for d in range(k + 1):
        # print (d)
        ans += m * pow(m - 1, n - 1 - d, mod) * C
        ans %= mod
        C = (C * (n - 1 - d) * modinv(d + 1, mod)) % mod
    print (ans)





mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
