#065-D
#クラスカル法
import heapq
V=int(input())#Eは辺の数、Vは頂点の数
vlist=[]
eque=[]
for i in range(V):
    x,y=map(int,input().split())
    vlist.append([i,x,y])

vlist.sort(key=lambda x:x[1])
for i in range(V-1):
    heapq.heappush(eque,[vlist[i+1][1]-vlist[i][1],vlist[i][0],vlist[i+1][0]])

vlist.sort(key=lambda x:x[2])
for i in range(V-1):
    heapq.heappush(eque,[vlist[i+1][2]-vlist[i][2],vlist[i][0],vlist[i+1][0]])


#Union-Find木
par=[]
rank=[]
def init(a): #初期化
    for i in range(a):
        par.append(i)
        rank.append(0)
def find(x): #根を見つける
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
    return par[x]
def unite(x,y): #併合
    x=find(x)
    y=find(y)
    if rank[x]==rank[y]:
        par[x]=y
    else:
        par[y]=x
        if rank[x]==rank[y]:
            rank[x]+=1
    return
def same(x,y): #同じ集合か判定
    return find(x)==find(y)

init(V) #同じ木に属しているかどうかはUFTで判断する、初めは全部孤立した木

res=0 #合計コスト
while len(eque)!=0:
    te=heapq.heappop(eque)
    cost,u,v=te[0],te[1],te[2]
    if same(u,v): #同じ木に属していたら閉路ができるのでcontinue
        continue
    res+=cost
    unite(u,v) #辺を追加したら同じ木にする

print(res)