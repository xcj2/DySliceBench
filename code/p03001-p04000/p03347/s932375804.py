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

def graphm():
    n=inp()
    g=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b,w=inpm()
        a-=1
        b-=1
        g[a].append((b,w))
        g[b].append((a,w))
    return n,g

def main():
    n=inp()
    a=inplm(n)
    ans=0
    if a[0]!=0:
        print(-1)
        return
    for i in range(n-1):
        if a[i+1]>a[i]+1:
            print(-1)
            return
        if a[i+1]==a[i]:
            ans+=a[i]
        elif a[i+1]>a[i]:
            ans+=1
        elif a[i]>a[i+1]:
            ans+=a[i+1]
    print(ans)
if __name__ == "__main__":
    main()
