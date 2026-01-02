import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
from collections import Counter
import bisect
from collections import defaultdict
import itertools
def main():
    mod = 998244353
    N, K = MI()
    sec = []
    for i in range(K):
        l, r = MI()
        sec.append((l, r))
    dp = [0 for _ in range(N + 1)]
    dpsum = [0 for _ in range(N + 1)]
    dp[0] = 1
    dpsum[0] = 1
    for i in range(1, N):
        for j in range(K):
            li = i - sec[j][1]
            ri = i - sec[j][0]
            if ri < 0:
                continue
            li = max(li, 0)
            dp[i] += (dpsum[ri] - dpsum[li - 1]) % mod
            dp[i] %= mod
        dpsum[i] = (dpsum[i - 1] + dp[i]) % mod
    print(dp[N - 1])
if __name__ == "__main__":
    main()

