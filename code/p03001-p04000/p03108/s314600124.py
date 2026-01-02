from collections import Counter,defaultdict,deque
import sys
import copy
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
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

def find(x): # 木の根を求める
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
        
def unite(x,y): # xとyの属する集合を併合
    x=find(x)
    y=find(y)
    if x==y:
        ans.append(0)
        return
    ans.append(num[x]*num[y])
    z=num[x]+num[y]
    num[x]=z
    num[y]=z
    if rank[x]<rank[y]:
        par[x]=y
    else:
        par[y]=x
        if rank[x]==rank[y]:
            rank[x]+=1

def same(x,y): # xとyが同じ集合に属するか判定
    return find(x)==find(y)

def main():
    n,m = map(int,input().split()) 

    global par,rank,num,ans
    par=[i for i in range(n)]  # 親
    rank=[0 for _ in range(n)] # 木の深さ
    num=[1 for _ in range(n)] # 木の大きさ
    ans=[]
    ab=[]
    for _ in range(m):
        a,b = map(int,input().split())
        ab.append((a-1,b-1))
    for i in range(m-1,-1,-1):
        unite(ab[i][0],ab[i][1])
    p=(n*(n-1))//2
    x=[]
    for i in range(m):
        x.append(p)
        p-=ans[i]
        if p<0:
            p=0
    x.reverse()
    for i in range(m):
        print(x[i])
    

if __name__ == "__main__":
    main()