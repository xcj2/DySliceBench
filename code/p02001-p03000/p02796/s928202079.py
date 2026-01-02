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
    return data.sort(key=lambda x:x[col],reverse=True)

n = int(input())
xl = [ list(myinput()) for _ in range(n) ]
# print(xl)

ls = []
for i in range(n):
    x = xl[i][0]
    l = xl[i][1]
    s = x - l
    e = x + l
    d = [s,e]
    ls.append(d)
# print(ls)
ls.sort(key=lambda x:x[1],reverse=False)
# print(ls)

count = 0
e = -1*float("inf")
for i in range(n):
    ns,ne = ls[i]
    if ns>=e:
        count += 1
        e = copy(ne)
    else:
        pass

print(count)