import sys
from bisect import bisect_left,bisect_right,insort
input = sys.stdin.readline
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parent=list(range(n+1))
        self.size=[1]*(n+1)
    def find(self,x):
    #根を探す。
    #別なグループ間をつなげた場合は、つなげた先の根に書き換える。
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
    def unite(self,x,y):
    #二つのグループをつなげる
    #大きいほうに小さいほうをつなげる。
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        else:
            if self.size[x]>=self.size[y]:
                self.parent[y]=x
                self.size[x]+=self.size[y]
            else:
                self.parent[x]=y
                self.size[y]+=self.size[x]
    def cnt(self,x):
    #サイズの取得
        return self.size[self.find(x)]

def main():
    n,m,k=map(int,input().split())
    u=UnionFind(n)
    ans=[0]*(n+1)
    for i in range(m):
        a,b=map(int,input().split())
        ans[a]-=1
        ans[b]-=1
        u.unite(a,b)
    for i in range(k):
        a,b=map(int,input().split())
        if u.find(a)==u.find(b):
            ans[a]-=1
            ans[b]-=1
    for i in range(1,n+1):
        ans[i]+=u.cnt(i)-1
    print(" ".join(map(str,ans[1:])))

if __name__ == '__main__':
    main()