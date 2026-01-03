def examA():
    group1 = [1,3,5,7,8,10,12]
    group2 = [4,6,9,11]
    x,y = LI()
    ans = "No"
    if x in group1 and y in group1:
        ans = "Yes"
    elif x in group2 and y in group2:
        ans = "Yes"
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

examA()
