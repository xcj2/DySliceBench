def examC():
    H, W = LI()
    A = [SI() for _ in range(H)]
    d = defaultdict(int)
    ans = "Yes"
    for a in A:
        for s in a:
            d[s] +=1
#    print(d)
    h = H//2; w = W//2; k = h*w
    for key,i in d.items():
        if k == 0:
            break
        while(d[key]>=4):
            d[key]-=4
            k -=1
            if k == 0:
                break
    if k>0:
        ans = "No"
#    print(d,k)
    k = 0
    if H%2==1:
        k +=w
    if W%2==1:
        k +=h
    for key,i in d.items():
        if k ==0:
            break
        while(d[key]>=2):
            d[key] -= 2
            k -= 1
            if k == 0:
                break
    if k>0:
        ans = "No"
#    print(d,k)
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
    examC()
