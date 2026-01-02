from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n = ri()
    C = input()
    if C[0] == "R":
        R = [1]
        W = [0]
    else:
        R = [0]
        W = [1]

    for c in C[1:]:
        if c == "R":
            R.append(1 + R[-1])
            W.append(W[-1])
        else:
            W.append(1 + W[-1])
            R.append(R[-1])

    best_cost = min(R[-1], W[-1])
    for i in range(n):
        rl = R[i]
        wl = W[i]
        rr = R[-1] - rl
        wr = W[-1] - wl
        swaps = min(wl, rr)
        flips = wl + rr - 2 * swaps
        best_cost = min(best_cost, flips + swaps)
    print (best_cost)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
