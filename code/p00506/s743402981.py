from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
from math import gcd
from functools import reduce
from pprint import pprint

def myinput():
    return map(int,input().split())

def mylistinput(n):
    return [ list(myinput()) for _ in range(n) ]

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

# def gcd3(*numbers):
#     return reduce(gcd, numbers)

# def gcd3_list(numbers):
#     return reduce(gcd, numbers)

n = int(input())
numbers = list(myinput())

numbers.sort()
a = numbers[0]
b = numbers[1]
g = gcd(a,b)

if len(numbers)==2:
    ls = []
    for i in range(1,g+1):
        if a%i==0 and b%i==0:
            ls.append(i)
    for i in range(len(ls)):
        print(ls[i])
else:
    c = numbers[2]
    ls = []
    for i in range(1,g+1):
        if a%i==0 and b%i==0 and c%i==0:
            ls.append(i)
    for i in range(len(ls)):
        print(ls[i])
