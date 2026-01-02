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

def n_base(n,k):
    if n==0:
        return 0
    else:
        bi=''
        if k<0:
            while n!=0:
                bi+=str(n%abs(k))
                n=-(-n//k)
        else:
            while n!=0:
                bi+=str(n%abs(k))
                n=n//k
        return bi[::-1]

print(n_base(N,-2))