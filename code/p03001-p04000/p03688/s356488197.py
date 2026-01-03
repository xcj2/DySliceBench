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
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(map(int, input().split())) for _ in range(N)]
        return map(list,zip(*read_all))

#################

N = I()
a = III()

small = a[0]
large = a[0]

for i in range(1,N):
    if a[i]>small:
        large = a[i]
        break
    if a[i]<small:
        large = small
        small = a[i]
        break

if small != large:
    if large!=small+1:
        print('No')
        exit()
    small_num = 0
    large_num = 0
    for i in range(N):
        if a[i]==small:
            small_num += 1
        else:
            large_num += 1
    num = large_num
    val = large-small_num
    if 2*val<=num and val>=1:
        print('Yes')
    else:
        print('No')
else:
    num = N
    val = large
    if val+1==num:
        print('Yes')
    elif 2*val<=num:
        print('Yes')
    else:
        print('No')