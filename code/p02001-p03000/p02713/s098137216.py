from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import Counter
from pprint import pprint
from math import gcd
from functools import reduce

def myinput():
    return map(int,input().split())

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
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

k = int(input())

def gcd3(*numbers):
    return reduce(gcd, numbers)

ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            ans += gcd3(a,b,c)
print(ans)