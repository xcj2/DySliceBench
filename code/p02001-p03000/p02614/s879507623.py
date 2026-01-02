import sys, math,os
from io import BytesIO, IOBase
#data = BytesIO(os.read(0,os.fstat(0).st_size)).readline
# from bisect import bisect_left as bl, bisect_right as br, insort
# from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
# from decimal import Decimal
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
#sys.setrecursionlimit(100000 + 1)
INF = 10**9
mod = 998244353


def recur1(r,c,a):
    global ans
    if a==w:
        cnt=0
        for i in range(h):
            for j in range(w):
                if i in r or j in c:
                    continue
                if mat[i][j] == '#':
                    cnt += 1
        if cnt==k:
            ans+=1
    else:
        recur1(r,c, a + 1)
        c1=c.copy()
        c1.add(a)
        recur1(r,c1, a + 1)

def recur(r,a):
    if a==h:
        recur1(r,set(),0)
    else:
        recur(r,a+1)
        r1=r.copy()
        r1.add(a)
        recur(r1,a+1)

h,w,k=mdata()
ans=0
mat=[data() for i in range(h)]
recur(set(),0)
out(ans)






