#グラフ上でのBFS
#s=始点 n=頂点数 e=隣接リスト
def glaph_bfs(s,n,e):
  Q=[s]
  visited={s}
  while Q:
    P=[]
    for i in Q:
      for j,_ in e[i]:
        if j in visited:continue
        visited.add(j)
        P.append(j)
    Q=P
  return visited
  

#負の閉路検出
#n=頂点数 e=[[a,b,c],[]...](a~bの距離がc)
def find_negative_loop(n,e):
	d=n*[10**20];d[0]=0
	for h in range(n):
		for i,j,k in e:
			if d[j]>d[i]+k:
				d[j]=d[i]+k
				if h==n-1:return True
	return False

#ベルマンフォード(d[i]=頂点sから頂点iの最短距離)
#単一始点最短経路(負の辺対応)
#s=始点 n=頂点数 e=[[a,b,c],[]...](a~bの距離がc)
def bellman_ford(s,n,e):
  inf=10**20;d=[inf]*n;d[s]=0
  while 1:
    f=True
    for i,j,k in e:
      if d[i]!=inf and d[j]>d[i]+k:d[j]=d[i]+k;f=False
    if f:break
  return d

n,m,p=map(int,input().split())
edge=[[]for _ in range(n)]
edger=[[]for _ in range(n)]
for _ in range(m):
  a,b,c=map(int,input().split())
  c-=p
  a-=1
  b-=1
  edge[a].append((b,c))
  edger[b].append((a,c))
visited=glaph_bfs(0,n,edge)
visitedr=glaph_bfs(n-1,n,edger)
for i in range(n):
  if not(i in visited and i in visitedr):edge[i]=[]
e=[]
for i in range(n):
  for j in range(len(edge[i])):e.append((i,edge[i][j][0],-edge[i][j][1]))
if find_negative_loop(n,e):print(-1);exit()
print(max(-bellman_ford(0,n,e)[n-1],0))