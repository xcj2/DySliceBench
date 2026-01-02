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
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n, k, c = LI()
    s = S()
    ans = [inf]
    tmp = -inf
    for i in range(n - 1, -1, -1):
        if ans[-1] - c > i and s[i] == "o":
            ans.append(i)
            if len(ans) > k:
                break
    ans.remove(inf)
    ans.sort()
    if len(ans) != k:
        return
    t_ans = [0] * (n + 1)
    for i in range(n):
        if s[i] == "o" and tmp + c + 1 <= i:
            tmp = i
            t_ans[i+1] = t_ans[i] + 1
        else:
            t_ans[i+1] = t_ans[i]
    tt = []
    tmp = 0
    for tmp, ai in enumerate(ans):
        if ai == 0:
            tt.append(str(ai + 1))
            continue
        if t_ans[ai] == tmp:
            tt.append(str(ai + 1))
    print("\n".join(tt))




    return


#main
if __name__ == '__main__':
    solve()
