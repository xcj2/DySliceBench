def examA():
    Q, H, S, D = LI()
    N = I()
    economical2 = min(Q*8, H*4, S*2, D)
    economical1 = min(Q*4, H*2, S)
    ans = (N//2)*economical2 + (N%2)*economical1
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examA()