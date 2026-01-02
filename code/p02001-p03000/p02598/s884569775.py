from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n, k = rl()
    A = rl()

    def check(L):
        cuts = 0
        for a in A:
            cuts += (a - 1) // L
            if cuts > k:
                return False
        return True

    lo = 0
    hi = max(A)
    if k == 0:
        print (hi)
        return

    while lo < hi - 1:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid

    print (hi)
    return








mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
