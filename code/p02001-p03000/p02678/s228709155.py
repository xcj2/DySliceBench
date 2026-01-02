from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import product,permutations,combinations,combinations_with_replacement
from collections import defaultdict,Counter
from bisect import bisect_left,bisect_right
# from math import gcd,ceil,floor,factorial
# from fractions import gcd
from functools import reduce
from pprint import pprint

INF = float("inf")

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col,reverse_flag):
    data.sort(key=lambda x:x[col],reverse=reverse_flag)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

def mycount(ls,x):
    # lsはソート済みであること
    l = bisect_left(ls,x)
    r = bisect_right(ls,x)
    return (r-l)

def myoutput(ls,space=True):
    if space:
        if len(ls)==0:
            print(" ")
        elif type(ls[0])==str:
            print(" ".join(ls))
        elif type(ls[0])==int:
            print(" ".join(map(str,ls)))
        else:
            print("Output Error")
    else:
        if len(ls)==0:
            print("")
        elif type(ls[0])==str:
            print("".join(ls))
        elif type(ls[0])==int:
            print("".join(map(str,ls)))
        else:
            print("Output Error")

def I():
    return int(input())

def MI():
    return map(int,input().split())

def RI():
    return list(map(int,input().split()))

def CI(n):
    return [ int(input()) for _ in range(n) ]

def LI(n):
    return [ list(map(int,input().split())) for _ in range(n) ]

def S():
    return input()

def MS():
    return input().split()

def RS():
    return list(input().split())

def CS(n):
    return [ input() for _ in range(n) ]

def LS(n):
    return [ list(input().split()) for _ in range(n) ]

n,m = MI()
ab = LI(m)

g = [ [] for _ in range(n) ]
for i in range(m):
    a = ab[i][0] - 1
    b = ab[i][1] - 1
    g[a].append(b)
    g[b].append(a)
# print(g)

ls_ans = [-1]*n

q = deque()
q.append(0)

while q:
    t = q.popleft()
    ls = g[t]
    for i in ls:
        if ls_ans[i]==-1:
            ls_ans[i] = t
            q.append(i)
        else:
            pass
# print(ls_ans)

if -1 in ls_ans:
    print("No")
else:
    for i in range(n):
        if i==0:
            print("Yes")
        else:
            print( ls_ans[i] + 1 )