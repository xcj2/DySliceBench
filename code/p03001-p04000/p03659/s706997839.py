import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = I()
    A = LI()
    leftThanMe = [0 for _ in range(N+1)]
    rightThanMe = [0 for _ in range(N+1)]
    for i in range(N-1):
        leftThanMe[i+1] = A[i] + leftThanMe[i]
    for i in range(1, N)[::-1]:
        rightThanMe[i-1] = A[i] + rightThanMe[i]
    ans = inf
    for i in range(N-1):
        val = abs(leftThanMe[i] + A[i] - rightThanMe[i])
        ans = min(ans, val)
    print(ans)
main()

