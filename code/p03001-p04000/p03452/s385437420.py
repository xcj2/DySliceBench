"""
unionFind木を使う。
根に対する距離を記録していく。
"""
import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents = [i for i in range(n+1)]
        self.distance = [0]*(n+1)

    def find(self,x):
        if self.parents[x]==x:
            return x,0
        else:
            self.parents[x],dist2=self.find(self.parents[x])
            self.distance[x] += dist2
            return self.parents[x],self.distance[x]

    def union(self,l,r,dist):
        lRoot,lDist = self.find(l)
        rRoot,rDist = self.find(r)
        #まず、位置関係に矛盾がないかを調べる
        #lRootはlよりlDist右にいる
        #rRootはrよりrDist右にいる
        #lRoot=rRootのとき、lDist-rDist != distなら矛盾。
        if lRoot==rRoot and lDist-rDist != dist:
            print("No")
            exit()

        #より左にいる根を右にいる根にマージする
        if lDist < dist+rDist:
            #lRootがrRootよりも左の場合
            self.parents[lRoot]=rRoot
            self.distance[lRoot]=(dist+rDist)-lDist
        else:
            self.parents[rRoot]=lRoot
            self.distance[rRoot]=lDist-(dist+rDist)

N,M = map(int,input().split())
tree = UnionFind(N)
for i in range(M):
    L,R,D = map(int,input().split())
    tree.union(L,R,D)

print('Yes')