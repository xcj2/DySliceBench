def examB():
    N, M, K = LI()
    ans = "No"
    for i in range(N+1):
        for j in range(M+1):
            cur = M*i + N*j - i*j*2
#            print(i,j,cur)
            if cur==K:
                ans = "Yes"
                break
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
    examB()
