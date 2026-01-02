
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

#solve
def solve():
    t1, t2 = LI()
    a1, a2 = LI()
    b1, b2 = LI()
    if t1 * a1 + t2 * a2 == t1 * b1 + t2 * b2:
        print("infinity")
        return
    if t1 * a1 > t1 * b1:
        if t1 * a1 + t2 * a2 > t1 * b1 + t2 * b2:
            print(0)
            return
        else:
            x = t1 * (a1 - b1) / (-t1 * (a1 - b1) + t2 * (b2 - a2))
            if x.is_integer():
                print(2 * (t1 * (a1 - b1) // (-t1 * (a1 - b1) + t2 * (b2 - a2))))
            else:
                print(2 * (t1 * (a1 - b1) // (-t1 * (a1 - b1) + t2 * (b2 - a2))) + 1)
            return
    elif t1 * a1 < t1 * b1:
        if t1 * a1 + t2 * a2 < t1 * b1 + t2 * b2:
            print(0)
            return
        else:
            x = t1 * (b1 - a1) / (-t1 * (b1 - a1) + t2 * (a2 - b2))
            if x.is_integer():
                print(2 * (t1 * (b1 - a1) // (-t1 * (b1 - a1) + t2 * (a2 - b2))))
            else:
                print(2 * (t1 * (b1 - a1) // (-t1 * (b1 - a1) + t2 * (a2 - b2))) + 1)
            return
    return


#main
if __name__ == '__main__':
    solve()
