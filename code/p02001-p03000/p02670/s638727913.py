from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
mod = 1000000007
m = [(0, 1), (1, 0), (-1, 0), (0, -1)]
inf = float('INF')

#solve
def solve():
    n = II()
    p = LI()
    dp = [min(i, j, n - i - 1, n - j - 1) for i in range(n) for j in range(n)]
    c = [1 for i in range(n) for j in range(n)]
    d = defaultdict(tuple)
    for i in range(-1, n + 1):
        for j in range(n):
            d[i * n + j] = (i, j)
    q = [0] * (n ** 2)
    ans = 0
    for pi in p:
        pi -= 1
        ans += dp[pi]
        c[pi] = 0
        q[0] = pi
        p = 0
        l = 1
        while p != l:
            yx = q[p]
            p += 1
            score = dp[yx] + c[yx]
            y, x = d[yx]
            if 0 < y < n - 1:
                if 0 < x < n - 1:
                    myx = yx + n
                    if dp[myx] > score:
                        dp[myx] = score
                        q[l] = myx
                        l += 1
                    myx = yx - n
                    if dp[myx] > score:
                        dp[myx] = score
                        q[l] = myx
                        l += 1
                    myx = yx - 1
                    if dp[myx] > score:
                        dp[myx] = score
                        q[l] = myx
                        l += 1
                    myx = yx + 1
                    if dp[myx] > score:
                        dp[myx] = score
                        q[l] = myx
                        l += 1
                else:
                    if x == 0:
                        myx = yx + 1
                        if dp[myx] > score:
                            dp[myx] = score
                            q[l] = myx
                            l += 1
                    elif x == n - 1:
                        myx = yx - 1
                        if dp[myx] > score:
                            dp[myx] = score
                            q[l] = myx
                            l += 1
            else:
                if y == 0:
                    if 0 < x < n - 1:
                        myx = yx + n
                        if dp[myx] > score:
                            dp[myx] = score
                            q[l] = myx
                            l += 1
                elif y == n - 1:
                    if 0 < x < n - 1:
                        myx = yx - n
                        if dp[myx] > score:
                            dp[myx] = score
                            q[l] = myx
                            l += 1
    print(ans)
    return


#main
if __name__ == '__main__':
    solve()
