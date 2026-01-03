def examC():
    sx, sy, tx, ty = LI()
    ans = ""
    k = 1
    for _ in range(2):
        if k==-1:
            ans = ans + "L"
            ty +=1; tx +=1

        for _ in range(ty - sy):
            ans = ans + "U"
        for _ in range(tx - sx):
            ans = ans + "R"
        k *= (-1)

        if k==1:
            ans = ans + "D"
            ans = ans + "R"

        for _ in range(ty - sy):
            ans = ans + "D"
        for _ in range(tx - sx):
            ans = ans + "L"

        if k==1:
            ans = ans + "U"
    print("".join(map(str,ans)))

import sys
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()