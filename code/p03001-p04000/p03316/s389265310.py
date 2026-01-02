def examA():
    def calc_L(x1,y1,x2,y2):
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    N = I()
    X = [LI()for _ in range(N)]
    ans = 0
    for x in itertools.permutations(X):
        cur = 0
        for i in range(1,N):
            cur += calc_L(x[i-1][0],x[i-1][1],x[i][0],x[i][1])
        #print(x,cur)
        ans += cur
    for i in range(1,N+1):
        ans /= i
    print(ans)
    return

def examB():
    def judge(n):
        sn = 0
        for i in n:
            sn += int(i)
        if int(n)%sn==0:
            return "Yes"
        return "No"
    N = SI()
    ans = judge(N)
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

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examB()

"""

"""