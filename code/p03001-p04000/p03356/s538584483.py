from collections import Counter,defaultdict,deque
import sys,bisect,math,itertools,string,queue,copy
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
 
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])
def sortx(x,n,k):
    if k == 0:x.sort(key=lambda y:y[1,n])
    else:x.sort(reversed=True, key=lambda y:y[1,n])
def graph():
    n,m=inpm()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=inpm()
        a-=1
        b-=1
        g[a].append(b)
        g[b].append(a)
    return n,m,g
 
def find(x): # 木の根を求める
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
 
def unite(x,y): # xとyの属する集合を併合
    x=find(x)
    y=find(y)
    if x==y:return
    if rank[x]<rank[y]:
        par[x]=y
    else:
        par[y]=x
        if rank[x]==rank[y]:
            rank[x]+=1
 
def same(x,y): # xとyが同じ集合に属するか判定
    return find(x)==find(y)
 
def main():
    n,m=inpm()
    global par,rank
    par=[i for i in range(n)]  # 親
    rank=[0 for _ in range(n)] # 木の深さ
    p=inpl()
    xy=[]
    for _ in range(m):
        x,y = inpm()
        if x>y:
            x,y=y,x
        xy.append([x,y])
    xy.sort()
    for i in range(m):
        x,y=xy[i]
        unite(x-1,y-1)
    groop=[[] for _ in range(n)]
    for i in range(n):
        groop[find(i)].append(i)
    ans=0
    for i in range(n):
        ps=[]
        for j in range(len(groop[i])):
            ps.append(p[groop[i][j]]-1)
        if ps==[]:
            continue
        else:
            ans+=len(set(ps)&set(groop[i]))
    print(ans)
 
if __name__ == "__main__":
    main()