def examD():
    N = I()
    s = S()
    ans = ""
    animal = [None, "S", "W"]
    ansC = ""
    for i in range(4):
        cur = ""
        if i==0:
            ansC = [1,1]
        elif i==1:
            ansC = [1,-1]
        elif i==2:
            ansC = [-1,1]
        elif i==3:
            ansC = [-1,-1]
        if (s[0]=="o" and ansC[0]==1) or (s[0]=="x" and ansC[0]==(-1)):
            cur = ansC[1]
        else:
            cur = ansC[1]*(-1)

        for j in range(1,N):
            if (s[j]=="o" and ansC[j]==1) or (s[j]=="x" and ansC[j]==(-1)):
                ansC.append(ansC[j-1])
            else:
                ansC.append(ansC[j-1]*(-1))
        if ansC[N-1]==cur and ansC[N]==ansC[0]:
            for i in ansC[:N]:
                ans = ans + animal[i]
            break
    if not ans:
        ans = int(-1)
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

examD()
