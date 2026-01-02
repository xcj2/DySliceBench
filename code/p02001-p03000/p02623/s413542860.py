from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n, m, k = rl()
    A = rl()
    B = rl()
    Ap = [0]
    for a in A:
        nxt = Ap[-1] + a
        if nxt > k:
            break
        Ap.append(nxt)

    best = bisect.bisect_right(Ap, k) - 1
    # print (best)
    bs = 0
    bcount = 0
    for b in B:
        bs += b
        bcount += 1
        if bs > k:
            break
        diff = k - bs
        acount = bisect.bisect_right(Ap, diff) - 1
        best = max(best, acount + bcount)
    print (best)




mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
