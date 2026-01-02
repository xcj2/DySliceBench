from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))

def T(n):
    return n * (n + 1) // 2

def S(a, b):
    return T(b) - T(a - 1)

def solve():
    n, k = rl()
    ans = 1
    for i in range(k, n + 1):
        lo = T(i - 1)
        hi = S(n - i + 1, n)
        ans += hi - lo + 1
        ans %= (10**9 + 7)
        # print (ans)

    print (ans)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
