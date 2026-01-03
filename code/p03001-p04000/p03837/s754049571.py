class WarshallFloyd:
    def __init__(self,V,inf):
        self.V=V
        self.inf=inf
        self.G=[[inf]*V for _ in range(V)]
        for i in range(V):
            self.G[i][i]=0

    def add(self,u,v,cost):
        self.G[u][v]=min(self.G[u][v],cost)

    def shortest_path(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    self.G[i][j]=min(self.G[i][j],self.G[i][k]+self.G[k][j])
        return self.G

    def exist_negative_loop(self):
        for i in range(self.V):
            if self.G[i][i]<0:
                return True
        return False

from sys import stdin
def main():
    #入力
    readline=stdin.readline
    inf=10**9
    n,m=map(int,readline().split())
    wf=WarshallFloyd(n,inf)
    a=[0]*m
    b=[0]*m
    c=[0]*m
    for i in range(m):
        a[i],b[i],c[i]=map(int,readline().split())
        a[i]-=1
        b[i]-=1
        wf.add(a[i],b[i],c[i])
        wf.add(b[i],a[i],c[i])

    li=wf.shortest_path()

    flags=[False]*m
    for i in range(m):
        v=a[i]
        u=b[i]
        w=c[i]
        for j in range(n):
            for k in range(n):
                if li[j][v]+w+li[u][k]==li[j][k]:
                    flags[i]=True

    print(len([i for i in range(m) if flags[i]==False]))

if __name__=="__main__":
    main()