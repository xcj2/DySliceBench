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
    n,m=map(int,input().split())
    ab=[list(map(int,input().split())) for _ in range(m)][::-1]
    u=UnionFind(n)
    ans=[0]*(m+1)
    ans[0]=n*(n-1)//2
    for i in range(m):
        a,b=ab[i][0],ab[i][1]
        if u.find(a)==u.find(b):
            ans[i+1]=ans[i]
        else:
            ans[i+1]=ans[i]-u.cnt(a)*u.cnt(b)
            u.unite(a,b)
    for i in ans[m-1::-1]:
        print(i)

if __name__ == '__main__':
    main()