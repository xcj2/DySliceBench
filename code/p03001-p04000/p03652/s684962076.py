def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    N, M = LI()
    A = [LI() for _ in range(N)]
    not_flag = [False]*M
    ans = N
    for i in range(M):
        d = defaultdict(int)
        for k in range(N):
            for j in range(M):
                cur = A[k][j]-1
                if not_flag[cur]:
                    continue
                d[cur] +=1
                break
        d = sorted(d.items(),key=lambda x:x[1],reverse=True)
#        print(d)
        not_flag[d[0][0]] = True
        ans = min(ans,d[0][1])
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LFI(): return list(map(float,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examB()

"""

"""