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
    h,w=map(int,readline().split())
    c=[list(map(int,readline().split())) for _ in range(10)]
    a=[list(map(int,readline().split())) for _ in range(h)]
    wf=WarshallFloyd(10,inf)
    for i in range(10):
        for j in range(10):
            if i==j: pass
            else: wf.add(i,j,c[i][j])

    tmp=wf.shortest_path()
    to_one=[tmp[i][1] for i in range(10)]

    ans=0
    for i in range(h):
        for j in range(w):
            if a[i][j]==-1: pass
            else:
                ans+=to_one[a[i][j]]

    print(ans)

if __name__=="__main__":
    main()