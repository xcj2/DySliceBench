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
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
uni = UnionFind(N)
for _ in range(M):
    a, b, d = map(int, input().split())
    uni.Unite(a-1, b-1)
    graph[a-1].append((d, b-1))
    graph[b-1].append((-d, a-1))

INF = 10**14
A = [INF]*N
def bfs(start):
    q = [start]
    A[start] = 0
    while q:
        qq = []
        for p in q:
            for d, np in graph[p]:
                if A[np] == INF:
                    A[np] = A[p] + d
                    qq.append(np)
                elif A[np] != A[p]+d:
                    return False
        q = qq
    return True

root = set()
for i in range(N):
    root.add(uni.Find_Root(i))

ok = True
for r in root:
    ok = ok and bfs(r)

print("Yes" if ok else "No")