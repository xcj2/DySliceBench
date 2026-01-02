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

def SI():
    return input()

def SMI():
    return input().split()

def SRI():
    return list(input().split())

def SCI(n):
    return [ input() for _ in range(n) ]

def SLI(n):
    return [ list(input().split()) for _ in range(n) ]

x,y,z,k = MI()
a = RI()
b = RI()
c = RI()

# a.sort(reverse=True)
# b.sort(reverse=True)
# c.sort(reverse=True)
# M = a[0] + b[0] + c[0]

M = max(a) + max(b) + max(c)

ls = []
for i in range(x):
    for j in range(y):
        ab = a[i] + b[j]
        ls.append(ab)

ls.sort(reverse=True)

ls = ls[:min(k,x*y)]

ls_ans = []
for i in range(min(k,x*y)):
    for j in range(z):
        ls_ans.append( ls[i] + c[j] )
ls_ans.sort(reverse=True)

for i in range(k):
    print(ls_ans[i])