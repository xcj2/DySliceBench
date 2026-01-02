
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

class UnionFind:
    def __init__(self,N): # 頂点数 N
        self.table = [i for i in range(N)]    # 親 table[x] == x で根
        self.rank  = [1 for i in range(N)]    # 木の長さ
        self.size  = [1 for i in range(N)]    # 集合のサイズ

    def Find(self,x):    #xの根を返す
        if self.table[x] == x:
            return x
        else:
            self.table[x] = self.Find(self.table[x]) #親の更新
            self.size[x] = self.size[self.table[x]]
            return self.table[x]

    def Unite(self,x,y): #xとyをdiff(x,y)=W で繋げる
        x,y = self.Find(x), self.Find(y)
        sx,sy = self.Size(x), self.Size(y)
        if x == y: return
        if self.rank[x] > self.rank[y]:
            self.table[y] = x
            self.size[x] = sx + sy
        else:
            self.table[x] = y
            self.size[y] = sx + sy
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def Check(self,x,y):
        return self.Find(x) == self.Find(y)

    def Size(self,x):
        return self.size[self.Find(x)]


N = inp()
AA = inpl()
BB = inpl()

BA = []
for i in range(N):
    BA.append((BB[i],AA[i]))


BA.sort()
act_AA = [(A,ai) for ai,(B,A) in enumerate(BA)]

sorted_AA = sorted(act_AA)

UF = UnionFind(N)

# print(sorted_AA)

for i,(A,ai) in enumerate(sorted_AA):
    UF.Unite(i,ai)


if UF.Size(0) != N:
    for i in range(N):
        A = sorted_AA[i][0]
        B = BA[i][0]
        if A <= B:
            continue
        else:
            print("No")
            sys.exit()
    print("Yes")
else:

    for i in range(N):
        A = sorted_AA[i][0]
        B = BA[i][0]
        if A <= B:
            continue
        else:
            print("No")
            sys.exit()

    for i in range(N-1):
        A1 = sorted_AA[i][0]
        A2 = sorted_AA[i+1][0]
        B1 = BA[i][0]
        B2 = BA[i+1][0]
        if A1 <= B2 and A2 <= B1:
            print("Yes")
            sys.exit()

    print("No")
