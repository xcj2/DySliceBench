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

def myinput():
    return map(int,input().split())

def mylistinput(n):
    return [ list(myinput()) for _ in range(n) ]

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

n = int(input())
ls_a = []
ls_xy = []
for i in range(n):
    a = int(input())
    ls_a.append(a)
    xy = mylistinput(a)
    ls_xy.append(xy)
# print(a)
# print(ls_xy)

ans = 0
for i in range(2**n):
    flag = True
    for j in range(n):
        if i & (2**j):
            for k in range(len(ls_xy[j])):
                x = ls_xy[j][k][0] - 1
                y = ls_xy[j][k][1]
                if y==1:
                    if i & (2**x) > 0:
                        pass
                    else:
                        flag = False
                elif y==0:
                    if i & (2**x) == 0:
                        pass
                    else:
                        flag = False
    if flag:
        tmp = sum( list(map(int,list(bin(i)[2:]))) )
        ans = max( ans, tmp )

print(ans)            