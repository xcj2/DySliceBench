def examA():
    N, A, B = LI()
    if (A-B)%2==0:
        ans = "Alice"
    else:
        ans = "Borys"
    print(ans)
    return

def examB():
    K = I()
    A = LI()
    cur = 2
    for i in range(K-1,-1,-1):
        a = A[i]
        if A[i]>cur:
            print(-1)
            exit()
        cur = (cur//a+1)*a-1
#        print(cur)
    maxA = cur; cur = 2
    for i in range(K-1,-1,-1):
        a = A[i]
        if cur<=a:
            cur = a
        else:
            cur = a*((cur-1)//a+1)
    minA = cur
    if minA>maxA:
        print(-1)
        exit()
    print(minA,maxA)
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
    examB()
