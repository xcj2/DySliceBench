def examF():
    T = LI()
    A = LI()
    B = LI()
    loop1 = T[0]*(A[0]-B[0])
    loop2 = T[1]*(A[1]-B[1])
    now = loop1
    cur = loop1 + loop2
    if now>0 and cur>0:
        ans = 0
    elif now<0 and cur<0:
        ans = 0
    else:
#        print(now,cur)
        if cur!=0:
            ans = abs(now)//abs(cur)*2
            if abs(now)%abs(cur)!=0:
                judge = now + cur*ans//2
                if (now>0 and judge+loop1>0) or (now<0 and judge+loop1<0):
                    ans +=1
        else:
            ans = "infinity"
    print(ans)
    return

import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examF()
