def pff(m):
    pf = {}
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1: pf[m] = 1
    return pf
def examD():
    N = I()
    d = defaultdict(int)
    for i in range(2,N+1):
        cur  = pff(i)
        for key,j in cur.items():
            d[key] +=j
#    print(d)
    Num = defaultdict(int)
    for i in d.values():
        for j in [3,5,15,25,75]:
            if i>=j-1:
                Num[j] +=1
            else:
                break
#    print(Num)
    ans = 0
    ans += (Num[5]*(Num[5]-1)//2)*(Num[3]-2)
    ans += Num[15]*(Num[5]-1)
    ans += Num[25]*(Num[3]-1)
    ans += Num[75]
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
    examD()
