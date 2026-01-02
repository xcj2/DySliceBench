#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    counter = [0]*N
    
    for i in range(M):
      A,B = map(int,input().split())
      A -= 1
      B -= 1
      counter[A] = max(counter[A],H[B])
      counter[B] = max(counter[B],H[A])
    ans = 0
    for i in range(N):
      if counter[i] < H[i]:
          ans += 1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()