import sys
input=sys.stdin.readline
 
 
class UnionFind(object):
    def __init__(self, n):
        self.parent={i:i for i in range(1,n+1)}
        self.size={i:1 for i in range(1,n+1)}
    def find(self, a):
        if self.parent[a]!=a:
            self.parent[a]=self.find(self.parent[a])
        return self.parent[a]
    def getsize(self, a):
        return self.size[self.find(a)]
    def unite(self, a, b):
        a=self.find(a)
        b=self.find(b)
        if a==b:return
        if self.size[a]>self.size[b]:
            self.size[a]+=self.size[b]
            self.parent[b]=a
        else:
            self.size[b]+=self.size[a]
            self.parent[a]=b
    def isunited(self, a, b):
        return self.find(a)==self.find(b)
 
 
def solve():
    N, M, K = map(int, input().split())

    uft = UnionFind(N)

    d = {i:set() for i in range(1, N+1)}
    # e:enemy　i番目の人のブロック関係の人数
    e = {i:0 for i in range(1, N+1)}
    # f:friend　i番目の人の友人関係の人数
    f = {i:0 for i in range(1, N+1)}
 
    for _ in range(M):
        A, B = map(int, input().split())
        d[A].add(B)
        d[B].add(A)
        f[A] += 1
        f[B] += 1
        # 友人関係はUnion-Findで
        uft.unite(A, B)
 
    for _ in range(K):
        C, D = map(int, input().split())
        # 同じグループかチェック　＝　友人の友人の…という状態かをチェック
        if uft.isunited(C, D):
            # if not D in d[C]:
            e[C] += 1
            # if not C in d[D]:
            e[D] += 1
 
    print(*(uft.getsize(i)-e[i]-f[i]-1 for i in range(1, N+1)))
 
 
if __name__ == "__main__":
    solve()