def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]
[h,w]=i2()
s=[]
c=0
for i in range(h):
 s.append(input())
 c+=s[-1].count("#")
d=[[float("inf") for i in range(w)]for j in range(h)]
import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
   global d
   d[x][y]=0
   q=[[x,y]]
   while len(q):
    v=q.pop(0)
    for i in [[0,1],[1,0],[0,-1],[-1,0]]:
      if 0<=v[0]+i[0]<h and 0<=v[1]+i[1]<w and d[v[0]+i[0]][v[1]+i[1]]==float("inf") and s[v[0]+i[0]][v[1]+i[1]]!="#":
         d[v[0]+i[0]][v[1]+i[1]]=min(d[v[0]+i[0]][v[1]+i[1]],d[v[0]][v[1]]+1)
         q.append([v[0]+i[0],v[1]+i[1]])
dfs(0,0)
if d[h-1][w-1]==float("inf"):
 print(-1)
else:
 print(h*w-c-d[h-1][w-1]-1)