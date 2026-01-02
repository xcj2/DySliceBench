#### import ####
import sys
import math
from collections import defaultdict

#### 設定 ####
sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

#### 定数 ####
mod = 10**9 + 7

#### 読み込み ####
def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

N = I()

val = [1]
temp = 1
while 1:
    temp *= 6
    if temp<=10**5:
        val.append(temp)
    else:
        break

temp = 1
while 1:
    temp *= 9
    if temp<=10**5:
        val.append(temp)
    else:
        break

val.sort(reverse=True)

def rec(price,i):
    if i==len(val)-1:
        return price
    else:
        q,m = divmod(price,val[i])
        if m==0:
            return q
        else:
            if q>=9:
                return float('inf')
            else:
                x = []
                for j in range(q+1):
                    x.append(rec(price-j*val[i],i+1) + j)
                return min(x)

print(rec(N,0))