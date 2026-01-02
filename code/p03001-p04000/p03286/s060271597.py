def judge(m,i):
    if m==1:
        return 1
    elif m>0:
        if m%(2**i)==0:
            return 0
        else:
            return 1
    else:
        m = -m
        if m%(2**i)==0:
            return 0
        else:
            return 1

def examC():
    n = I()
    N = copy.deepcopy(n)
    i = 0
    ans = []
    while(N!=0):
        cur = judge(N,i+1)
#        print(cur,N)
#        input()
        N -=((-2)**i)*cur
        ans.append(cur)
        i +=1
    if not ans:
        ans = [0]
    print("".join(map(str,ans[::-1])))

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

examC()