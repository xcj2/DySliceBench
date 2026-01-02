import sys

from collections import deque
# q = deque(); q.append(x); q.appendleft(x); q.pop() -> x; q.popleft() -> x
from collections import defaultdict
# d = defaultdict(lambda: []); d[key] -> []
import heapq
# hq = []; heapq.heappush(hq, x); heapq.heappop(hq) -> x; heapq.heappushpop(hq, x) -> x
import bisect
# i = bisect.bisect_left([1,2,3,4], 1.5); i = bisect.bisect_right([4,3,2,1], 1.5)

#import numpy as np
#from scipy.misc import comb

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

def fib_memo(n):
    memo = [0] * (n+1)
    memo[0] = 1
    if n < 1:
        return memo
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo

def main_nondp():
    N, M = i2nn()
    A = ii2nn(M)
    MOD = int(1e+9) + 7
    D = [0] * (M+1)
    if M == 0:
        D[0] = N
    else:
        D[0] = A[0] - 1
        for i in range(1, M):
            t = A[i] - A[i-1] - 2
            if t <= -1:
                print(0)
                return
            D[i] = t
        D[M] = N - A[M-1] - 1
    n = 1
    memo = fib_memo(max(D))
    for d in D:
        n = (n * memo[d]) % MOD
    print(n)

def main():
    N, M = i2nn()
    A = ii2nn(M)
    MOD = int(1e+9) + 7
    AS = set(A)
    dp = [0] * (N+9)  # i段目のパターン数
    dp[0] = 1
    for i in range(1, N+1):
        if i in AS:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
    print(dp[N])

main()
