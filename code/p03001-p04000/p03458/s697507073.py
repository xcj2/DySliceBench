#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(str, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b = LI()
    ans = ['Odd', 'Even']
    print(ans[(a*b)%2-1])
    return

#B
def B():
    a, b = map(str,input().split())
    a = a + b
    if math.sqrt(int(a)).is_integer():
        print("Yes")
    else:
        print("No")
    return

#C
def C():
    n = II()
    pre = (0, 0, 0)
    for _ in range(n):
        t,x,y = LI()
        dist = abs(pre[0] - x) + abs(pre[1] - y)
        if dist <= t - pre[2] and dist % 2 == (t - pre[2]) % 2:
            pre = (x, y, t)
            continue
        print("No")
        return
    print("Yes")
    return

# D
# 解説AC
# prd_xxxさんのを参考にしたけど理解できてないので絶対に理解すること
# https://atcoder.jp/contests/abc086/submissions/3454297
# PS: 2019/10/12
# なんとなく理解
# まず白の情報は市松模様的にk右に行ったところが黒になるという情報と同じ
# 更に座標を2*kの剰余で考えても問題ない
# あとは2次元累積和をとって市松模様の一番左下に当たる白の領域の右上が
# どの位置にあるかはk*k通りあるのでそれを試してその時の模様における
# 黒配置がどの数ただしくなるか調べる
def D():
    n, k = LI()
    dp = [[0] * (2 * k + 1) for i in range(2 * k + 1)]
    for _ in range(n):
        x, y, c = LS()
        x, y = int(x), int(y)
        if c == "W":
            dp[y % (2 * k) + 1][(x + k) % (2 * k) + 1] += 1
        else:
            dp[y % (2 * k) + 1][x % (2 * k) + 1] += 1
    for y in range(2 * k + 1):
        for x in range(1, 2 * k + 1):
            dp[y][x] += dp[y][x - 1]
    for y in range(1, 2 * k + 1):
        for x in range(2 * k + 1):
            dp[y][x] += dp[y - 1][x]
    
    def count(l, r, d, u):
        return dp[d][l] - dp[d][r] - dp[u][l] + dp[u][r]
    
    ans = 0
    for i in range(k):
        for j in range(k):
            tmp = count(j, j + k, i, i + k) + count(0, j, 0, i) + count(j + k, 2 * k, 0, i) + \
                 count(0, j, i + k, 2 * k) + count(j + k, 2 * k, i + k, 2 * k)
            ans = max(ans, tmp, n - tmp)
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
