def examB():
    A = S()
    B = S()
    if len(A)>len(B):
        ans = "GREATER"
    elif len(A)<len(B):
        ans = "LESS"
    else:
        i = 0; k = 0; cur = 0; loop = len(A)
        while i==k:
            if cur==loop:
                ans = "EQUAL"
                break
            i = int(A[cur])
            k = int(B[cur])
            if i>k:
                ans = "GREATER"
                break
            elif i<k:
                ans = "LESS"
                break
            cur +=1
    print(ans)

import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
