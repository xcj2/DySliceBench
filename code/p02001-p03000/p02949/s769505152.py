#!/usr/bin/env python3
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
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    print(max(a + b, a - b, a * b))
    return

#B
def B():
    k, x = LI()
    ans = []
    for i in range(x - k + 1, x + k):
        ans.append(i)
    print(*ans)
    return

#C
def C():
    n = II()
    d = defaultdict(int)
    for _ in range(n):
        s = S()
        s.sort()
        d[tuple(s)] += 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    print(ans)
    return

# D
# 解説AC
# 後方から見ていくのはわかったけど。。。
# i日前に選べるバイトの中から一番報酬が大きいを選んでいく
def D():
    n, m = LI()
    q = []
    d = defaultdict(list)
    ans = 0
    for _ in range(n):
        a, b = LI()
        d[a].append(b)
    for i in range(m):
        for di in d[i+1]:
            heappush(q, -di)
        if q:
            ans -= heappop(q)
    print(ans)
    return

#E
def E():
    n,m,p = LI()
    dag = [-inf] * n
    edg = LIR_(m)
    dag[0] = 0
    for i in range(n):
        for a, b, c in edg:
            c += 1
            c -= p
            if dag[a] + c > dag[b]:
                dag[b] = dag[a] + c
    ans = dag[n - 1]
    for i in range(n):
        for a, b, c in edg:
            c += 1
            c -= p
            if dag[a] + c > dag[b]:
                dag[b] = inf
    if ans != dag[n - 1]:
        print(-1)
    else:
        print(max(ans, 0))

    return

#F
def F():
    return

#Solve
if __name__ == '__main__':
    E()
