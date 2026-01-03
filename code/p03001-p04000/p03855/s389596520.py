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
def inpln(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])
def sortx(x,n,k):
    if k == 0:x.sort(key=lambda y:y[1,n])
    else:x.sort(reversed=True, key=lambda y:y[1,n])

def find(x): # 木の根を求める
    if par[x]==x:
        return x
    else:
        return find(par[x])

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
    n,k,l = inpm()
 
    global par,rank
    par  = [i for i in range(2*n)]
    rank = [-1 for _ in range(2*n)] 
    for _ in range(k):
        p,q = inpm()
        p-=1
        q-=1
        unite(p,q)
    for _ in range(l):
        r,s = inpm()
        r-=1
        s-=1
        unite(r+n,s+n)

    root_s=defaultdict(int)
    root=[]
    for i in range(n):
        root.append(str(find(i))+' '+str(find(i+n)))
        root_s[root[i]]+=1
    
    ans=[0 for _ in range(n)]
    for i in range(n):
        ans[i] = root_s[root[i]]
    print(*ans) 


if __name__ == "__main__":
    main()
