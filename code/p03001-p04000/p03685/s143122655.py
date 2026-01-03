def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    R, C, N = LI()
    P = []
    P1 = []; P2 = []; P3 = []; P4 = []
    index = 0
    for i in range(N):
        x1,y1,x2,y2 = LI()
        if (x1 not in (0,R)) and (y1 not in (0,C)):
            continue
        if (x2 not in (0,R)) and (y2 not in (0,C)):
            continue

        if x1==0:
            P1.append((x1, y1, index))
        elif y1 == C:
            P2.append((x1, y1, index))
        elif x1==R:
            P3.append((x1, y1, index))
        else:
            P4.append((x1, y1, index))

        if x2==0:
            P1.append((x2, y2, index))
        elif y2 == C:
            P2.append((x2, y2, index))
        elif x2==R:
            P3.append((x2, y2, index))
        else:
            P4.append((x2, y2, index))
        index += 1
    P1.sort(key=lambda x:x[1])
    P2.sort()
    P3.sort(key=lambda x:x[1], reverse=True)
    P4.sort(reverse=True)
    for _,_,p in P1:
        P.append(p)
    for _,_,p in P2:
        P.append(p)
    for _,_,p in P3:
        P.append(p)
    for _,_,p in P4:
        P.append(p)
    #print(P)

    que = deque()
    for index in P:
        if que:
            now = que.pop()
            if index==now:
                continue
            que.append(now)
            que.append(index)
        else:
            que.append(index)
    if que:
        print("NO")
    else:
        print("YES")
    return

def examF():
    ans = 0
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""