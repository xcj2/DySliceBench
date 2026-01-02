def examA():
    N = I(); A = LI()
    sumnale = sum(A)/N
    cur = 10**9; curL = 0
    for i in range(N):
        if cur>abs(A[i]-sumnale):
            cur = abs(A[i]-sumnale)
            curL = i
    ans = curL
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
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examA()
