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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,K = II()
a = III()

cuma = [a[0]]
for i in range(1,N):
    cuma.append(cuma[-1]+a[i])

val = []
for i in range(N):
    for j in range(i,N):
        if i==0:
            val.append(cuma[j])
        else:
            val.append(cuma[j]-cuma[i-1])

val.sort(reverse=True)

ans = 0
use = [True]*len(val)
for i in range(val[0].bit_length())[::-1]:
    ok_num = 0
    ng_list = []
    for j in range(len(val)):
        if not use[j]:
            continue
        else:
            if val[j]>>i&1:
                ok_num += 1
            else:
                ng_list.append(j)
    if ok_num>=K:
        ans += 2**i
        for n in ng_list:
            val[n] = False

print(ans)