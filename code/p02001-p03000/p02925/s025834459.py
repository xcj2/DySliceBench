import sys
sys.setrecursionlimit(10000)

n=int(input())
a=[[0]*(n-1) for i in range(n)]
id=[[-1]*(n) for i in range(n)]
MAXV=n*(n-1)//2
to=[[]*(n) for i in range(MAXV)]
  
def toId(i,j):
  if (i>j):
    i,j=j,i
  return id[i][j]


visited=[False]*MAXV
calculated=[False]*MAXV
dp=[0]*MAXV
def dfs(v):
  if visited[v]:
    if not calculated[v]:
      return -1
    return dp[v]
  visited[v]=True
  dp[v]=1
  for u in to[v]:
    res = dfs(u)
    if res==-1:
      return -1
    dp[v]=max(dp[v], res+1)
  calculated[v]=True
  return dp[v]


def main():
  for i in range(n):
    a[i]=list(map(lambda x:int(x)-1,input().split()))
  v=0
  for i in range(n):
    for j in range(n):
      if i<j:
        id[i][j]=v
        v+=1
  for i in range(n):
    for j in range(n-1):
      a[i][j]=toId(i,a[i][j])
    for j in range(n-2):
      to[a[i][j+1]].append(a[i][j])
      
  ans=0
  for i in range(v):
    res=dfs(i)
    if res==-1:
      print(-1)
      exit(0)
    ans=max(ans, res)

  print(ans)
  
  
  
if __name__=='__main__':
  main()