import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# 各森の最小値を使う
# 後は全体から最小値を順に取ってくればよい

class UF(object):
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.size = [1]*n

    # x が属する集合の代表値を返す
    def find(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # x と y の集合を結合する
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    # x と y が同じ集合に属するか判定する
    def is_same(self,x,y):
        return self.find(x) == self.find(y)

    # x が属する集合の要素数を返す
    def get_size(self,x):
        x = self.find(x)
        return self.size[x]

N,M = LI()
a = LI()
x,y = LIR(M,2)

uf = UF(N)
for i in range(M):
    uf.union(x[i],y[i])

d = defaultdict(list)
for i in range(N):
    d[uf.find(i)].append(a[i])

for g in d.values():
    g.sort(reverse=True)

if 2*(len(d)-1) > N:
    print('Impossible')
else:
    if len(d) == 1:
        print(0)
        exit()
    ans = 0
    num = 0
    for gr in d.values():
        ans += gr.pop()
        num += 1
    left = []
    for gr in d.values():
        left.extend(gr)
    left.sort()
    for i in range(2*(len(d)-1)-num):
        ans += left[i]
    print(ans)