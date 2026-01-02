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
# from statistics import mean,median,mode

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

n = I()
v = RI()

ans1 = 0
ans2 = 0

a = []
b = []
for i in range(n):
    if i%2==0:
        a.append( v[i] )
    else:
        b.append( v[i] )

ac = Counter(a)
bc = Counter(b)

ma = 0
mb = 0

for i in ac:
    if ma<ac[i]:
        ma = ac[i]
        no1 = i
    else:
        pass

for i in bc:
    if mb<bc[i] and i!=no1:
        mb = bc[i]
        no2 = i
    else:
        pass

ans1 += len(a) - ma
ans1 += len(b) - mb

ma = 0
mb = 0

for i in bc:
    if mb<bc[i]:
        mb = bc[i]
        no2 = i
    else:
        pass

for i in ac:
    if ma<ac[i] and i!=no2:
        ma = ac[i]
        no1 = i
    else:
        pass

ans2 += len(a) - ma
ans2 += len(b) - mb

print(min(ans1,ans2))