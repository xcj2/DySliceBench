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

def index_sort(A):
    x = []
    for i,a in enumerate(A):
        x.append((a,i))
    return sorted(x, key=lambda x: x[0])

N = I()
X = III()

y = index_sort(X)
order = [0]*N
for i in range(N):
    order[y[i][1]] = i

for i in range(N):
    if order[i]<=(N-1)//2:
        print(y[(N+1)//2][0])
    else:
        print(y[(N-1)//2][0])