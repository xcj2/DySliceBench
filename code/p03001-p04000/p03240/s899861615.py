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
xyh = LI(n)

xyh = mysort(xyh,2,True)
# pprint(xyh)

for i in range(101):
    for j in range(101):
        flag = True
        for k in range(n):
            x = xyh[k][0]
            y = xyh[k][1]
            h = xyh[k][2]
            if k==0: 
                H = h + abs(x-i) + abs(y-j)
            elif k==(n-1):
                l = max( H - abs(x-i) - abs(y-j), 0 )
                if l==h:
                    ans = [i,j,H]
                else:
                    flag = False
            else:
                l = max( H - abs(x-i) - abs(y-j), 0 )
                if l==h:
                    pass
                else:
                    flag = False
        if flag:
            myoutput(ans,True)
            exit()
        else:
            continue
exit()