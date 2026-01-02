from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))

def T(i):
    return i * (i + 1) // 2


def solve():
    # n log n : sieving
    # n = ri()
    # sieve = [1] * (n + 1)
    # ans = 1
    # for p in range(2, n + 1):
        # for q in range(p, n + 1, p):
            # sieve[q] += 1
        # ans += p * sieve[p]
    # print (ans)

    # summing with floor n / i technique
    # O(sqrt n)
    n = ri()
    if n in [1,2,3]:
        print ({1:1, 2:5, 3:11}[n])
        return

    sq = int(n**0.5)
    ans = 0
    for i in range(1, sq + 1):
        # print (i, i * T(n // i), T(i) * (T(n // i) - T(n // (i + 1))))
        ans += i * T(n // i)
        ans += T(i) * (T(n // i) - T(n // (i + 1)))

    if sq * (sq + 1) > n:
        ans -= sq * T(n // sq)
    print (ans)





mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
