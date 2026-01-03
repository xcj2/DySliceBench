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

N,W = MI()
WV = LI(N)

ls_w = mycol(WV,0)
ls_w = list(set(ls_w))
ls_w.sort()
if len(ls_w)==3:
    ls_w = [0] + ls_w
elif len(ls_w)==2:
    ls_w = [0,0] + ls_w
elif len(ls_w)==1:
    ls_w = [0,0,0] + ls_w
else:
    pass
# print(ls_w)

a = []
b = []
c = []
d = []
for i in range(N):
    w = WV[i][0]
    v = WV[i][1]
    ind = ls_w.index(w)
    if ind==0:
        a.append(v)
    elif ind==1:
        b.append(v)
    elif ind==2:
        c.append(v)
    elif ind==3:
        d.append(v)
    else:
        print("E")
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
d.sort(reverse=True)
# print("---")
# print(a)
# print(b)
# print(c)
# print(d)
# print("---")

M = -1*INF

for i in range(len(a)+1):
    for j in range(len(b)+1):
        for k in range(len(c)+1):
            for l in range(len(d)+1):
                w = i*ls_w[0] + j*ls_w[1] + k*ls_w[2] + l*ls_w[3]
                if w>W:
                    pass
                else:
                    v = sum(a[:i]) + sum(b[:j]) + sum(c[:k]) + sum(d[:l])
                    M = max(M,v)
print(M)