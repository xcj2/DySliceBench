def examB():
    s = S()
    for i,j in enumerate(s):
        if j=="A":
            right = i
            break
    for i,j in enumerate(s[::-1]):
        if j=="Z":
            left = i
            break
    ans = len(s)-right-left
    print(ans)


import sys
import copy
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
