import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    q = deque()
    s = S()
    for c in s:
        q.append(c)
    Q = I()
    backward = False
    for _ in range(Q):
        query = LS()
        if int(query[0]) == 1:
            backward = not backward
            continue
        _, f, c = query
        f = int(f)
        if backward and f == 1:
            # ushiro ni tsuika
            q.append(c)
        if backward and f == 2:
            # mae ni tsuika
            q.appendleft(c)
        if not backward and f == 1:
            # mae
            q.appendleft(c)
        if not backward and f == 2:
            # ushiro
            q.append(c)
    if not backward:
        ans = ''.join(q)
    else:
        q.reverse()
        ans = ''.join(q)
    print(ans)
main()

