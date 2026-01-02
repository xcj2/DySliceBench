def examA():
    S = SI()
    if len(S)==3:
        ans = S[::-1]
    else:
        ans = S
    print(ans)
    return

def examB():
    A, B, K = LI()
    for i in range(K):
        if i%2==0:
            B +=A//2
            A //=2
        else:
            A +=B//2
            B //=2
    print(A,B)
    return

def examC():
    N = I()
    A = [I() for _ in range(N)]
    A.sort()
    A1 = A[:N//2]; A2 = A[N//2:]
    ans = 0; cur = 0
    for i in range(len(A2)):
        if i<len(A1):
            cur +=(A2[i]-A1[i])
        if i-1>=0:
            cur +=(A2[i]-A1[i-1])
    if N%2==1:
        cur += (A2[-1] - A2[1])
    ans = max(ans,cur)
#    print(A1,A2)
#    print(ans)
    if N%2==1:
        A1 = A[:1+(N//2)]; A2 = A[1+(N//2):]
        cur = 0
        for i in range(len(A1)):
            if i < len(A2):
                cur += (A2[i] - A1[i])
            if i - 1 >= 0:
                cur += (A2[i-1] - A1[i])
        cur +=(A1[-2]-A1[0])
        ans = max(ans, cur)
#    print(A1,A2)
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
    examC()
