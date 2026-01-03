def examB():
    N = I()
    ansC = [(i+1) for i in range(N)]
    k = 0
    while(len(ansC)>=2):
        cur = []
        for i in ansC:
            if i % 2 == 0:
                cur.append(i // 2)
        ansC = cur
        k +=1
        if len(ansC)==1:
            break
    ans = 2**k
    print(ans)

import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
