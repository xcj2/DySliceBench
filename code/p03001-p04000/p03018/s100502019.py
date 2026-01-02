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

S = str(input())
S = S.replace('BC', 'D')

ans = 0
a = 0
d = 0
flag = False
for s in S[::-1]:
    if s=='D':
        if a>=1:
            ans += a*d
            a = 0
        d += 1
        flag = True
    elif s=='A':
        if flag:
            a += 1
    else:
        ans += a*d
        a,d = 0,0
        flag = False
ans += a*d

print(ans)