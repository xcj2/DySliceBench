def examA():
    A, B = LI()
    if B%A==0:
        ans = A+B
    else:
        ans = B-A
    print(ans)
    return

def examB():
    N, M = LI()
    Flag = [0]*M
    for i in range(N):
        K = LI()
        for j in range(1,K[0]+1):
            Flag[K[j]-1] +=1
    ans = 0
    for i in Flag:
        if i==N:
            ans +=1
    print(ans)
    return

def gcd(x,y):
    if y==0:
        return x
    while(y!=0):
        x, y = y,x%y
    return x
def examC():
    N = I()
    A = LI()
    cur = A[0]
    for i in range(N-1):
        cur = gcd(cur,A[i+1])
    ans = cur
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
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examC()
