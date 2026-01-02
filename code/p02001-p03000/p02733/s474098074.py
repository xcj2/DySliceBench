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
    h, w, k = LI()
    s = SR(h)
    bit_length = [0] 
    for i in range((h-1)): 
        bit_length += [x + 1 for x in bit_length]
    ans = inf
    for i in range(1 << (h - 1)):
        tmp = [0] * (bit_length[i] + 1)
        num = 0
        for x in range(w):
            t = 0
            f = 0
            tmp1 = [0] * (bit_length[i]+1)
            for y in range(h):
                # print(t)
                tmp[t] += int(s[y][x])
                tmp1[t] += int(s[y][x])
                if tmp[t] > k:
                    f = 1
                if tmp1[t] > k:
                    break
                t += 1 & (i >> y) 

            else:
                if f:
                    num += 1
                    # print(tmp)
                    tmp = tmp1[::1]
                continue
            break
        else:
            # print(tmp,tmp1,bin(i),num)
            ans = min(ans, bit_length[i] + num)
    print(ans)


        
    return


#main
if __name__ == '__main__':
    solve()
