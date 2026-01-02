import sys
readline = sys.stdin.buffer.readline

from collections import deque
from copy import copy,deepcopy
from itertools import permutations,combinations
from pprint import pprint

def myinput():
    return map(int,input().split())

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
    return data

n,m = myinput()
ab = [ list(myinput()) for _ in range(m) ]
# print(ab)

ab_sorted = mysort(ab,1)
# print(ab_sorted)

count = 0
e = 0
for i in range(m):
    ns = ab_sorted[i][0]
    ne = ab_sorted[i][1]
    if ns>=e:
        count += 1
        e = ne
    else:
        pass
print(count)