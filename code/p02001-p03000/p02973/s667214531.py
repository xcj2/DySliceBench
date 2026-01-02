#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys, math, bisect, random, itertools
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
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
    n = II()
    print(n*n*3)
    return

#B
def B():
    n, d = LI()
    print((n-1)//(2*d+1)+1)
    return

#C
def C():
    n = II()
    a = IR(n)
    b = a[::1]
    b.sort()
    for i in range(n):
        if a[i] == b[-1]:
            print(b[-2])
        else:
            print(b[-1])
    return

#D
def D():
    n = II()
    a = [0] + LI()
    for i in range(n // 2, 0, -1):
        x = sum(a[i::i])
        if x % 2 != a[i]:
            a[i] ^= 1
    ans = []
    x = 0
    for i in range(1, n + 1):
        if a[i]:
            ans.append(str(i))
            x += 1
    print(x)
    if x == 0:
        return
    print(" ".join(ans))
    return

#E
def E():
    n = II()
    a = IR(n)
    dp = deque([a[0]])
    ans = 1
    for i in a[1:]:
        x = bisect_right(dp, i)
        y = bisect_left(dp, i)
        if y == 0:
            ans += 1
            dp.appendleft(i)
        else:
            if x == y:
                dp[y - 1] = i
            else:
                if y >= ans:
                    ans += 1
                    dp.append(i)
                else:
                    dp[y - 1] = i
    print(ans)
    return

#F
def F():
    return

#Solve
if __name__ == '__main__':
    E()
