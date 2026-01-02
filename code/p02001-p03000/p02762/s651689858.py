class UnionFind:
  def __init__(self, N):
    self.par=[i for i in range(N)]
    self.rank=[0 for _ in range(N)]
    self.size=[1 for _ in range(N)]
    
  def unite(self, x, y):
    x=self.getroot(x)
    y=self.getroot(y)
    if x!=y:
      if self.rank[x]<self.rank[y]:
        x, y=y, x
      if self.rank[x]==self.rank[y]:
        self.rank[x]+=1
      self.par[y]=x
      self.size[x]+=self.size[y]
      
  def united(self, x, y):
    return self.getroot(x)==self.getroot(y)
      
  def getroot(self, x):
    if self.par[x]==x:
      return x
    else:
      self.par[x]=self.getroot(self.par[x])
      return self.par[x]

  def getsize(self, x):
    return self.size[self.getroot(x)]
  
def LN2NL(N, LN):
  out=[[] for _ in range(N)]
  M=len(LN)
  for i in range(M):
    out[LN[i][0]].append(LN[i][1])
    out[LN[i][1]].append(LN[i][0])
  return out

N, M, K=map(int, input().split())
UF=UnionFind(N+1)
AB=[list(map(int, input().split())) for _ in range(M)]
CD=[list(map(int, input().split())) for _ in range(K)]
ABNL=LN2NL(N+1, AB)
CDNL=LN2NL(N+1, CD)

for i in range(M):
  UF.unite(AB[i][0], AB[i][1])
  
ans=[UF.getsize(i)-len(ABNL[i])-1 for i in range(N+1)]
for i in range(1, N+1):
  for j in range(len(CDNL[i])):
    if UF.united(i, CDNL[i][j]):
      ans[i]-=1
      
print(*ans[1:])