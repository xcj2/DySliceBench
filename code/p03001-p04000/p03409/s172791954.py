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

n = int(input())
ab = [ list(myinput()) for _ in range(n) ]
cd = [ list(myinput()) for _ in range(n) ]

count = 0
for i in range(n):
    cd_sorted = mysort(cd,0)
    bx = cd[0][0]
    by = cd[0][1]
    cd.remove([bx,by])
    ab.sort(key=lambda x:x[1],reverse=True)
    # print(cd)
    # print(ab)
    for j in range(len(ab)):
        rx = ab[j][0]
        ry = ab[j][1]
        if rx<bx and ry<by:
            count += 1
            ab.remove([rx,ry])
            break
        else:
            pass
print(count)