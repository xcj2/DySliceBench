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

from collections import Counter

n = I()
v = III()

if v==[v[0]]*len(v):
    print(len(v)//2)
    exit()

x = [v[i] for i in range(0,n,2)]
y = [v[i] for i in range(1,n,2)]

xc = Counter(x)
yc = Counter(y)
xval = xc.most_common(1)[0][0]
yval = yc.most_common(1)[0][0]
xnum = xc.most_common(1)[0][1]
ynum = yc.most_common(1)[0][1]

if xval!=yval:
    print(len(x)-xnum+len(y)-ynum)
else:
    if xnum==len(x):
        print(min(len(x)+len(y)-ynum, len(x)-xnum+len(y)-yc.most_common(2)[1][1]))
    elif ynum==len(y):
        print(min(len(x)-xnum+len(y), len(x)-xc.most_common(2)[1][1]+len(y)-ynum))
    else:
        print(min(len(x)-xc.most_common(2)[1][1]+len(y)-ynum, len(x)-xnum+len(y)-yc.most_common(2)[1][1]))