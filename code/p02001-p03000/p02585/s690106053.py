class UnionFind():
    n=1
    par=[0]
    rnk=[0]
    def __init__(self,size):
        self.n=size
        self.par=[i for i in range(self.n)]
        self.rnk=[0 for i in range(self.n)]
    def find(self,vertex1):
        if self.par[vertex1]==vertex1:
            return vertex1
        else:
            self.par[vertex1]=self.find(self.par[vertex1])
            return self.par[vertex1]
    def unite(self,vertex1,vertex2):
        vertex1=self.find(vertex1)
        vertex2=self.find(vertex2)
        if vertex1==vertex2:
            return
        if (self.rnk[vertex1]<self.rnk[vertex2]):
            self.par[vertex1]=vertex2
        else:
            self.par[vertex2]=vertex1
            if(self.rnk[vertex1]==self.rnk[vertex2]):
                self.rnk[vertex1]+=1
    def same(self,vetrex1,vertex2):
        return self.find(vetrex1)==self.find(vertex2)

N,K=map(int,input().split())
P=[int(i)-1 for i in input().split()]
C=[int(i) for i in input().split()]
G=UnionFind(N)
for i in range(N):
    G.unite(i,P[i])
D=dict()
for i in range(N):
    if G.find(i) in D:
        D[G.find(i)]+=1
    else:
        D[G.find(i)]=1

dp=[[0 for j in range(N)] for i in range(N+1)]
for j in range(N):
    dp[0][j]=j
for i in range(N):
    for j in range(N):
        dp[i+1][j]=P[dp[i][j]]
#1 3 4 0 2
#0->1->3->0, 2->4->2
score=[[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        score[i][j]=score[i-1][j]+C[dp[i+1][j]]
def maxpoint(j,L):
    if L<=N:
        return max([score[i][j] for i in range(L)])
    else:
        roop=D[G.find(j)]
        cyclepoint=score[roop-1][j]
        if cyclepoint<0:
            return maxpoint(j,roop)
        else:
            if L%roop!=0:
                return maxpoint(j,L%roop)+(L//roop)*cyclepoint
            else:
                return maxpoint(j,roop)+(-1+L//roop)*cyclepoint
ans=[maxpoint(j,K) for j in range(N)]
print(max(ans))
