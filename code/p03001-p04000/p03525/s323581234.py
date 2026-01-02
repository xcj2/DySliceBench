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

from itertools import product

N = I()
D = III()

if 0 in D:
    print(0)
elif N>=24:
    print(0)
elif N==23:
    D.sort()
    for i in range(N):
        if D[i]!=i//2+1:
            print(0)
            exit()
    print(1)
else:
    a = list(product([0,1],repeat=N))
    ans = 0
    for a0 in a:
        l = [False]*24
        flag = False
        for i in range(N):
            if a0[i]==0:
                if l[D[i]]:
                    flag = True
                    break
                else:
                    l[D[i]] = True
            else:
                if l[24-D[i]]:
                    flag = True
                    break
                else:
                    l[24-D[i]] = True
        if flag:
            continue
        before = 0
        val = 13
        for i in range(24):
            if l[i]:
                temp = min(i-before, 24-i+before)
                before = i
                if temp<val:
                    val = temp
        temp = min(before,24-before)
        if temp<val:
            val = temp
        if val>ans:
            ans = val
    print(ans)