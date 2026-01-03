def gcd(a,b):
    if a>b :
        while b!=0:
            a,b = b,a%b
        return a
    else :
        while a!=0:
            a,b = b%a,a
        return b
def examB():
    A, B, C = LI()
    cur = gcd(A,B)
    if C%cur==0:
        ans = "YES"
    else:
        ans = "NO"
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