def examA():
    N = I()
    S = SI(); T = SI()
    ans = 2*N
    for l in range(N-1,-1,-1):
        flag = True
        for i in range(l+1):
            if S[N-1-i] != T[l-i]:
                flag = False
                break
        if flag:
            ans -=(l+1)
            break
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
