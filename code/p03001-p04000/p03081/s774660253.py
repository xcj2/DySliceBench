import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,Q = II()
s = str(input())
read = [tuple(map(str, input().split())) for _ in range(Q)]
t,d = map(list, zip(*read))

def is_l_not_delete(i):
    flag = True
    place = i
    for j in range(Q):
        if t[j]==s[place]:
            if d[j]=='L':
                place -= 1
            else:
                place += 1
        if place<0:
            flag = False
            break
        if place>=N:
            break
    return flag

def is_r_delete(i):
    flag = False
    place = i
    for j in range(Q):
        if t[j]==s[place]:
            if d[j]=='L':
                place -= 1
            else:
                place += 1
        if place<0:
            break
        if place>=N:
            flag = True
            break
    return flag

delete = 0

left = -1
right = N
while right-left>1:
    mid = left+(right-left)//2
    if is_l_not_delete(mid):
        right = mid
    else:
        left = mid
delete += right

left = -1
right = N
while right-left>1:
    mid = left+(right-left)//2
    if is_r_delete(mid):
        right = mid
    else:
        left = mid
delete += N-right

print(N-delete)