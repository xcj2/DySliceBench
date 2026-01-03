def examA():
    a, b = LI()
    if a>0:
        ans = "Positive"
        print(ans)
        return
    if b>=0:
        ans = "Zero"
    else:
        judge = b-a
        if judge%2==1:
            ans = "Positive"
        else:
            ans = "Negative"
    print(ans)
    return

def examB():
    N, M = LI()
    boal = [1]*N
    d = defaultdict(bool)
    d[0] = True
    for _ in range(M):
        x,y = LI()
        boal[x-1] -=1
        boal[y-1] +=1
        if d[x-1]:
            d[y-1] = True
        if boal[x-1]==0:
            d[x-1] = False
    ans = sum(d.values())
    print(ans)
    return

def examC():
    N, L = LI()
    A = LI(); cur = -1
    ans = "Impossible"
    for i in range(N-1):
        if A[i]+A[i+1]>=L:
            ans = "Possible"
            cur = i
            break
    print(ans)
    if cur==-1:
        return
    ansC = []
    for i in range(cur):
        ansC.append(i)
    for i in range(N-2,cur,-1):
        ansC.append(i)
    ansC.append(cur)
    for v in ansC:
        print(v+1)
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
