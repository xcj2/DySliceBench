def examC():
    N = I()
    A = LI()
    Ad = [0]*N
    for i in range(N):
        Ad[i] = A[i]-(i+1)
    Ad.sort()
#    print(Ad)
    b = Ad[N//2]
    ans = 0
    for a in Ad:
        ans +=abs(a-b)
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = 10**18

if __name__ == '__main__':
    examC()
