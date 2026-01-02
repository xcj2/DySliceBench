class UnionFind():
    # 作りたい要素数nで初期化
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズ
    def Count(self, x):
        return -self.root[self.Find_Root(x)]


import sys
input = sys.stdin.buffer.readline
from operator import itemgetter

N, M = map(int, input().split())
W = list(map(int, input().split()))
ABY = [list(map(int, input().split())) for _ in range(M)]

ABY.sort(key=itemgetter(2))

uni = UnionFind(N)
dic = {}
for i, w in enumerate(W):
    dic[i] = (w, 0)

for a1, a2, y in ABY:
    a1 -= 1; a2 -= 1
    r1 = uni.Find_Root(a1)
    r2 = uni.Find_Root(a2)
    w1, c1 = dic[r1]
    w2, c2 = dic[r2]
    if r1 == r2:
        c = 0 if y <= w1 else c1 + 1  
        dic[r1] = (w1, c)
    else:
        w = w1 + w2
        c = 0 if y <= w else c1 + c2 + 1
        uni.Unite(r1, r2)
        r = uni.Find_Root(r1)
        dic[r] = (w, c)

r = uni.Find_Root(0)
_, ans = dic[r]
print(ans)