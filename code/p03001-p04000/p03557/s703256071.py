from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
from bisect import bisect_left,bisect_right
# from math import gcd,ceil,floor,factorial
# from fractions import gcd
from functools import reduce
from pprint import pprint

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
a = list(myinput())
b = list(myinput())
c = list(myinput())

a.sort()
b.sort()
c.sort()

# print(a)
# print(b)
# print(c)
# print("\n")

ls = [0]*n
for j in range(n):
    ind_a = bisect_left(a,b[j])
    ls[j] = ind_a
# print(ls)

ls_sum = [0]*n
s = 0
for i in range(n):
    s += ls[i]
    ls_sum[i] = s
# print(ls_sum)
     
count = 0
for k in range(n):
    ind_b = bisect_left(b,c[k])
    # print(k,ind_b)
    if ind_b==0:
        count += 0
    elif ind_b==n:
        count += ls_sum[-1]
    else:
        count += ls_sum[ind_b-1]
    # print(count)
print(count)