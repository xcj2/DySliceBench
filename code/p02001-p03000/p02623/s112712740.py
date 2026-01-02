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
    N, M, K = LI()
    A=  LI()
    B = LI()
    cumA = [0] * (N+1)
    cumB = [0] * (M + 1)
    for i in range(N):
        cumA[i+1] = cumA[i] + A[i]

    for j in range(M):
        cumB[j+1] = cumB[j] + B[j]

    ans = 0
    for read_a in range(N+1):
        left = K - cumA[read_a]
        if left < 0:
            continue
        if left == 0:
            ans = max(ans, read_a)
            continue
        # print('read_a: ', read_a)
        # print('cumA[read_a]: ', cumA[read_a])
        # print('left: ', left)
        # print('cumB: ', cumB)
        ix = bisect.bisect_right(cumB, left)
        # print('ix: ', ix)
        ans = max(ans, read_a + (ix - 1))
        # print()
    print(ans)

main()

